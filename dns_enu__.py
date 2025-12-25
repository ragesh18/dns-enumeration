import dns.resolver
import dns.zone
import dns.query

target_domain = input("Enter the target domain: ")
records_type = input("Enter the DNS record type (A, MX, CNAME, TXT, SOA, CAA): ").upper()


resolver = dns.resolver.Resolver()
for record_type in records_type.split():
    try:
        answer = resolver.resolve(target_domain, record_type.strip())
        print(f"\n{record_type} Records for {target_domain}:")
        for data in answer:
            print(f" - {data}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        print(f" - No {record_type} record found or domain does not exist.")

# AXFR Attempt
axfr_choice = input("\nDo you want to attempt a zone transfer? [YES/NO]: ").upper()
if axfr_choice == 'YES':
    try:
        ns_answers = resolver.resolve(target_domain, 'NS')
        for ns in ns_answers:
            ns_name = str(ns.target)
            try:
               
                ip_answer = resolver.resolve(ns_name, 'A')
                ip = str(ip_answer[0])
                print(f"[*] Trying AXFR on {ns_name} ({ip})")
                zone = dns.zone.from_xfr(dns.query.xfr(ip, target_domain))
                print(f"\n Zone Transfer Successful from {ns_name}!")
                for name, node in zone.nodes.items():
                    rdatasets = node.rdatasets
                    for rdataset in rdatasets:
                        for data in rdataset:
                            print(f"{name} {rdataset.ttl} {rdataset.rdtype} {data}")
                break  
            except Exception as e:
                print(f"❌ AXFR failed for {ns_name}: {e}")
    except Exception as e:
        print(f"Could not retrieve NS records: {e}")   
