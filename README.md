## What Is This Tool?
This tool was created to fulfill the need for bulk metadata updates on a Cloudinary DAM account.
This tool will allow you to maintain 2 main approaches.

### The update by CSV
Simply upload a CSV file to the root of your account when the structure is rather simple.
The first line of the CSV file (the Headers) will contain the following structure:
```
	FILENAME,external id of first field, external id of second field, etc..
	foo.jpg,value1,value2
	bar.bmp.value1,value2
```
The file will be processed line by line and for each line you will be able to see the actions taken in the attached Coralogix instance.

### The update by file structure (Upon upload)
This method will update the metadata field with regard to the assets "folder" location.
So if you upload an asset to `/Cloudinary root/Folder1/Folder2/Asset_name`
And your "tree logic" value is `Field1/Field2`

The result will be as such: `Field1=Folder1, Field2=Folder2`

The update of upload will happen only on upload, and not on rename action.

## Installation
The fastest way is to click Here -->:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cloudinary-devs/cloudinary-meta-pop)

### Fill in the variables:
`CLOUDINARY_URL` - You can get this value from your Cloudinary console dashboard. It's the way we authenticate the app with Cloudinary

`TREE_LOGIC` - Here you have 2 options, you can set it up now or later.
If you have no plans of using the "Metadata by folder structure" there is no need to set it up.

### Configure it on your Cloudinary account:
To configure the tool you will need to create an upload preset with a notification URL.
You can learn how to do it here: https://cloudinary.com/documentation/upload_presets

To use the update by CSV method point the notification URL to:
	{your app url}/manifest

To use the Update by folder method point the notification URL to:
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
## Disclaimer:
This software/code provided under Cloudinary Labs is an unsupported pre-production prototype undergoing further development and provided on an “AS IS” basis without warranty of any kind, express or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. Furthermore, Cloudinary is not under any obligation to provide a commercial version of the software

Your use of the Software/code is at your sole risk and Cloudinary will not be liable for any direct, indirect, incidental, special, exemplary, consequential or similar damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of the Software, even if advised of the possibility of such damage.

You should refrain from uploading any confidential or personally identifiable information to the Software. All rights to and in the Software are and will remain at all times, owned by, or licensed to Cloudinary.
