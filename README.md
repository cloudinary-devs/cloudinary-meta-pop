## What Is This Tool?
This tool was created to fullfill the need for bulk metadata updates on a cloudinary DAM account.
This tool will allow you to maintain 2 main approches

### The update by CSV
Simply upload a csv file to the root of your account when the structure is rather simple.
the first line of the csv file (the Headers) will contain the folloeing structure:
	FILENAME,external id of first field, external id of second field, etc..
	foo.jpg,value1,value2
	bar.bmp.value1,value2

the file will be processed line by line and for each line you will be able to see the actions taken in the attached Coralogix instance.

### The update by file structure (Upon upload)
This method will update the metadata field with regards to the assets "folder" location.
So if you upload an assets to /Cloudinary root/Folder1/Folder2/Asset_name
And your "tree logic" value is the following "Field1/Field2"

The result will be as such: Field1=Folder1, Field2=Folder2

The update of upload will happen only on upload, and not on rename action.

## Installation
The fastest way is to click Here -->:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cloudinary-devs/cloudinary-meta-pop)

### Fill in the variables:
CLOUDINARY_URL - You can get this value from your cloudinary console dashboard. It's the way we authenticate the app with Cloudinary

TREE_LOGIC - Here you have 2 options, You can set it up now or later.
If you have no plans of using the "Metadata by folder structure" there is no need to set it up"

### Configure it on your cloudinary account:
To Configure the tool you will need to create an upload preset with a notification url.
you can learn how to do it here: https://cloudinary.com/documentation/upload_presets

To use the update by csv method point the notification url to:
	{your app url}/manifest

To use the Update by folder method point the notification url to:
	{your app url}/foldertree


## Develop and Evolve the code!
Run the following command to get a local copy running.
Please tell us about any bugs you find or open a PR for fixing them and adding features.

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
