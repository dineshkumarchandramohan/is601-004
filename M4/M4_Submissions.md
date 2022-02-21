<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Dinesh Kumar Chandramohan(dc648)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2022 8:19:34 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/dc648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you&#39;re working in an up to date branch</p>
<ul>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b M4-Simple-Calc</code></li>
</ul>
<p>This will likely be started in class.</p>
<p>Steps:</p>
<ol>
<li>Create a new Folder called M4</li>
<li>Create a new file called MyCalc.py inside this folder</li>
<li>Create a MyCalc Class</li>
<li>Define basic addition / subtraction / multiplication / division functions<ol>
<li>These functions should update an internal variable as a running total/value called <code>ans</code></li>
<li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero)</li>
<li>Since you&#39;ll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li>
</ol>
</li>
<li>Define a &quot;main&quot; logic to run when the program runs</li>
<li>This logic should ask for user input<ol>
<li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol>
<li>This will do an immediate calculation, print it, and store the answer in the <code>ans</code> variable</li>
</ol>
</li>
<li>Alternatively, the input can be <code>ans</code>, any valid math operator, any valid number (i.e., <code>ans</code> * 2)<ol>
<li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the <code>ans</code> variable</li>
</ol>
</li>
</ol>
</li>
<li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass<ol>
<li>Test number-add-number</li>
<li>Test ans-add-number</li>
<li>Test number-sub-number</li>
<li>Test ans-sum-number</li>
<li>Test number-mult-number</li>
<li>Test ans-mult-number</li>
<li>Test number-div-number</li>
<li>Test ans-div-number</li>
</ol>
</li>
<li>Create a new file called m4_submission.md inside the M4 folder</li>
<li>Fill out the below deliverables</li>
<li>Generate the markdown and paste it into the m4_submission.md</li>
<li><code>git add .</code></li>
<li><code>git commit -m &quot;adding m4 hw&quot;</code></li>
<li><code>git push origin M4-Simple-Calc</code></li>
<li>Create a pull request M4-Simple-Calc to dev</li>
<li>Create a pull request dev to prod (after the previous one is merged)</li>
<li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li>
<li>Submit this link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154878406-337357e5-bcd3-4da0-a9a0-49601aa0d633.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add method screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154878746-1ec5483c-1751-4504-8163-a66ec00cdc5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub method screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154878851-59669756-fefd-4c8c-9e90-0c32125c9d16.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mult method screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154878909-e4c4d32d-5622-4490-a759-d9d8822576c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Div method screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of passing number-add-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154879172-a1e632d0-a0d2-4044-8d87-f0b00a87a1cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot for Testcase 1 : Adding 2 numbers and the testcase<br>result is PASS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of passing ans-add-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154879433-3211be55-811b-4370-9572-cae70fec9bf4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot for Testcase 2 : Adding 2 numbers(ans + any number)<br>by taking the cached value of ans from previous addition and the testcase<br>result is PASS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of passing number-sub-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154879673-46bc4b1b-4c5b-40ce-837f-6835c89a1c37.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot for Testcase 3 : Subtracting 2 numbers and the testcase<br>result is PASS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of passing ans-sub-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154879873-82d9d4a4-a54b-4826-8619-5ffb12d359eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot for Testcase 4 : Subtracting 2 numbers (ans - anynumber)<br>by taking the cached value of ans from previous addition and the testcase<br>result is PASS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot of passing number-mult-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154879940-763a742c-0599-469a-80a0-a55994ae1351.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot for Testcase 5 : Multiplying 2 numbers and the testcase<br>result is PASS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot of passing ans-multi-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154880122-090ac8fd-c5d9-4735-8d7b-fa2134625550.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot for Testcase 6 : Multiplying 2 numbers (ans * anynumber)<br>by taking the cached value of ans from previous addition and the testcase<br>result is PASS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshot of passing number-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154880242-eaa061ef-d3f4-49e0-a44c-5176b42f0ae9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot for Testcase 7 : Dividing 2 numbers and the testcase<br>result is PASS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshot of passing ans-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/98123760/154880346-ad220ba8-16cc-4412-9771-2e84ce02ad3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding the screenshot for Testcase 8 : Dividing 2 numbers (ans * anynumber)<br>by taking the cached value of ans from previous addition and the testcase<br>result is PASS<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>This assignment helped me to understand python basic codes and helped me to<br>learn how to use functions for mathematicals operations using pycharm and also helped<br>me to understand the testcases running using pytest.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>We have to download pytest using python packages and use the same for<br>running testcases and get the result.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/dineshkumarchandramohan/is601-004/pull/6">https://github.com/dineshkumarchandramohan/is601-004/pull/6</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/dc648" target="_blank">Grading</a></td></tr></table>
