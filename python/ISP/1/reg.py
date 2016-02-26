import re

email_validator = re.compile(r"""[a-z0-9!#$%&'*+-/=?^_`{|}~]*[.]*[a-z0-9!#$%&'*+-/=?^_`{|}~]+
                             @[a-z0-9]+(.[a-z0-9]{2,63})+$""", re.X) #massive common sense violation

number_validator = re.compile(r"([+-]?[1-9]+[0-9]*)?[.]?[0-9]*([Ee][+-]?[0-9]+)?$")

url_groups = re.compile("""(?P<scheme>[a-z]+[a-z0-9+\-\.]*:[/]+)?
                           (?P<authentication>[a-z0-9]:[a-z0-9])?
                           (?P<host>[a-z0-9]+(?P<subdomains>\.[a-z0-9]{2,63})+)*
                           (?P<path>/+[a-z0-9/_/.]*)?
                           (?P<query>\?[a-z0-9=&\-_]+)?
                           (?P<fragment>\#[a-z0-9=&_\-]+)?$""", re.X)

emails = ["sim.ple@email.com", "#!$%&'*+-/=?^_`{}|~@valid.example.org", 
          "vasyan2006@narod.rumail.ru", "not valid@email.com", 
          "to_many_domain_levels@m.egahost.coolmail.abacaba"]

floats = ["1.", ".2", "3.14", "5e6", "5e-6", "5E+6", "7.e8", "9.0E-10", ".11e12"]

urls = ["https://regex101.com/#python",
        "http://vk.com/im?sel=10787191asd39s4#9",
        "pokapoka.com",
        "file:///home/pokapoka/pictures/smile.jpg"] 

groups = ["scheme", "authentication", "host", 
          "path", "query", "fragment"]

print "emails:"
for x in emails:
    result = email_validator.match(x)
    print result

print "floats:"
for x in floats:
    result = number_validator.match(x)
    print result

print "url_groups:"
for url in urls:
    print "\n" + url + "\n"
    for group in groups:
        result = url_groups.match(url)
        try:
            print group + ": " + result.group(group)
        except TypeError: 
            print group + ": none"
        except AttributeError:
            print group + ": none"
