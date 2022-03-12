<table><tr><td> <em>Assignment: </em> Sample Flask App and Readings</td></tr>
<tr><td> <em>Student: </em> Dinesh Kumar Chandramohan(dc648)</td></tr>
<tr><td> <em>Generated: </em> 3/12/2022 6:38:20 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/sample-flask-app-and-readings/grade/dc648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Follow the slides from class.</li>
<li>Get the sample app deployed to Google Cloud Run</li>
<li>Once finished with the slides create a pull request from Flask-Sample to dev (don&#39;t close it yet)</li>
<li>Create an m6_submission.md file in the same directory as the sample flask app</li>
<li>Fill in the deliverables below</li>
<li>Generate the markdown and paste the content into the new md file</li>
<li>git add/commit/push</li>
<li>Complete the pull request</li>
<li>Create a pull request from dev to prod</li>
<li>Complete the merge</li>
<li>Locally checkout dev</li>
<li>git pull the latest dev changes</li>
<li>On GitHub navigate to the location of the m6_submission.md file</li>
<li>Grab that direct link and submit it to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Proof App has been deployed </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot the output of the app (including the url) showing it's running from Google</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/158037245-ad34cdb9-1b43-4e7a-a4b6-c51ef62e5a4a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output from the google cloud app including the URL<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a direct link to the app here</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-343902-fizvc27uja-uc.a.run.app/">https://is601-343902-fizvc27uja-uc.a.run.app/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a link to the pull request from Flask-Sample to Dev</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dineshkumarchandramohan/is601-004/pull/10">https://github.com/dineshkumarchandramohan/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Did you have any issues during setup and if so how did you resolve them?</td></tr>
<tr><td> <em>Response:</em> <p>I had issue in running the deploy.yml from github-actions</p><br><p>Mistake: I did not create<br>.github folder which holds the deploy.yml and sample-app folder which holds dockerfile,main.py and<br>requirements.txt file under the same root directory</p><br><p>Solution: I fixed it by creating both<br>the .github directory and sample-app directory in the same root directory<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Readings </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> What can you tell me about docker? Describe the various steps needed to get an app ran inside a docker container</td></tr>
<tr><td> <em>Response:</em> <p>1.Docker is an open platform for developing, shipping, and running applications<br>2.With Docker, you<br>can manage your infrastructure in the same ways you manage your applications<br>3.By taking<br>advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can<br>significantly reduce the delay between writing code and running it in production<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> What is Google Cloud Run? Why do you feel it was chosen for this class?</td></tr>
<tr><td> <em>Response:</em> <p>1.Cloud Run is a managed compute platform that enables you to run containers<br>that are invocable via requests or events<br>2.Google Cloud protects your data, applications, infrastructure,<br>and customers from fraudulent activity, spam, and abuse with the same infrastructure and<br>security services Google uses<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What is flask? List a few things you learned about it</td></tr>
<tr><td> <em>Response:</em> <p>1.Flask is a web framework.This means flask provides you with tools, libraries and<br>technologies that allow you to build a web application<br>2.Flask is part of the<br>categories of the micro-framework. Micro-framework are normally framework with little to no dependencies<br>to external libraries<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> What is the difference between a Dockerfile and a Github Action .yml file?</td></tr>
<tr><td> <em>Response:</em> <p>1.GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows<br>you to automate your build, test, and deployment pipeline<br>2.You can create workflows that<br>build and test every pull request to your repository, or deploy merged pull<br>requests to production<br>3.A Dockerfile is a text document that contains all the commands<br>a user could call on the command line to assemble an image<br>4.Using docker<br>build users can create an automated build that executes several command-line instructions in<br>succession.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/sample-flask-app-and-readings/grade/dc648" target="_blank">Grading</a></td></tr></table>/
