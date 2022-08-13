
## About mailcheck

- What is mailMeta?
Mailcheck is an email header analyzer tool that detects whether your emailis spoofed or not. This help in detection of phishing and spammed mails.

 - What are the information revealed by the mailcheck?
Mailcheck parses the following headers:
   
   * Message-ID 
   * SPF-Record
   * DKIM-Record
   * DMARC-Record
   * Spoofed Email detection based on the above headers
   * IP-Address of the sender
   * Service Provider used for sending the email
   * Content-Type
   * Data and Time 
   * Subject
 

## Installation

You have two methods to use metacheck. Either you can download the github repo and run the mailcheck.py file from the command line. Make sure you have all requirements installed in this case like python3. You may also run the standalone binaries. This is for those who have very little technical knowledge.

<br>
1. Clone the repository

  ```(bash)
    git clone https://github.com/FeNriR0077/Email-security-mailcheck-.git
  ```

2.  Running from the mailcheck.py file

  ```(bash)
    cd Email-security-mailcheck-
    pip install -r requirements.txt
    python3 mailcheck.py
  ```

## Usage
<br>

Either you are on windows or linux first download the original metadata of the email using the **show original** / **view raw** / **download original** option. 

Then we pass the `eml` file to the executable.
<br>



### Linux

1. Use `mailcheck.py` from the cloned repo. (Python is required)

```
python3 mailcheck.py -f message.eml
```


<br>


### Windows


1. Running from the repository clonned (Python Required)

```
python3 mailcheck.py -f message.eml
```



