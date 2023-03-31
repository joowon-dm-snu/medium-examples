ProblemSolverFunctionDefinition = """Create a plan as a list, step by step, to answer the request or goal given.
To create a plan, follow these steps:
1. Identify the request or goal to be achieved.
2. Break down the request into smaller tasks and steps.
3. If the goal has a ""use"" parameter, use those functions with the exact name given.
4. Use experience and logic to determine the steps and tasks needed.
5. Provide a detailed decision-making process for each step.
6. Avoid generic instructions and add as many details as possible.
7. Present the solution using precise XML syntax with ""solution"" and ""step"" tags.
8. Ensure that all tags are closed.
9. Append an ""END"" comment at the end of the plan.
10. If you don't know how to fulfill a request, use the ""noSolution"" tag.
11. Use a computer, browser, apps, and external services to fulfill the goal.
12. Ensure that all goals are fulfilled from a computer.

Here some good examples:

<goal>
what time is it?
</goal>
<variables />
<solution>
  <step>Get current location</step>
  <step>Find the time zone for the location in the variables</step>
  <step>Get the current time for the time zone in the variables</step>
</plan><!-- END -->

<goal use=""time.timezone"">
what time is it?
</goal>
<variables />
<solution>
  <callFunction name=""time.timezone"" />
  <step>Get the current time for time zone in the variables</step>
</solution><!-- END -->

<goal use=""time.timezone,time.currentTime"">
what time is it?
</goal>
<variables />
<solution>
  <callFunction name=""time.timezone"" />
  <callFunction name=""time.currentTime"" />
  <step>Get the current time from the variables</step>
</solution><!-- END -->

<goal use=""timeSkill.GetTimezone,timeSkill.currentTime,timeSkill.currentDate"">
how long till Christmas?
</goal>
<variables />
<solution>
  <callFunction name=""timeSKill.GetTimezone"" />
  <callFunction name=""timeSKill.currentTime"" />
  <callFunction name=""timeSKill.currentDate"" />
  <step>Get the current date from the variables</step>
  <step>Calculate days from ""current date"" to ""December 25""</step>
</solution><!-- END -->

<goal>
Get user's location
</goal>
<variables />
<solution>
  <step>Search for the user location in variables</step>
  <step>If the user location is unknown ask the user: What is your location?</step>
</solution><!-- END -->

<goal use=""geo.location"">
Get user's location
</goal>
<variables />
<solution>
  <callFunction name=""geo.location"" />
  <step>Get the location from the variables</step>
  <step>If the user location is unknown ask the user to teach you how to find the value</step>
</solution><!-- END -->

<goal use=""GeoSkill.UseMyLocation"">
Find my time zone
</goal>
<variables />
<solution>
  <callFunction name=""GeoSkill.UseMyLocation"" />
  <step>Get the location from the variables</step>
  <step>If the user location is unknown ask the user: What is your location?</step>
  <step>Find the timezone for given location</step>
  <step>If the user timezone is unknown ask the user to teach you how to find the value</step>
</solution><!-- END -->

<goal>
summarize last week emails
</goal>
<variables />
<solution>
  <step>Find the current time and date</step>
  <step>Get all emails from given time to time minus 7 days</step>
  <step>Summarize the email in variables</step>
</solution><!-- END -->

<goal>
Get the current date and time
</goal>
<variables />
<solution>
  <step>Find the current date and time</step>
  <step>Get date and time from the variables</step>
</solution><!-- END -->

<goal use=""time.currentDate,time.currentTime,.GETTIMEZONE,me.myFirstName"">
Get the current date and time
</goal>
<variables />
<solution>
  <callFunction name=""time.currentDate"" />
  <callFunction name=""time.currentTime"" />
  <callFunction name="".GETTIMEZONE"" />
  <callFunction name=""me.myFirstName"" />
  <step>Get date and time from the variables</step>
</solution><!-- END -->

<goal use=""time.currentDate,time.GetCurrentTime,time.timezone,me.UseMyFirstName"">
how long until my wife's birthday?
</goal>
<variables />
<solution>
  <callFunction name=""time.currentDate"" />
  <callFunction name=""time.GetCurrentTime"" />
  <callFunction name=""time.timezone"" />
  <callFunction name=""me.UseMyFirstName"" />
  <step>Search for wife's birthday in memory</step>
  <step>If the previous step is empty ask the user: when is your wife's birthday?</step>
</solution><!-- END -->

<goal>
Search for wife's birthday in memory
</goal>
<variables />
<solution>
  <step>Find name of wife in variables</step>
  <step>If the wife name is unknown ask the user</step>
  <step>Search for wife's birthday in Facebook using the name in memory</step>
  <step>Search for wife's birthday in Teams conversations filtering messages by name and using the name in memory</step>
  <step>Search for wife's birthday in Emails filtering messages by name and using the name in memory</step>
  <step>If the birthday cannot be found tell the user, ask the user to teach you how to find the value</step>
</solution><!-- END -->

<goal>
Search for gift ideas
</goal>
<variables />
<solution>
  <step>Find topics of interest from personal conversations</step>
  <step>Find topics of interest from personal emails</step>
  <step>Search Amazon for gifts including topics in the variables</step>
</solution><!-- END -->

<goal>
Count from 1 to 5
</goal>
<variables />
<solution>
  <step>Create a counter variable in memory with value 1</step>
  <step>Show the value of the counter variable</step>
  <step>If the counter variable is 5 stop</step>
  <step>Increment the counter variable</step>
</solution><!-- END -->

<goal>
foo bar
</goal>
<variables />
<solution>
  <noSolution>Sorry I don't know how to help with that</noSolution>
</solution><!-- END -->

The following is an incorrect example, because the solution uses a skill not listed in the 'use' attribute.

<goal use="">
do something
</goal>
<variables />
<solution>
  <callFunction name=""time.timezone"" />
</solution><!-- END -->

End of examples.

<manual>
{{$SKILLS_MANUAL}}
</manual>

<goal use=""{{$SKILLS}}"">
{{$INPUT}}
</goal>
"""

SolveNextStepFunctionDefinition = """{{$INPUT}}

Update the plan above:
* If there are steps in the solution, then:
    ** use the variables to execute the first step
    ** if the variables contains a result, replace it with the result of the first step, otherwise store the result in the variables
    ** Remove the first step.
* Keep the XML syntax correct, with a new line after the goal.
* Emit only XML.
* If the list of steps is empty, answer the goal using information in the variables, putting the solution inside the solution tag.
* Append <!-- END --> at the end.
END OF INSTRUCTIONS.

Possible updated plan:
"""
