![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/logo_.png)

**GitHub - https://github.com/ncorbuk/SubZone**

**pypi - https://pypi.org/project/subzone/**

# Tutorial on SUBZONE: https://www.youtube.com/watch?v=5oNe7Rmtvoo&t=**
**For python tutorials: https://bit.ly/2U58Lt9**

## If you want to leave a tip
**If you would like to leave a tip you can do so below, thanks**
* PayPal: https://paypal.me/w3w3w3
* Bitcoin: 1EHmioBmujNAyVs5A6Uo1nfto9JZhGBDLd <-- pref this way :)

# SubZone
**```HTTP(S)-Subdomains,Dns records, & More!```**
* All **registered** subdomains!
* All **active** subdomains!
* All **Dns records**!
* Is **non-intrusive** - leave **NO fingerprints**, *totally fast and totally anonymous.*

**SubZone** - Gathers all registered subdomains for target domain, and then checks too see which ones are active subdomains, 
also will go through dns servers and do zonetransfer to see if any server have been miss configured and are leaking valuable
information.

* Owner/sys-admin email.
* Owner contact info.
* Server contact info.
* Ip addresses.
* Port numbers
* Telephone numbers.
* Location of server.
* Other servers
* Software.
* & more!.
*(Check out dns record pics for zonetransfer.me at bottom of page for example)*

This helps penetration testers and bug hunters collect and gather subdomains and information for the domain they are targeting. 

## Getting Started

Either Fork the latest repository or use pip to get latest version of subzone.
For easy install of python package and all dependencies use - *pip install subzone*

**Key points**
* Arguments are **-d** *(For domain)* & **-o** *(For output file)*
* Use http(s) in your domain.  ~  *Ex. -d https://example.com (Not https://www.example.com)*
* Specifying domain name is *NOT* optional.  ~  *Ex. -d https://example.com*
* Specifying output file *is* optional.  ~  *Ex. -o example.txt* 

**Can also be used as an import to your own script/program** 
*from subdomain import subzone*
then use **subzone.get(url)** eg. subzone.get('https://facebook.com')
Will print out a list of registered domains and active domains - in color - 

**Example Usage:**
```
-d (domain) is True(needed)  -o (output) is True (needed) - 
- python subzone_v2.0.py -d (domain) -o (output)
- python subzone_v2.0.py -d https://facebook.com -o facebook.txt
- python subzone_v2.0.py -d https://zonetransfer.me -o zonetransfer.txt
```

- *100%*: You will get everything that can be possibly got from the domain/host all whilst leaving **NO** fingerprints.

### Prerequisites

**Python** - This is built on Python 3.6, you will need at least Python 3.5+ (might work with 3+ i haven't tested it - should not be hard to make work tho if doesn't!) to use this software. - [https://www.python.org/](https://www.python.org/)

**Libraries** - You will need/use these libraries to use this software: 
*pip install subzone - will take care of this automatically.*

*From the standard libraries.*
* Time : n/a
* Socket : n/a
* Subprocess : n/a
* os : n/a
* Argparse : n/a
* Json : n/a

*Not from the standard libraries.*
* Colorama : >=0.3.9
* Requests : >=2.18.4
* Urlib3 : >=1.22

## Deployment

subzone is mainly to be used in console using the commands stated above, *OR* you can use **from subdomain import subzone** in your own script/program and use the following command **subzone.get('https://website.com')** to invoke the subdomain function in your own python code.

## Usage examples with pictures

### Facebook (https://facebook.com)
**python subzone.py -d https://facebook.com -o facebook.txt**

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/facebook_01.png)

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/facebook_02.png)

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/facebook_3.png)

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/facebook_04.png)

### Zonetransfer (https://zonetransfer.me)
**python subzone.py -d https://zonetransfer.me -o zonetransfer.txt**

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/zonetransfer_1.png)

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/zonetransfer_2.png)

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/zonetransfer_3.png)

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/zonetransfer_4.png)

### Output documents (-o filename.txt)

![alt text](https://raw.githubusercontent.com/ncorbuk/SubZone/master/Usage_pictures/output_docs01.png)

* **Output content** - *[View file(s) content](https://github.com/ncorbuk/SubZone/tree/master/Example%20of%20output%20files)*

## Built With

* **Python 3.6.5** - [https://www.python.org/](https://www.python.org/)

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests.

## Version

*Current version: 0.2.8*

*Current filename: subzone.py*

## Authors

* **Nathan Corbin** - *Github*: [ncorbuk](https://github.com/ncorbuk)

## Acknowledgments

* I took inspiration from [UnaPibaGeek](https://github.com/UnaPibaGeek) and her *ctfr* code.(check her out, great stuff)
* I took inspiration from [DigiNinja - DigiNinja](https://zonetransfer.me) for setting up *zonetransfer.me* which is purposely *vulnerable* and not setup correctly to show how a *dns server* can *betray* you and *leak* information if you don't know what your doing.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
