The idea is security must be usable in order to prevent many attacks. In **Phishing** we are tricked into believing a message is form someone that isn't. Clicking on links could cause damage. *Human Computer Interaction* is a filed that deals with this interaction with machines.

### Usable Phishing
In usable fishing we attempt to compress very complicated encryption algorithms down to usable interfaces like a **lock icon**. Things that makes this field hard are:

1. Users are unmotivated - so security has to be simple and easy
2. Complex configuration makes sense to scientists but not to end users
3. Good feedback is hard to give
4. **Barn door** once security is lost it cannot be recovered (so we need to have complete security)

### Phishing
Adversaries attempt to get information form an end user that is confidential (passwords etc). Only 48% for fraudulent emails are detected.  Often it can be hard to distinguish phishing attacks. Many legitimate emails can be mistaken.

### Phishing Ecosystem
Here we start with a *User* and a *Phisher*. The phisher must first send an email to *Email Server* these check the email against a known set of local rules and list of known sites. If the email makes it past this the end user can either fall for, trash it or report it. If it gets reported it can help update rules for detecting emails.
Sites can also get reported to be potential.

![[Pasted image 20230301180411.png]]

This makes use of the Swiss' cheese model where we can block a pert of bad emails each time.

### Solutions
Automatically blocking attacks can be done with ML and rules (stops around 90%). We can train users. We can Support users. We can also use **authentication** to block emails.

### Authentication
This is how an entity proves it is some entity. If this worked perfectly phishing would be impossible. This doesn't have to be identity it can also just prove some fact about us like age, purchase etc.

The problem is when logging in we should authenticate the website is correct before we try to log into it. Instead we just use the website but the website doesn't use this. There is a lack of **backward authentication**.

### Phishing History
This is a **wicked solution** but there is no human solution.

**AOHell** (America Online) - This was an early internet schemes. User made an AOL bomb attack that could cuase trouble. Users got banned for using this and then decided to user others attacks. AOL used a passive indicator to stop users pretending to be AOL. This became more of a problem when it moved off AOL and to email.

**Email** - here there is much less security and so passive indicators couldn't be used. Many websites made their own passive indicators that show you when you are on the correct sight. Generally sights aren't judged by  these indicators and instead the websites.

**Active indicators** - here a browser block a page and you actively have to continue after given a warning.

![[Pasted image 20230301181519.png]]

These generally have a better effect. But with time users get past this as they get used to this and are curious to see what the page is.

![[Pasted image 20230301181632.png]]

Habituation is the case where the users click through and move through security features without thinking.

### Where to learn about security
Generally users are unmotivated and will not learn about security. Generally prompts are a major way users learn from. So dialogs can allow us to integrate learning into a message.

Marketing material is generally less trusted. High socioeconomic users get their phishing advice from work while other get info from friend and family.

Generally users would have to check details they don't understand and therefore we cannot 