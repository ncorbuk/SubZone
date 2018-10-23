![alt text](https://github.com/ncorbuk/SubZone/blob/master/logo_.png)

# SubZone
**```HTTP(S)-Subdomains,Dns records, & More!```**
* All subdomains  ~ (all registered subdomains from primary domain/host)
* All **active** subdomains  ~ (domains that are online and alive!)
* Dns records  ~ (all records that have leaked and are recoverable)
* Is non-intrusive... leave NO fingerprints, totaly fast and totaly anonymous.

This program **SubZone** will find all subdomains for a domain/host you specify, Dns records of all the 
dns server's for that domain/host, included in the records can be found -

* Owner/sys-admin email.
* Owner contact info.
* Server contact info.
* Ip addresses.
* Port numbers
* Telephone numbers.
* Location of server.
* Other servers.
* Description of any software being used... like tcp/udp or sic_tcp.(VoIp software).
* & more!.

The possibiltes are endless, depending on how well the domain/host has configured there 
dns server(s) and what information they are leaking.

## Getting Started

To get *started* simply *Fork the repository*, open up console (*cmd/powershell/terminal*) cd into repository folder with 
the *SubZone v_2.0.py* (Or the latest up to date version). Then type "**python subzone_v2.0.py -h**" - This will give you the *options/arguments* you need to specify to run file. 

**Key points for arguments/options**...
* Arguments are **-d** *(For domain)* & **-o** *(For output file)*
* Use http(s) in your domain.  ~  *Ex. -d https://example.com (Not https://www.example.com)*
* Specifying output file is *NOT* optional.  ~  *Ex. -o example.txt* 
* Specifying domain name is *NOT* optional.  ~  *Ex. -d https://example.com
* You may need to change the **shebang** at the top of the source code file. Ex. *#!d:/python 3.6.5/python.exe* (use own path) or for **Linux** use *#!/usr/bin/env python* (Example), **Windows** use *#!disk(c/d/e):/path to python folder/python.exe*

**Example Usage:**
```
-d (domain) is True(needed)  -o (output) is True (needed) - *Was optional but seems that there is a bug and is making the color disapeer on console, was working. uhm :/*

- python subzone_v2.0.py -d (domain) -o (output)
- python subzone_v2.0.py -d https://facebook.com -o facebook.txt
- python subzone_v2.0.py -d https://zonetransfer.me -o zonetransfer.txt
```

Above is the command layout, and some examples. If you wish to see how good! my program is.. I highly reccomend trying the above
TWO arguments with SubZone to see what Subdomains/Dns records you will receive for facebook.com (very many subsdomains) and
zonetransfer.me(the kinda of dns records you could get)

- *NOTE*: You wont always get Subdomains and Dns records. Some domains dont have any subdomains and/or some dns servers are configured
correctly, like in facebook's case its not not leaking dns records.. but got the subdomains.

- *100%*: You will get everything that can be got from the domain/host!

### Prerequisites

**Python** - This is built on Python 3.6, you will need at least Python 3.5+ (might work with 3+ i havent tested it - should not be hard to make work tho if dosent!) to use this software. - [https://www.python.org/](https://www.python.org/)

**Libraries** - You will need/use these libraries to use this software:

*From the standerd libraries.*
* Time : n/a
* Socket : n/a
* Subprocess : n/a
* os : n/a

*Not from the standerd libraries.*
* Colorama : >=0.3.9
* Requests : >=2.18.4
* Json : >=2.0.9
* Argparse : >=1.1
* Urlib3 : >=1.22

## Deployment

Just double tap and go ;) joke.

Just use console and use commands in the **Getting Started** section at the top, or you can quickly use this command to view help in terminal.
**python subzone_v2.0.py -h**  ~ (Which will give you options/arguments that you will need to specify in order for it to work.)

## Usage examples with pictures

### Facebook (https://facebook.com)
**python subzone_v2.0.py -d https://facebook.com -o facebook.txt**

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/facebook_01.png)

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/facebook_02.png)

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/facebook_3.png)

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/facebook_04.png)

### Zonetransfer (https://zonetransfer.me)
**python subzone_v2.0.py -d https://zonetransfer.me -o zonetransfer.txt**

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/zonetransfer_1.png)

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/zonetransfer_2.png)

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/zonetransfer_3.png)

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/zonetransfer_4.png)

### Output documents (-o filename.txt)

![alt text](https://github.com/ncorbuk/SubZone/blob/master/Usage_pictures/output_docs01.png)

* **Output content** - *[View file(s) content](https://github.com/ncorbuk/SubZone/tree/master/Example%20of%20output%20files)*

## Built With

* **Python 3.6.5** - [https://www.python.org/](https://www.python.org/)

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests.

## Versioning

Versioning will be in terms off v1/v2.2/v3 etc. Highest number in version/file is the most up too date version of software.

## Authors

* **Nathan Corbin** - *Github*: [ncorbuk](https://github.com/ncorbuk) - *Twitter*: [@ncorbuk](https://twitter.com/ncorbuk)

## Acknowledgments

* I took inspiration from [UnaPibaGeek](https://github.com/UnaPibaGeek) and her *ctfr* code.(check her out, great stuff)
* I took inspiration from [DigiNinja - DigiNinja](https://zonetransfer.me) for setting up *zonetransfer.me* wich is purposely *vulnerable* and not setup correctly to show how a *dns server* can *betray* you and *leak* information if you dont know what your doing.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

