
## About mailcheck

- What is mailMeta?
mailcheck is an email header analyzer tool that detects whether your emailis spoofed or not. This help in detection of phishing and spammed mails.

 - What are the information revealed by the mailcheck?
mailcheck parses the following headers:
   
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
    cd mailcheck
    python3 mailcheck.py
  ```

## Usage
<br>

Either you are on windows or linux first download the original metadata of the email using the **show original** / **view raw** / **download original** option. 

Then we pass the `eml` file to the executable.
<br>

This is a demo of how to download the mail. You should find something similar.

![mail-download](images/mail-download.gif)

### Linux

1. Use `meta.py` from the cloned repo. (Python is required)

```
python3 meta.py -f message.eml
```

![metapy-linux](images/linux-metapy.png)

or

2. Downloading the `meta` executable for linux and giving it executable permissions. Then supplying the eml file to the pre-compiled binary. (No dependencies)

```
wget https://github.com/gr33nm0nk2802/mailMeta/releases/download/1.0.0/meta
chmod +x meta
meta -f message.eml
```
<br>

![meta-linux](images/linux-meta.png)

### Windows

1. Executing the precompiled binaries downloaded from the releases page. (No dependencies needed)

```
meta.exe -f .\message.eml
```

![win-meta-exe](images/win-meta-exe.png)

<br>

or

2. Running from the repository clonned (Python Required)

```
python3 meta.py -f message.eml
```

![win-meta-py](images/win-meta-py.png)

## Demo

This is a sample demonstration explaining all the procedures. First it has the steps for running on linux then it has the steps needed for running on windows just in case you are struck.

![demo-gif](images/demo.gif)

## Contributions

Contributions and pull requests are highly encouraged for this project.

## Inspiration

This project has been made as a part of the GPCSSIP 2021 under the mentorship of [Rakshit Tandon](https://www.linkedin.com/in/rakshittandon/) sir to help aid in the detection of spoofed email and their tracking. 

## FAQ

What is the accuracy of this tool?
This tool simply reads the raw data of the mail downloaded.

## License

This project is licensed under the [MIT license](https://github.com/gr33nm0nk2802/mailMeta/blob/main/LICENSE).
