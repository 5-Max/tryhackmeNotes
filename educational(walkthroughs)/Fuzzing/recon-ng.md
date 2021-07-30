https://github.com/lanmaster53/recon-ng

https://www.geeksforgeeks.org/recon-ng-installation-on-kali-linux/

https://sushant747.gitbooks.io/total-oscp-guide/content/finding_subdomains.html

create workspace and look at marketplace
```bash
[recon-ng][default] > workspace 
[!] Invalid command: workspace.
[recon-ng][default] > workspaces
Manages workspaces

Usage: workspaces <create|list|load|remove> [...]

[recon-ng][default] > workspaces create first
[recon-ng][first] > marketplace search

  +---------------------------------------------------------------------------------------------------+
  |                        Path                        | Version |     Status    |  Updated   | D | K |
  +---------------------------------------------------------------------------------------------------+
  | discovery/info_disclosure/cache_snoop              | 1.1     | not installed | 2020-10-13 |   |   |
  | discovery/info_disclosure/interesting_files        | 1.1     | not installed | 2020-01-13 |   |   |
  | exploitation/injection/command_injector            | 1.0     | not installed | 2019-06-24 |   |   |
  | exploitation/injection/xpath_bruter                | 1.2     | not installed | 2019-10-08 |   |   |
  | import/csv_file                                    | 1.1     | not installed | 2019-08-09 |   |   |
  | import/list                                        | 1.1     | not installed | 2019-06-24 |   |   |
  | import/masscan                                     | 1.0     | not installed | 2020-04-07 |   |   |
  | import/nmap                                        | 1.1     | not installed | 2020-10-06 |   |   |
  | recon/companies-contacts/bing_linkedin_cache       | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/companies-contacts/censys_email_address      | 2.0     | not installed | 2021-05-11 | * | * |
  | recon/companies-contacts/pen                       | 1.1     | not installed | 2019-10-15 |   |   |
  | recon/companies-domains/censys_subdomains          | 2.0     | not installed | 2021-05-10 | * | * |
  | recon/companies-domains/pen                        | 1.1     | not installed | 2019-10-15 |   |   |
  | recon/companies-domains/viewdns_reverse_whois      | 1.0     | not installed | 2019-08-08 |   |   |
  | recon/companies-domains/whoxy_dns                  | 1.1     | not installed | 2020-06-17 |   | * |
  | recon/companies-hosts/censys_org                   | 2.0     | not installed | 2021-05-11 | * | * |
  | recon/companies-hosts/censys_tls_subjects          | 2.0     | not installed | 2021-05-11 | * | * |
  | recon/companies-multi/github_miner                 | 1.1     | not installed | 2020-05-15 |   | * |
  | recon/companies-multi/shodan_org                   | 1.1     | not installed | 2020-07-01 | * | * |
  | recon/companies-multi/whois_miner                  | 1.1     | not installed | 2019-10-15 |   |   |
  | recon/contacts-contacts/abc                        | 1.0     | not installed | 2019-10-11 | * |   |
  | recon/contacts-contacts/mailtester                 | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/contacts-contacts/mangle                     | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/contacts-contacts/unmangle                   | 1.1     | not installed | 2019-10-27 |   |   |
  | recon/contacts-credentials/hibp_breach             | 1.2     | not installed | 2019-09-10 |   | * |
  | recon/contacts-credentials/hibp_paste              | 1.1     | not installed | 2019-09-10 |   | * |
  | recon/contacts-credentials/scylla                  | 1.3     | not installed | 2020-09-14 |   |   |
  | recon/contacts-domains/migrate_contacts            | 1.1     | not installed | 2020-05-17 |   |   |
  | recon/contacts-profiles/fullcontact                | 1.1     | not installed | 2019-07-24 |   | * |
  | recon/credentials-credentials/adobe                | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/credentials-credentials/bozocrack            | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/credentials-credentials/hashes_org           | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/domains-companies/censys_companies           | 2.0     | not installed | 2021-05-10 | * | * |
  | recon/domains-companies/pen                        | 1.1     | not installed | 2019-10-15 |   |   |
  | recon/domains-companies/whoxy_whois                | 1.1     | not installed | 2020-06-24 |   | * |
  | recon/domains-contacts/hunter_io                   | 1.3     | not installed | 2020-04-14 |   | * |
  | recon/domains-contacts/metacrawler                 | 1.1     | not installed | 2019-06-24 | * |   |
  | recon/domains-contacts/pen                         | 1.1     | not installed | 2019-10-15 |   |   |
  | recon/domains-contacts/pgp_search                  | 1.4     | not installed | 2019-10-16 |   |   |
  | recon/domains-contacts/whois_pocs                  | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/domains-contacts/wikileaker                  | 1.0     | not installed | 2020-04-08 |   |   |
  | recon/domains-credentials/pwnedlist/account_creds  | 1.0     | not installed | 2019-06-24 | * | * |
  | recon/domains-credentials/pwnedlist/api_usage      | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/domains-credentials/pwnedlist/domain_creds   | 1.0     | not installed | 2019-06-24 | * | * |
  | recon/domains-credentials/pwnedlist/domain_ispwned | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/domains-credentials/pwnedlist/leak_lookup    | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/domains-credentials/pwnedlist/leaks_dump     | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/domains-credentials/scylla                   | 1.3     | not installed | 2020-09-25 |   |   |
  | recon/domains-domains/brute_suffix                 | 1.1     | not installed | 2020-05-17 |   |   |
  | recon/domains-hosts/binaryedge                     | 1.2     | not installed | 2020-06-18 |   | * |
  | recon/domains-hosts/bing_domain_api                | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/domains-hosts/bing_domain_web                | 1.1     | not installed | 2019-07-04 |   |   |
  | recon/domains-hosts/brute_hosts                    | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/domains-hosts/builtwith                      | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/domains-hosts/censys_domain                  | 2.0     | not installed | 2021-05-10 | * | * |
  | recon/domains-hosts/certificate_transparency       | 1.2     | not installed | 2019-09-16 |   |   |
  | recon/domains-hosts/google_site_web                | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/domains-hosts/hackertarget                   | 1.1     | installed     | 2020-05-17 |   |   |
  | recon/domains-hosts/mx_spf_ip                      | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/domains-hosts/netcraft                       | 1.1     | not installed | 2020-02-05 |   |   |
  | recon/domains-hosts/shodan_hostname                | 1.1     | not installed | 2020-07-01 | * | * |
  | recon/domains-hosts/spyse_subdomains               | 1.0     | not installed | 2020-07-07 |   | * |
  | recon/domains-hosts/ssl_san                        | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/domains-hosts/threatcrowd                    | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/domains-hosts/threatminer                    | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/domains-vulnerabilities/ghdb                 | 1.1     | not installed | 2019-06-26 |   |   |
  | recon/domains-vulnerabilities/xssed                | 1.1     | not installed | 2020-10-18 |   |   |
  | recon/hosts-domains/migrate_hosts                  | 1.1     | not installed | 2020-05-17 |   |   |
  | recon/hosts-hosts/bing_ip                          | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/hosts-hosts/censys_hostname                  | 2.0     | not installed | 2021-05-10 | * | * |
  | recon/hosts-hosts/censys_ip                        | 2.0     | not installed | 2021-05-10 | * | * |
  | recon/hosts-hosts/censys_query                     | 2.0     | not installed | 2021-05-10 | * | * |
  | recon/hosts-hosts/ipinfodb                         | 1.1     | not installed | 2020-06-08 |   | * |
  | recon/hosts-hosts/ipstack                          | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/hosts-hosts/resolve                          | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/hosts-hosts/reverse_resolve                  | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/hosts-hosts/ssltools                         | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/hosts-hosts/virustotal                       | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/hosts-locations/migrate_hosts                | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/hosts-ports/binaryedge                       | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/hosts-ports/shodan_ip                        | 1.2     | not installed | 2020-07-01 | * | * |
  | recon/locations-locations/geocode                  | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/locations-locations/reverse_geocode          | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/locations-pushpins/flickr                    | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/locations-pushpins/shodan                    | 1.1     | not installed | 2020-07-07 | * | * |
  | recon/locations-pushpins/twitter                   | 1.1     | not installed | 2019-10-17 |   | * |
  | recon/locations-pushpins/youtube                   | 1.2     | not installed | 2020-09-02 |   | * |
  | recon/netblocks-companies/censys_netblock_company  | 2.0     | not installed | 2021-05-11 | * | * |
  | recon/netblocks-companies/whois_orgs               | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/netblocks-hosts/censys_netblock              | 2.0     | not installed | 2021-05-10 | * | * |
  | recon/netblocks-hosts/reverse_resolve              | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/netblocks-hosts/shodan_net                   | 1.2     | not installed | 2020-07-21 | * | * |
  | recon/netblocks-hosts/virustotal                   | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/netblocks-ports/census_2012                  | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/netblocks-ports/censysio                     | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/ports-hosts/migrate_ports                    | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/ports-hosts/ssl_scan                         | 1.0     | not installed | 2020-04-13 |   |   |
  | recon/profiles-contacts/bing_linkedin_contacts     | 1.1     | not installed | 2019-10-08 |   | * |
  | recon/profiles-contacts/dev_diver                  | 1.1     | not installed | 2020-05-15 |   |   |
  | recon/profiles-contacts/github_users               | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/profiles-profiles/namechk                    | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/profiles-profiles/profiler                   | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/profiles-profiles/twitter_mentioned          | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/profiles-profiles/twitter_mentions           | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/profiles-repositories/github_repos           | 1.1     | not installed | 2020-05-15 |   | * |
  | recon/repositories-profiles/github_commits         | 1.0     | not installed | 2019-06-24 |   | * |
  | recon/repositories-vulnerabilities/gists_search    | 1.0     | not installed | 2019-06-24 |   |   |
  | recon/repositories-vulnerabilities/github_dorks    | 1.0     | not installed | 2019-06-24 |   | * |
  | reporting/csv                                      | 1.0     | not installed | 2019-06-24 |   |   |
  | reporting/html                                     | 1.0     | not installed | 2019-06-24 |   |   |
  | reporting/json                                     | 1.0     | not installed | 2019-06-24 |   |   |
  | reporting/list                                     | 1.0     | not installed | 2019-06-24 |   |   |
  | reporting/proxifier                                | 1.0     | not installed | 2019-06-24 |   |   |
  | reporting/pushpin                                  | 1.0     | not installed | 2019-06-24 |   | * |
  | reporting/xlsx                                     | 1.0     | not installed | 2019-06-24 |   |   |
  | reporting/xml                                      | 1.1     | not installed | 2019-06-24 |   |   |
  +---------------------------------------------------------------------------------------------------+

  D = Has dependencies. See info for details.
  K = Requires keys. See info for details.

[recon-ng][first] > 
```

modules load <module>
	
info - shows options
	
options set source <ip>
	
wordlists, 
	
run