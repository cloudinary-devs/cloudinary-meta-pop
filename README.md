## What Is This Tool?
This tool was created to fullfill the need for bulk metadata updates on a cloudinary DAM account.
This tool will allow you to maintain 2 main approches

The update by CSV
The update by file structure (Upon upload)

## How Can You Get the Tool?

### Installation
The fastest way is to click the button below:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cloudinary-devs/cloudinary-meta-pop)

Fill in the variables:

### Configure it on you cloudianry account:
To Configure the tool you will need the following

### Wiring the Tool



### Develop and Evolve the code!
Depending on your goal, do either of the following:


```bash
git clone https://github.com/cloudinary-devs/cloudinary-meta-pop
 cd cloudinary-meta-pop
 pip install -r requirements.txt
 python meta_pop_app.py
```


Unless you’ve configured the environmental variable `PORT`, the local development environment runs on port 80 by default. Also, you can change the name of the upload preset on the development environment by setting the `UP_PRESET` variable. To facilitate development, both `PORT` and `UP_PRESET` contain default values, as follows:


``` bash
export PORT=80
export UP_PRESET=’email_uploader’
```
