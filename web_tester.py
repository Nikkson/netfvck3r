import requests
import re
import urllib.parse as urlparse
import bs4 as BeautifulSoup


class WebTester:
    def __init__(self, url, login_url, ignore_links):
        self.session = requests.Session()
        self.target_url = url
        self.login_url = login_url
        self.target_links = []
        self.links_to_ignore = ignore_links
        self.sqli_test_string = "' or 1=1 #"
        self.xss_test_script = "<sCript>alert('test')</scriPt>"
        self.vulnerabilities = []

    def extract_links_from(self, url):
        try:
            response = self.session.get(url)
            return re.findall('(?:href=")(.*?)"', response.content.decode())
        except UnicodeDecodeError:
            pass

    def crawl(self, url=None):
        if url is None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        if href_links is not None:
            for link in href_links:
                link = urlparse.urljoin(url, link)

                if "#" in link:
                    link = link.split("#")[0]

                if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
                    self.target_links.append(link)
                    self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup.BeautifulSoup(response.content, "lxml")
        return parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urlparse.urljoin(url, action)
        method = form.get("method")

        inputs_list = form.findAll("input")
        post_data = {}
        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value

            post_data[input_name] = input_value
        if method == "post":
            return self.session.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                is_vulnerable_to_xss = self.test_xss_in_form(form, link)
                if is_vulnerable_to_xss:
                    vuln_dict = {"vulnerability": "XSS", "url": link, "form_or_url": "Form",
                                "injection_string": self.xss_test_script}
                    self.vulnerabilities.append(vuln_dict)

                is_vulnerable_to_sqli = self.test_sql_injection_in_form(form, link)
                if is_vulnerable_to_sqli:
                    vuln_dict = {"vulnerability": "SQL Injection", "url": link, "form_or_url": "Form",
                                "injection_string": self.sqli_test_string}
                    self.vulnerabilities.append(vuln_dict)
                test_params_in_link = self.submit_form(form, "test", link)
                if "=" in test_params_in_link.url:
                    is_vulnerable_to_xss = self.test_xss_in_link(test_params_in_link.url)
                    if is_vulnerable_to_xss:
                        vuln_dict = {"vulnerability": "XSS", "url": link, "form_or_url": "URL",
                                    "injection_string": self.xss_test_script}
                        self.vulnerabilities.append(vuln_dict)
                    is_vulnerable_to_sqli = self.test_sql_injection_in_link(test_params_in_link.url)
                    if is_vulnerable_to_sqli:
                        vuln_dict = {"vulnerability": "SQL Injection", "url": link, "form_or_url": "URL",
                                    "injection_string": self.sqli_test_string}
                        self.vulnerabilities.append(vuln_dict)

            if "=" in link:
                is_vulnerable_to_xss = self.test_xss_in_link(link)
                if is_vulnerable_to_xss:
                    vuln_dict = {"vulnerability": "XSS", "url": link, "form_or_url": "URL",
                                "injection_string": self.xss_test_script}
                    self.vulnerabilities.append(vuln_dict)

                is_vulnerable_to_sqli = self.test_sql_injection_in_link(link)
                if is_vulnerable_to_sqli:
                    vuln_dict = {"vulnerability": "SQL Injection", "url": link, "form_or_url": "URL",
                                "injection_string": self.sqli_test_string}
                    self.vulnerabilities.append(vuln_dict)

    def test_xss_in_link(self, url):
        url = url.replace("=", "=" + self.xss_test_script)
        response = self.session.get(url)
        return bytes(self.xss_test_script, encoding="utf-8") in response.content

    def test_xss_in_form(self, form, url):
        response = self.submit_form(form, self.xss_test_script, url)
        return bytes(self.xss_test_script, encoding="utf-8") in response.content

    def test_sql_injection_in_link(self, url):
        url = re.sub(r'(?:=)(.*?)(?:&)', "=" + urlparse.quote(self.sqli_test_string) + "&", url)
        response = self.session.get(url)
        return bytes(self.sqli_test_string, encoding="utf-8") in response.content

    def test_sql_injection_in_form(self, form, url):
        response = self.submit_form(form, self.sqli_test_string, url)
        return bytes(self.sqli_test_string, encoding="utf-8") in response.content

    def start(self, data_dict):
        self.session.post(self.login_url, data=data_dict)
        self.crawl()
        self.run_scanner()
        return self.vulnerabilities
