## What Is This Tool?
This tool
## How Can You Get the Tool?

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cloudinary-devs/cloudinary-email-uploader)


### Setting Up the Prerequisites 
Set up the following:

### Wiring the Tool



### Deploying the Code
Depending on your goal, do either of the following:


```bash
git clone https://github.com/cloudinary-devs/
 cd cloudinary-email-uploader
 pip install -r requirements.txt
 python cld-email-uploader.py
```


Unless you’ve configured the environmental variable `PORT`, the local development environment runs on port 80 by default. Also, you can change the name of the upload preset on the development environment by setting the `UP_PRESET` variable. To facilitate development, both `PORT` and `UP_PRESET` contain default values, as follows:


``` bash
export PORT=80
export UP_PRESET=’email_uploader’
```
