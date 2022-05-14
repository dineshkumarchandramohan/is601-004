<table><tr><td> <em>Assignment: </em> Mini Project 2_Advanced Calculator</td></tr>
<tr><td> <em>Student: </em> Dinesh Kumar Chandramohan(dc648)</td></tr>
<tr><td> <em>Generated: </em> 4/30/2022 1:27:19 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/dc648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Prepare your workspace</p>
<ol>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b MP2-AdvCalc</code></li>
</ol>
<p>In this project, you&#39;ll decorate or extend one of the given MyCalc samples (do not edit MyCalc directly).
For every added calculation you&#39;ll need to provide a positive and negative test case.
<strong>Note:</strong> negative test cases will throw and capture exceptions to generate a positive test case
Negative test cases test for invalid input and/or invalid operations. These test cases will be via csv files as well 
(just like the changes to addition, subtraction, multiplication, division, square, and square root)</p>
<p>HINT 1: You can generate a normal distribution of random distribution of numbers with excel to use for your data:  Here (<a href="http://howtoexcel.org/statistics/normal-distribution/">http://howtoexcel.org/statistics/normal-distribution/</a>)</p>
<p>HINT 2: You can create another excel file that contains the answers to your calculations that you can use in your unit tests.</p>
<p><strong>Your program needs to additionally calculate the following:</strong></p>
<ol>
<li>Square</li>
<li>Square Root</li>
<li>Pick 5 from below<ul>
<li>Population Mean</li>
<li>Median</li>
<li>Mode</li>
<li>Population Standard Deviation</li>
<li>Variance of population proportion</li>
<li>Z-Score</li>
<li>Standardized score</li>
<li>Population Correlation Coefficient</li>
<li>Confidence Interval</li>
<li>Population Variance</li>
<li>P Value</li>
<li>Proportion</li>
<li>Sample Mean</li>
<li>Sample Standard Deviation</li>
<li>Variance of sample proportion</li>
</ul>
</li>
</ol>
<ul>
<li>You&#39;ll update your previous test cases to read from csv files for the input and output values.</li>
<li>Use the below csv files for your existing test cases of addition, subtraction, multiplication, and division.
As well as testing the new square and square root modifications.</li>
</ul>
<p><strong>Note</strong>: You may need to view the data via the &quot;Raw&quot; button on the gist.
<a href="https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe">https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe</a> </p>
<p>Once done do the following:</p>
<ol>
<li>Git add all changes (including the test case csv files)</li>
<li>Git commit with relevant messages</li>
<li>Git push origin MP2-AdvCalc</li>
<li>Create a Pull Request on Github to dev (keep it open)</li>
<li>Fill out the details here</li>
<li>Save and Generate the markdown (any changes require this step to be repeated)</li>
<li>Paste the content into a <code>mp2_submission.md</code> file</li>
<li>Git add/commit/push the submission file change</li>
<li>Complete the pull request merge</li>
<li>Create a new pull request from dev to prod and complete it</li>
<li>Navigate to prod branch&#39;s <code>mp2_submission.md</code> file and paste the direct link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Added Functionality: Square </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/165843727-3b178b3b-d673-4f13-b6bc-5b55f56bbbfc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for Square<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166089632-82575fe9-2bfe-4ba7-a6f3-796924c13b1f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passed test case<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Added Functionality: Square Root </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166090080-a31232b8-a6fb-484c-a0ac-7f116030f0d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for squareroot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166090017-ce77c00f-cd60-4455-829d-d59875362488.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passed test case<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Choice 1 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>I choose mean for my first subtask .Mean is same as the average<br>value of a data set<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166090137-5e9d2c10-65c3-49b4-a4a1-ea19b802f357.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mean function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166092577-719d6a58-0448-4921-88dd-bd82c38a8641.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166092577-719d6a58-0448-4921-88dd-bd82c38a8641.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>testcase<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Choice 2 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>subtask 2 : Median<br>Add up all the numbers and divide by the number<br>of number in dataset.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166091720-9a9a4ea2-d757-4a28-9062-b910eb3162e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Median function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166091654-048c97a7-9b50-44a5-bdfe-559ca597e0c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Positive<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166091654-048c97a7-9b50-44a5-bdfe-559ca597e0c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Negative<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Choice 3 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Subtask 3: Mode<br>Mode of a dataset is the number that occurs most frequently<br>in the set.to find the mode,put the numbers in order from least to<br>greatest and count how many times each number occurs.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166091789-4c982925-caf2-4c3f-948a-fe9c546928d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mode function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166091873-f9cce672-d58d-4793-ae33-9fd7cbe3c97a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passed test case<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166091873-f9cce672-d58d-4793-ae33-9fd7cbe3c97a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failed test case<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Choice 4 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>subtask 4: Standara deviation<br>find the mean and find the scores deviation from the<br>mean.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166091920-1d1cc453-f6d9-4fed-b9d4-846f5511ca2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>St dev function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166092003-a8690063-be39-4bf4-b8a5-f461fe3fc6f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passed testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166092003-a8690063-be39-4bf4-b8a5-f461fe3fc6f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failed testcase<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Choice 5 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>subtask 5 : variance<br>variance is a measure of dispersion of data points from<br>the mean.low variance indicates that data points are generally similar and do not<br>vary widely from the mean.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166092051-41c04a5f-999e-43d5-8e6d-c7f24308283a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Variance function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166092537-bd3e9983-31c7-48cb-bdf5-10140c58a026.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/166092537-bd3e9983-31c7-48cb-bdf5-10140c58a026.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>testcase<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Mention any difficulties and how you overcame them or what you learned during this mini project.</td></tr>
<tr><td> <em>Response:</em> <p>Faced issues during postive and negative test running<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Pull Request Link(s) for this project</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dineshkumarchandramohan/is601-004/pull/12">https://github.com/dineshkumarchandramohan/is601-004/pull/12</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/dc648" target="_blank">Grading</a></td></tr></table>
