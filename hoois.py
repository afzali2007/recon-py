import whois

print("please enter site name")
a = input("")
domain = a

w = whois.whois(domain)

print(w)

# Safely print each field if it exists
print("Domain registrar:", w.registrar if hasattr(w, 'registrar') else "N/A")
print("WHOIS server:", w.whois_server if hasattr(w, 'whois_server') else "N/A")
print("Domain creation date:", w.creation_date if hasattr(w, 'creation_date') else "N/A")
print("Domain expiration date:", w.expiration_date if hasattr(w, 'expiration_date') else "N/A")
print("Domain last updated:", w.last_updated if hasattr(w, 'last_updated') else "N/A")
print("Name servers:", w.name_servers if hasattr(w, 'name_servers') else "N/A")
print("Registrant name:", w.name if hasattr(w, 'name') else "N/A")
print("Registrant organization:", w.org if hasattr(w, 'org') else "N/A")
print("Registrant email:", w.email if hasattr(w, 'email') else "N/A")
print("Registrant phone:", w.phone if hasattr(w, 'phone') else "N/A")

