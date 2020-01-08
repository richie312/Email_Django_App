

# Email_Django_App
An Application which takes the recruiter's email and sends the profile of the candidate to the recruiter. The application also has the options to change the sender's email (this is available and only limited to GMAIL).

## Steps to create the application

1. Setup the AWS RDS Database with Django. **Done** (&#x1F4D7;)

2. Create the model and create fields in the database using django ORM. **Done**(&#x1F4D7;)
    - connect with the existing table and manipulate the data: **Done**(&#x1F4D7;)

3. Make the Frontend webform and integrate it with Django backend: **Done**(&#x1F4D7;)
	- Added the datefield which by default populates the current time: **Done**(&#x1F4D7;)

4. Make the provision to attach the resume:**In Progress**(&#x1F4D9;)
	- upload button (accepts only pdf/html/docx): **In Progress**(&#x1F4D9;)
	- connect it with email_portal.views.Sendmail: **In Progress**(&#x1F4D9;)

5. Make the provision to upload the image and add with the template layout.

	- pull in the login decorator and save the profile information by userwise.
	- Make a separate division to edit the profile template and route to different page 

6. Provision to create the preview.

7. Finally send the mail and Test it with different user.

8. Render the details of the total number of applications made by individual users.
