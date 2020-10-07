#! /usr/bin/python3

import configparser

import requests


config = configparser.ConfigParser()
config.read("/usr/local/shodan/etc/shodan.ini")


class Shodan:
    def __init__(self):
        self.api_key = config["Api"]["key"]
        self.base_url = "https://api.shodan.io"

    def shodan_host_ip(self, value):
        api_url = "{}/shodan/host/{}".format(self.base_url, value)
        params = {"key": self.api_key}
        return requests.get(api_url, params=params)

    def shodan_protocols(self):
        api_url = "{}/shodan/protocols".format(self.base_url)
        params = {"key": self.api_key}
        return requests.get(api_url, params=params)

    def account_profile(self):
        api_url = "{}/account/profile".format(self.base_url)
        params = {"key": self.api_key}
        return requests.get(api_url, params=params)

    def dns_domain_domain(self, value):
        api_url = "{}/dns/domain/{}".format(self.base_url, value)
        params = {"key": self.api_key}
        return requests.get(api_url, params=params)

    def dns_resolve(self, value):
        api_url = "{}/dns/resolve".format(self.base_url)
        params = {
            "key": self.api_key,
            "hostnames": value,
        }
        return requests.get(api_url, params=params)

    def dns_reverse(self, value):
        api_url = "{}/dns/reverse".format(self.base_url)
        params = {
            "key": self.api_key,
            "ips": value,
        }
        return requests.get(api_url, params=params)

    def tools_httpheaders(self):
        api_url = "{}/tools/httpheaders".format(self.base_url)
        params = {"key": self.api_key}
        return requests.get(api_url, params=params)

    def tools_myip(self):
        api_url = "{}/tools/myip".format(self.base_url)
        params = {"key": self.api_key}
        return requests.get(api_url, params=params)

    def api_info(self):
        api_url = "{}/api-info".format(self.base_url)
        params = {"key": self.api_key}
        return requests.get(api_url, params=params)

    def labs_honeyscore(self, value):
        api_url = "{}/labs/honeyscore/{}".format(self.base_url, value)
        params = {"key": self.api_key}
        return requests.get(api_url, params=params)
