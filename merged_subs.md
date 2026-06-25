
### 001-AI Coding for Real Engineers p01 001 Where We're Going Before We Start

Welcome, welcome, welcome to the AI Coding for Real Engineers cohort. I'm super excited to be

running version 2 of this cohort. We've learned a lot since version 1 and I just can't wait to show

you the material. Since around December last year coding agents have taken a massive leap

forward in terms of capabilities and the stuff that you can do with them is just gone through

the roof in terms of power level, in terms of the stuff you can build and the speed at which

you can build it at. This has resulted in lots of folks getting very very excited and building

these huge great complex frameworks around AI coding agents to help you build stuff faster. You

guys may have used some of them like you know GSD or SpecKit or B-Mad or lots of things like

this. However I personally believe and have really always believed that you as a developer

should own your process and what we're going to be doing in this course is teaching you a

process that you can then iterate on and build on and make your own. And at the core of this

approach our reliance on real engineering skills, on heuristics and knowledge built up

from 30 years of development experience throughout the industry. Periodically throughout the course

I'm going to be waving actual books at you and we're going to be quoting from various sources

taking real development advice from people who've been doing it for a long time. And

we're going to end up with a seven phase process that looks something like this, that

takes in grilling or interviewing, research, prototyping, creating documents that get us where

we need to go, turning those documents into issues, implementing those issues and then

reviewing what we've done. One of the main key pillars here is making sure that our implementation

step runs completely AFK, in other words away from keyboard, allowing you to parallelise your

work with the agent. One of the things I see people say all the time is it's so annoying

that I just have to sit there and watch the agent do its work. Well with AFK you don't have

to and that's one of the core tenets of this whole system. But getting it working and

getting it producing good code regularly is difficult and requires real engineering skills.

In order to make these exercises stick this is not just going to be lectures, these are

interactive exercises. So we have an entire 20,000 line of code playground for you to

do your work in. We're going to be getting stuck in, we're going to be building real

features inside this application. However I wanted to leave this door open to you which is

you don't have to use this repo. You can take the exercises that I'm giving you like

building a feature or making a product requirements document and you can use it on

your own repo if you like. If you choose the cohorts project then of course you'll be able

to follow along exactly, you'll be able to get support, whereas if you choose your own repo then

you'll be able to actually apply what we're learning directly into your own code. However

because it's your code I won't be able to offer as good support as if you're using

the actual project. So I would say beginners or folks who are just starting out with this stuff

then use the cohort project, but if you're really confident or if you're just desperate

to get your own work and you don't mind a little less support then use your own repo.

The cohort project itself is written in TypeScript and Node and React but you don't

really need to know that much about those technologies in order to be productive with

the course. I'm going to walk you through exactly how to set up everything for the

playground so you don't have to worry about that either. By the end of this course you

will be able to take any coding agent and wrap it in a process so that you can start using it to

ship code on your own code bases. You'll be able to move faster than you've ever done before

because you'll be able to parallelise yourself with the AI. You'll be planning while the AI is

shipping. You'll know when to intervene as the human in order to prototype and research

and get a sense for imposing your taste on the project. Your code base will be healthier

than it's ever been before because we know that agents thrive in good code bases and you'll be

able to build PRDs, you'll be able to turn those PRDs into issues and you'll be able to plan

huge tranches of work for your agent to pick up. Now if that sounds good then you are in the

right place. Nice work and I will see you in the next one.


### 002-AI Coding for Real Engineers p02 002 Navigating The Discord Before We Start

One of the most useful resources you will have during the cohort will be the Discord server.

The Discord server is a place where you can get your questions answered,

where you can have discussions, where you can talk about stuff that's out of scope for the cohort

or stuff that you've kind of discovered while going through the cohort material.

Inside the Discord server then we have a bunch of stuff that's actually not related to the course.

So I have anyone who's really part of my community is in here.

We have the text channels where we have a general channel for just sort of general chat.

For any stuff that's specific to AI Hero there's a channel here.

Then I have some for my prominent open source repositories.

So Everlight has a repo or a Discord channel here.

Sandcastle has one here.

The Skills repo has one here.

Then there's a showcase channel for people to showcase whatever they want.

And then a channel for random folks.

So these channels up here these are general use channels.

So anyone who's even if you've not bought a course you can access these channels.

However the stuff that you get with your course is down here.

If you have the cohort 004 role in Discord you can see this.

One thing I've done with this cohort is that folks who bought the previous cohort,

cohort 003, can also access these channels.

So you can see in here that we actually have a bunch of folks already chatting

and these guys have the cohort 003 role.

So AI Coding Cohort General this is for anyone who's taken the AI Coding Cohort.

And AI Coding Cohort Random is the same kind of vibe

except it's just for out of scope stuff, off topic stuff.

We've then got two channels specifically for cohort 004.

So this one is for questions.

This one is really important for getting your questions answered

about specific things inside the course.

For instance in cohort 003 we did the same thing

and we got many many different questions here

all about different topics from within the course.

So if you have any questions regarding setup, anything that you need answers to

then you can open up a thread inside one of those questions

and you can get your question answered.

We also have a separate one of these for questions that you want answered

specifically by me in the office hours.

During the office hours I will be answering your questions

that's the whole purpose of the thing

and so I'll be looking in here to see your questions

and the best questions or the most popular questions will be floated up to the top.

For the duration of the cohort I'm going to be sitting in the Discord server

answering your questions.

And I'm also going to be nominating heroes.

So for instance El Gordino here and Kamel

both not only have the cohort 003 role

they've also got this little red hero role here

and you get the hero role for being heroic.

So for being really really helpful for posting interesting tips

or for just generally showing up inside the cohort and answering folks questions.

So if you see any heroes in the Discord

then feel free to thank them for their generosity

and treat them with the respect they deserve.

If you have any issues and you can't see the channels below

then make sure you click the link below

which will take you to an interactive setup

where you can just recover the role that you've purchased.

Hopefully that all makes sense

and feel free to ask in the Discord if you have any queries.

Nice work and I'll see you in the next one.


### 003-AI Coding for Real Engineers p03 003 Repo Setup Before We Start

Okay, let's clone the repo and pull down the actual workspace we're going to be doing the course in.

The repo is at AI Hero Dev Cohort 004 Project, and I will put a link below for you.

You can clone it to your local setup by pressing the code button here, by pressing HTTPS here,

and by pressing copy, and then by going into a terminal and writing git clone,

and then pasting in the URL that you got.

Again, I'll have this command below for you so that you can easily run it.

Next, you will need to download Node.js in order to complete the exercises.

You can go to the link below and choose your version.

I recommend you choose either LTS version is fine, so either 22 or 24 is the current state.

You can follow the instructions here.

Make sure you select the right platform.

And once that's done, you should be able to open up the project inside VS Code,

open the integrated terminal, and then run Node-v, and it will tell you some version.

If you get some kind of unexpected error here or you see something that isn't this little version number,

it means that Node has not been properly installed.

Once that's done, you're going to run corepack-enable here.

And what this does is it installs a really important little bit of kit called PNPM.

PNPM is just a lot faster than NPM.

It saves a lot more disk space.

And in my mind, it's the industry standard.

Once you've run corepack-enable, you should be able to run PNPM-v

and see some kind of version printed out.

And then you will be able to run PNPM-install to install all of the packages in the repo.

You should see some kind of output like this, which has all of the packages here.

And you should also see a Node-modules folder that has been added.

If I refresh there, there it is.

There's my Node-modules folder with a bunch of stuff in.

Once that's done, we're going to set up the playground here.

So we're going to go to the bottom and we're going to run PNPM-db colon seed.

What this is going to do is just seed a little database that runs locally with our project.

The project is a course platform.

And so inside the database, we've created some user tables, some categories tables,

quizzes, enrollments, lesson progress, records, quiz attempts, video watch events, all sorts of stuff.

And so now we can go to the bottom and run PNPM-dev.

And this runs a script to run the application locally on localhost, in my case, 5175.

If I go to visit that URL, then I should see a cadence video platform here.

If I click on courses, we can see some courses in theory.

There we go. Node.js and TypeScript looking good.

There is even a dev UI at the bottom here where we can log in as a user.

We're not going to explore this too thoroughly because one of the lessons that we're going to do in the course is exploring new code bases.

So don't get too familiar with how this works yet.

Let's not use our human eyes. Let's let the robots do it.

Why not? Finally, you should install the agents that you're using if you don't already have one.

In my case, I'm going to be using Claude code while we're walking through the course.

But the stuff we cover in the course will be workable with nearly any CLI based agents.

So for Claude code, I can run this command here and then I should be able to run Claude.

And then I'll be prompted to log in, follow the prompts to log in with my account, and we should be good to go.

Once that's done, you should be able to run Claude like this and open up the.

Yeah, here we go. Let me trust this folder.

You should see a UI that looks something like this, although they may have changed it by the time that you see this.

There should be some variety of text input here that you can say hello and it should reply to you back with some message.

If you have any setup issues or weirdnesses at all, make sure you head to the Discord so that people can help you out.

But if all went smoothly, then you are ready to take the course.

Nice work, and I'll see you in the next one.


### 004-AI Coding for Real Engineers p04 004 Database Migrations Before We Start

One thing that a lot of folks got confused about when I first ran this course was how database and

database migrations work. If you are an experienced developer you probably don't need to watch this bit

but if you need a bit of kind of catching up on how databases function then this is the lesson

for you. The type of database that we're using is an SQLite database and that sounds pretty

scary if you're a newbie but really what this means is it's a type of database that you can

save as a file on your file system. This is very different from databases like Postgres for instance

that you need to host on a remote server or run in let's say a docker container. If you ran the

db seed script then you should see these little files here data.db data.bd shm data.db wow.

If we want to we can totally delete these files from our code base that's a very simple

way that we can just reset the database back to nothing. And now if we try to run pnpm

dev let's say and visit localhost 5175 then we're going to get an error that looks like this

saying no such table courses because it's trying to fetch a courses table that doesn't actually

exist because the database isn't there. So this means we can come back into here we can

control c out of the dev script and run pnpm db colon seed again which will reseed it.

And just like that if we look at our file system again we can see that data.db is back.

The way that we manage changes to the database is by looking at first of all the schema.ts file.

Inside here we can see there are multiple different tables that represent the different

things inside the database. So we have a users table, a categories table, a courses table,

modules table, lessons table, enrollments table etc. You don't need to like look at this in

depth but this is an important thing to see. This is a drizzle schema and drizzle is a

library that we're using drizzle orm up here to manage our database. But changes to this schema

won't automatically synchronize over to that database. To synchronize it over you can see

the script that we might want to run. Inside your package.json file there are some scripts

inside here and these are the ones that we have been running with pnpm. So pnpm run db seed

that was the script that we've run. We ran the seed scripts just here.

We've run pnpm dev to run react router dev to start the dev server. There's a couple of other

db scripts that you need to be aware of. First of all is db generate. Every time you make a

change to the schema a new one of these will be created when you run db generate. If we go back

to package.json and usually your agent will be smart enough to work this out itself. The

thing the agent probably doesn't know to do is to run db colon migrate. What this migrate

script does is it looks at all of the migration scripts just up here and then if any haven't been

run it runs them. So this means that you need to deliberately keep your database in sync with

the state of your code. So the whole process looks like this. You have a schema.ts file

which is the kind of drizzle source of truth. You run db generate to turn that into migration

files and then you run db migrate to actually migrate it to the database. This is how a lot

of production setups actually work and this is the setup I want you to bear in mind anytime

you're doing work with the database. And remember if you get into trouble and you need to reset

you can always just delete this data.db file run pnpm db seed just here and you should be

fine to start again. There are no actual users relying on this data it's just a dummy database

so you can feel free to just delete it and refresh anytime. Nice work and I will see you in the next one.


### 005-AI Coding for Real Engineers p05 005 Setting Up Claude For The Course Before We Start

Okay, now the repo is fully set up.

We are now going to be setting up the agent

that I'll be using throughout this course,

which is Claude Code.

If you want to follow along with Claude Code,

you are absolutely welcome to,

but you're also welcome to use

any kind of CLI based coding agent.

But for those who've never used a coding agent before,

I recommend you do use Claude Code.

And the video here is advice

for what you should do if you do use it.

And the first question you probably have

is which model should I choose?

You can choose your model by specifying forward slash model

and running this and you can set the model for Claude Code.

So what I recommend is going with the defaults.

But the tricky thing is that your defaults will be different

based on which subscription you have.

So for me, I'm on 5x max.

So my default model is Opus 4.6 currently.

However, if you're on the pro subscription,

then your default will be Sonnet 4.6 instead.

I do not recommend using Haiku

at any point during the course.

Basically, it's just not capable enough.

And even though it's fast,

it just won't handle some of the workflows

that we're gonna throw at it.

So those are my recommendations.

If you're on 5x max or the max max plan,

then go for Opus 4.6.

If you're not, then I recommend going to 4.6 Sonnet.

And I also recommend choosing medium effort.

You can choose low effort

just by adjusting left and right here or high effort.

I basically recommend whatever the default

the harness suggests is.

For instance, recently they defaulted to high

for Opus 4.6 and then they lowered the default

to medium again.

They must have done some internal evaluations

that actually checks that okay,

medium is fine for most work.

So to select the model and the effort,

I can just press enter here

and then we can see set model to default Opus 4.6.

So your next question probably is

which subscription should I get?

There are several options.

You can go for pro, you can go for max 5x

or you can go for max 20x.

Now I can't give you a recommendation

because I don't know what your constraints are

in terms of cost.

I don't know what your constraints are

in terms of how much you're gonna use this going forward.

What I would say is that I created the course

with max 5x on this price point.

So if you want to use the best model Claude has available

which is Opus 4.6,

then I do recommend getting that max 5x

even if it's just for a month.

But if you can't stretch that far

or you just wanna try it out,

then pro with Sonnet 4.6 will be good enough.

I can't guarantee that if you're not like

diving deep into every lesson,

diving deep into every section

that you won't come up against usage limits,

but you should be able to get through it

with pro for sure.

So those are my recommendations.

Use the default model for your subscription tier

and decide between pro or 5x max

depending on what your budget is.

Nice work and I will see you in the next one.

Hello folks, edit Matt here just to say that

the models have changed slightly

since I first ran this course,

but the actual subscription tiers

and the underlying ideas have absolutely not.

Whichever model provider you use,

they are gonna have a sort of Opus level,

top level model.

They're probably gonna have a mid tier model

and they're probably gonna have

a very cheap Haiku level model.

If you have any further questions about which model,

which agent setup you should use,

then do feel free to ask in the Discord.

Nice work, edit Matt out.


### 006-AI Coding for Real Engineers p06 006 How To Take This Course Before We Start

This course is structured into a bunch of interactive exercises,

and these interactive exercises all happen in the playground.

Now in order to run those exercises and do them yourself,

you're going to need to get your repo into the same state that mine was when

I recorded the exercise.

I've given you a really simple,

easy to use tool that you can use to get your repo into the same state as

mine.

The way this works is you can go into the playground and run PNPM reset.

And what this will do is give you a bunch of commits that you can choose from,

from a history that I've provided for the entire course here.

For instance, we can reset to main, which is the starting point,

the main branch of the repo.

Or if we want to reset to a future point to maybe do a lesson further on

in the course, then we can reset to that point.

I'm navigating down this by just pressing up and down like this,

but I can also search.

So if I want to look for the grill me skills section,

then I can type grill me and that will show up.

Or I can search by number.

So oh four point oh five point oh one, for instance.

Then we've got this skill as a demo.

We are going to reset to this little point here.

Oh one point oh one point oh one.

And here what you'll notice is that we're on main right now and inside

the package doc Jason file, there's a description saying,

it's an awesome horse platform.

That doesn't seem right.

This is a course platform, not a horse platform.

So what we can do is we can use reset to reset to the point where I

fixed that package doc Jason description.

And if we select this, then it says you cannot reset the main branch.

So we're not on the correct branch.

So it's now giving me the option to choose a new branch name.

I'm going to call this dev for instance.

This is going to be my working branch throughout the course.

And now it creates a new branch dev and it's switched to the version of

the course or the version in the history where I've got an awesome

course platform instead of an awesome horse platform.

So two things happen there at once.

We switch branches to a new branch.

So if I run git status, we can see we're on branch dev.

And if I run git log like this, we can see that the commit here is

the one with the fixed package Jason description.

If I want to, I can run PM PM reset again, and now I can go back to main.

So I can reset to the starting point.

And when I do this, then if I choose that, I can either reset the current

branch or create a new branch from the commit.

I'm going to choose to reset the current branch.

And now we've got an awesome horse platform back.

So we're back at the starting point.

Now, PM PM reset is a destructive action.

That means it deletes existing work when it finds it.

This is really useful if you want to totally reset your repo to the state

that it was when I recorded the video, but it's less useful if you have

some cool work that you want to preserve.

For instance, let's say you added an NPM script here saying pizza that

just echoes an emoji of a pizza.

You commit it and you want to preserve it.

And let's just grab that in there.

Then we're going to run PM PM reset again.

And if we reset to main or we really reset anywhere actually, and let's

just reset the current branch, then we are going to, if we see pizza

is still there and then we reset the current branch and now the

pizza script has gone.

So unrelated changes get removed when you reset.

You're resetting the entire branch to the state that I recorded it in.

If you have some work that you want to preserve, then you can run PM

PM cherry pick, and this preserves existing work.

So I've reset our repo back to the main branch and you can see

we're back at horse platform here.

If I go in and add our pizza script again, and I will generate a

thingy thing here and I've committed.

Now, if we try to let's go PM PM cherry hyphen pick instead.

When we go to cherry pick the commit here, we should now should just work

because all we're changing is this course platform and our existing

work gets preserved.

However, if I reset back to main, so let's just go PM PM reset

heading back to main here.

I'm going to reset the current branch.

So we go back to horse platform.

If instead I go to frog platform like this, you can tell I've got a

two year old cause I just think in farm animals and I commit it here.

Now, when I go to run PM PM cherry pick and I cherry pick the course commit,

we're going to get a merge conflict because it's attempting to preserve my

previous work, but we have a merge conflict between the both here.

We can see the incoming change here is the course platform, which is the

one that we're attempting to cherry pick.

And the current change that we have is the frog platform.

Now, if you get into a situation like this where you want to cherry pick,

but you have a gnarly merge conflict, then AI is actually really good at

helping you out.

You can just say Claude, fix this merge conflict for me.

And it will guide you through it.

Or if you just want to get out of there, you can run git cherry

pick hyphen hyphen abort, and it will abort the cherry pick.

And you'll still end up with your work preserved.

Finally, the way these courses generally work is I'll be pushing

updates to the course while you're taking the course, either to fix

local issues or update packages, things like that.

So this means that your dev branch, the one that you're working on

will get out of date with what I've prepared locally.

So what I've done here is I've provided for you.

Let's just do a git status.

We're on the dev branch and we are going to run PNPM pull here.

And PNPM pull is kind of like an analogy to git pull, except it fetches

all the stuff from the parent repo and pulls them into your branch.

And in theory, this will just preserve everything.

So it's not going to be a reset.

It's not going to reset it to any state.

It's just going to grab all of the changes to main and pull them

into your branch.

If you do get any merge conflicts here, then you should head into

Claude and say, just fix the merge conflicts.

So those are the three commands you need to know PNPM reset, which

totally resets your work to the state that I recorded it in.

Cherry pick that allows you to cherry pick existing commits and PNPM

pull, which pulls in upstream changes as I make them to the repo.

Hopefully that all makes sense and feel free to ask in the

discord if you have any questions.

Nice work and I'll see you in the next one.


### 007-AI Coding for Real Engineers p07 007 Office Hours Before We Start

As part of this course, you get office hours with me.

This is about a 30 to 45 minute live stream that we do on day one, day five and day eight.

It's a YouTube live stream.

So you can just log in with your YouTube account and comment there.

And I'll be able to see your comments and we'll have a nice chat.

And we can basically talk about anything.

This could be stuff in the course or it could be stuff that's happened

while the course has occurred.

The videos for the office hours will be just available as YouTube VOD.

So I'll keep them up there.

This is absolutely not mandatory viewing.

It's mostly just for vibes and for having a bit of fun during the course.

Though, of course, if there is something that you want to walk through in depth

with me, then that is absolutely the time to do it as well.

If interesting stuff comes out from the office hours, I usually record it

as a little explainer somewhere in the course.

So don't feel like you have to watch the whole thing just to catch any golden

nuggets that might fall from this particular goose or eggs, I suppose, if it's a goose.

But anyway, I won't be laying eggs on stream, that's for sure.

The links for all of the office hours are below.

Nice work and I'll see you in the next one.


### 008-AI Coding for Real Engineers p08 008 Intro Getting To Know Claude Code

In this course I'm going to be primarily using Claude Code as my agent for driving the lessons,

for demonstrating things and for showing you how, you know, agents in general work.

I'm doing this because it's a very popular harness, you may have used it yourself,

and it's the one that I personally use the most right now.

But this course is harness agnostic, so you can choose whatever harness you like,

as long as it runs in a CLI.

However, for folks who've never used a coding harness before,

or who just want a bit more out of Claude Code,

I've given you this section here so that you can get the basics before we get started.

It will give you a nice grounding of all of the things that you'll need to know about Claude Code

before getting started with the course.

And if you're experienced with Claude Code, then you'll probably still pick up a few tips,

because I'm not just covering the basics, there are a couple of advanced things in there too.

So, nice work, and I will see you in the next one.


### 009-AI Coding for Real Engineers p09 009 Managing Your Claude Code Session Getting To Know Claude Code

All right, so you got Claude code ready to go and installed.

Let's open it up and check out the first few commands that I want you to learn.

For this entire course, I'm going to be running Claude from within VS code.

We're going to talk about the relationship between Claude code and VS code.

But for now, it's OK just to run Claude inside the integrated terminal.

What you should see is a UI kind of like this.

I can't promise that they haven't changed the UI since they've recorded this.

But something they will definitely keep is this enormous input box here.

We can say to Claude, hello, how are you?

And then to send it, we can press return inside the terminal.

It comes back with, hi, I'm doing well.

Thanks for asking. How can I help you today?

In other words, this so far is so much like any other AI chat

application that you've used already.

At this point, I would like you to run something.

I'd like you to run forward slash then terminal hyphen setup.

It should turn this nice shade of lilac when you've completed the command here.

You can then use enter to initiate the command.

And this will set up a couple of key bindings for you.

In my case, because I'm on Windows Subsystem Linux,

then I have to install this manually myself.

But if you're on a different operating system,

like such as Windows or like Mac, you're going to just have it installed for you.

But once it is installed, you'll be able to do something very nice,

which is you'll be able to press shift enter to add new lines into your input here,

which is really important when you want to express more complicated things.

For instance, I can type thank you and then add a couple of new lines

and then say very much like this for sort of dramatic effect.

So from here, let's show a couple of really important commands

that we're going to be using on every single time that we use Claude Code.

The first one here is forward slash usage, which shows your plan usage limits.

So again, just to show you that again, because I did that quite fast,

we go forward slash then usage.

And I can even use tab here to complete the command there.

So again, usage like that.

And then I run it with return.

And this shows me how much Claude Code usage I have left in my current session

on my current week.

And there's a separate one for current week, Sony only.

Now, this will probably look different based on which plan you're on

and what Claude plans even look like in the future.

For me, I'm on 5x max, and this is what it looks like with 5x max.

I can then press escape to cancel out of this.

Another really important command is to run forward slash context here.

And what context is going to do is show me a graph of all of the different ways

I'm using up my context window.

We are currently using about 21,000 tokens out of a maximum of 200k tokens.

So we're using around 10% here.

We're going to be talking a lot, lot more about context throughout this entire course.

And so this is a great way of giving you the ability to introspect the context

that you're using and how much you have left.

The next command you definitely need to know about is to go down to the bottom

and run clear here, which clears the entire conversation history.

Clear resets that context window back to zero.

So it's kind of like you started up a whole new chat with Claude code.

It's forgotten everything that you talked about in your last chat.

Again, we're going to be talking a lot about when to clear the context window,

but this is how you do it.

You either, of course, you can either just cancel out of code

by pressing control C twice and just starting up a new Claude session here,

or you can clear the current session by just running clear.

Now, finally, how do you interrupt Claude when it's running?

Well, I'm going to ask it a question that's going to take a little longer to answer,

which is tell me about this code base here.

And any time I want to, I can just press escape to interrupt it.

Once I've interrupted it, if I wanted to go again, I can just say go as well.

And that was me literally just typing in the word go and sending it on its way again.

And if I want to interrupt it again, I can just press escape

and then it stopped doing what it's doing.

OK, so we've learned how to add basic prompts inside here.

We've learned that we can do shift enter to add new lines.

We've learned how to invoke commands with forward slash and using tab

to get to the end of the command.

We've learned how to run usage here to check our plan usage limits.

We've learned how to run context here to visualize the current context.

And we've learned how to clear the context with forward slash clear.

So I would say those are the basics done.

Nice work. And I will see you in the next one.


### 010-AI Coding for Real Engineers p10 010 Prompting In The Terminal Getting To Know Claude Code

Now we understand the basics about Claw Code, I want to give you some nice little tips that you can use to improve your prompting.

You may want to reference individual files when you're using Claw Code.

For instance, you may want to say, tell me lots of information about this file or make some changes to this specific file.

To do that, you can use the at command and start typing inside here.

For instance, I might want something inside the roots.ts file and it's just right here.

So I can auto complete by pressing up and down on the keyboard.

When I want to select something, I can press tab here.

And of course, if I want to add another file, I can just go through that process again, where I can say app and then DB.

And let's see what's in here.

Maybe DB schema is what I need.

So I tab and I complete that.

When I then run this by pressing return, these files will be automatically read into the context window here.

This means that it doesn't need to go and find those files manually.

It's just read them automatically.

This does cost you a little bit of upfront time, in other words, having to find these files.

But it is worth it because it gives Claude exactly what it needs to succeed.

One other tip you might not know about, even if you've been using Claude code for a while, is if you have a big prompt here and you want to,

let's say, not do this now, but do it later, you can press control S and it will stash it.

This has now stashed my command inside Claude's memory here.

And I can now submit another command, let's say hello, like this.

And it will then rehydrate and sort of come back to me here.

So again, I can stash with control S.

I can submit something says I'm good.

Thanks.

And when I submit, it will then restore after that.

This is really useful when you're giving Claude some feedback, let's say on some code that it's not done very well.

And then you realize, oh, I just need to tell it something first, stash my current command, bring it back later.

If you then realize, oh, I don't need this command at all, you can press control C and get rid of it.

One other really sweet thing you can do is you can copy and paste images into Claude code.

I've got this lovely image of Lake Bled in Slovenia.

I can right click it, copy the image and go to Claude code.

And if you copy and paste it in, it can then reference that image.

Annoyingly, I'm on Windows Subsystem Linux and this doesn't actually work on WSL.

But if you try it for yourself and press return, then it should be able to tell you where am I in the world?

And it should tell you Lake Bled in Slovenia.

Pretty cool.

So to summarize, then we've covered referencing particular files with this at symbol here.

We've covered stashing with control S and we've covered pasting in images, which I'm kind of gutted not to be able to show you.

And hopefully you were able to follow along clearly and nothing went wrong or did anything weird.

Nice work. And I will see you in the next one.


### 011-AI Coding for Real Engineers p11 011 Claude And Your IDE Getting To Know Claude Code

Let's now talk about how Claude integrates with your IDE of choice.

I'm using VS Code for this course, but you do not have to.

You can use Cursi, you can use Windsurf, Antigravity,

whatever fancy tools are available now.

The way that Claude integrates with it is via this IDE command here,

where it says you can manage the IDE integrations and show the status.

If we run this, we can see that we are connected to Visual Studio Code.

I've got this working because I have installed the Claude code for VS Code extension here.

But if you run IDE in your terminal here,

then it should show you how to install your version for your IDE that you're using.

If you're following along, let's press Enter to confirm and get out of this.

The IDE integration is really for diff management.

That's the thing that comes up most often.

For instance, if we prompt Claude to say,

remove the test watch command from package.json,

we can see that it read one file.

So it read the package.json and now it's made an update to package.json.

Now, if we weren't connected to the IDE,

then this would show as a diff inside the terminal, which is a little bit awkward.

But since we're connected to VS Code,

we can actually close this and we can see the diff in VS Code.

This is really nice because this is much, much richer.

And it lets us actually scroll and see what's going on in the file.

And we can see that this is a decent edit.

We can then either press this accept proposed changes up here

or we can click inside here and save the file.

And by saving the file, we agree to the changes.

This is the reason that I'm running Claude code inside VS Code.

It's really nice to be able to dive in sometimes

and just tweak some things about Claude code's output.

And if I need to update any diffs or review any diffs,

it's so much nicer doing that in a proper IDE

than just doing it in the terminal.

There are more features and there are more ways

that VS Code integrates with Claude code

and your IDE probably does too.

But this diff feature was the one I wanted to show off

because it's the one I end up using, you know, 99% of the time.

So hopefully you were able to follow along with that.

Feel free to go back through the video if you weren't

and ask any questions on the Discord if you ran into trouble.

Nice work and I will see you in the next one.


### 012-AI Coding for Real Engineers p12 012 Going Forwards And Backwards In Time Getting To Know Claude Code

One really important thing that Claude code allows you to do is go backwards and forwards in the conversation.

This is really important for when you're trying something out that maybe you later want to revert.

For instance, in the previous video, we just did a change where we removed a dev script.

Now, what I could say to Claude is just revert that, please,

and it will go and undo the change that it just did before by just rewriting, re-adding it back in.

And I'm just going to accept this by pressing Ctrl S to save the diff.

But there's another option here.

I can press Escape Escape in quick succession to enter rewind mode.

And in rewind mode, I get to restore the code and or the conversation to this point.

For instance, if I just want to revert the command that I just did, I can just choose this one.

This one at the bottom is the current state.

This one is the point at which I said revert that, please.

And so I can select it with enter.

Now, there's a few different options here that I can choose.

The first one will be to restore the code and the conversation.

In other words, to just rewind my session to the point before this code edit was made.

Or I could restore the conversation, but keep the code as it was.

That would be number two.

Or I could restore the code, but keep the conversation how it is.

The one I choose most often is just to restore the full code and conversation.

So I'll do that now.

And we can see that the code has been reverted.

So now we are back to the point at which we had test watch deleted.

If I want to go back further, I can open up the terminal again and just press escape twice to go back.

And let's choose we go back to the point where we remove the test watch command completely.

Another interesting option is this summarize from here command, but we'll talk about that later.

I'm actually going to cancel this by choosing never mind and just sticking to the current state.

One of the things that's also really important is the fact that Claude actually persists its sessions locally.

What this means is you can quit out of Claude by pressing control C twice and then you can resume it in a bunch of different ways.

You can either resume the session by running this command directly that you get from the output of the previous command.

So I can just run Claude resume and then the UUID.

And then I just go back into the exact state that I left previously.

Another way of doing this is if I can just control C twice again to exit and I opened up a new session just by typing Claude.

This one is a totally clear session.

Inside here, I can press forward slash resume and resume a previous conversation.

And now I get to choose all of the conversations that I've had here.

I can even search through all of the sessions that I've had in the repo if I want.

Let's go back to the one that we were just using and I can press return to go into that.

And again, I'm back in that same session.

So if your session is interrupted for any reason, then you can always resume it because Claude persists it locally.

So that's how Claude allows you to go backwards and forwards in the conversation, either by entering rewind mode by pressing double escape and just kind of like zooming through all of the content here.

Or I can cancel out of this and restart my session any time.

I can even just choose to resume the previous session by running Claude hyphen hyphen continue.

And again, this pulls me into exactly where I was.

Beautiful. So very nice work and I will see you in the next one.


### 013-AI Coding for Real Engineers p13 013 Running Bash Commands Getting To Know Claude Code

One super important part of working with Claw Code is running bash commands.

Bash commands turn your agent from just a passive code writer into something that can actually seek feedback loops,

can actually work with your project and can use all the power of bash at its disposal to find information and to do stuff.

Now we can just manually ask Clawed, OK, run the dev server for me.

And because it's quite smart, it will understand, OK, I need to read the package.json.

I need to find where the dev server is and then I need to run it like this.

We'll get into what this is doing here in this kind of approval setup here.

But suffice to say, there are sometimes when you just know what command you want to run and you just want to run it and then put the results into Clawed's context.

So the way you do that is I've just restarted my Clawed code instance.

I'm going to just put an exclamation mark and now I've entered bash mode.

And now anything I put in here will be turned into a bash command and actually run for Clawed.

So, for instance, why don't I run npm run type check inside here?

And now it just runs the command after I press enter.

Now, because I haven't run npm install in my setup here, I'm getting a lot of errors and these errors are now present to Clawed in its context.

So I'm going to get it to help me solve these errors and it will be able to see the errors and actually work with them.

And there we go. It's figured out that Zod is in package.json, but not installed.

I should run npm install. There we go.

Now, this works well for commands that essentially have a start and an end.

But what about commands that are supposed to persist, like long running dev servers?

Well, for that, we can run npm run dev inside bash mode here.

And what we can do is while it's running, we can actually press control B to run it in the background.

And in this version of Clawed code, something appears that says command was manually background with user with ID this.

And any output in that task goes into a local file.

You can then see that underneath our status line here, there is a little background task that's showing.

And so I can zoom downwards with just the down arrow there and I can press return to see it.

And now I can actually view the shell.

I can view what's going on here and I can see that it's on localhost 5175.

I've got lots of options here.

I can stop it with X if I want to, or I can just press left to go back.

And now I'm back in my Clawed code instance.

This is really useful when you're debugging a problem with your dev server, let's say, or with a long running command,

because Clawed can see where all of the logs are being written to.

It can try something out in the UI maybe or send a curl request.

And then it can actually see the output of the dev server.

So I've just reset my instances so we can see another feature, which is suspending Clawed code.

If, for instance, I want to run something that I don't want Clawed to see the results of, or I don't care to show it,

and I have some state inside Clawed that I want to preserve, then I can use suspend.

I can press control Z inside here and Clawed code has been suspended.

This means I can now run any command I want to.

I can just echo foo inside here.

And this is not visible to Clawed code.

If I want to bring Clawed code back, I can just run FG here and I get my Clawed code instance back with all of its state.

So this is great if you just want to go, OK, don't care about Clawed code, do something like whatever command I want,

and then FG to bring it back.

So the decision tree for this really looks like this.

If you want the output of the bash command that you're running to be visible to Clawed,

then you can use bash mode here by using the exclamation mark.

And you can background that with control B and then manage those backgrounded tasks.

Again, really, really useful for dev servers.

I don't use it every single time, but when I do use it, it's usually for debugging some kind of dev server issue.

But if you want the command to be totally hidden from Clawed, you can just suspend it quickly with control Z.

And of course, these are Windows shortcuts, so you might be needing to do something different if you're on Mac.

So those are all the different ways that you can manage bash commands in Clawed code.

Nice work, and I'll see you in the next one.


### 014-AI Coding for Real Engineers p14 014 Permissions Getting To Know Claude Code

Whenever you're working with an agent, you always need to think about risk versus reward.

Especially in how much power you give over to it.

If I were to give Claude infinite power like many people have done,

then I would be understandably nervous that it would do something crazy with that power.

For instance, you know, delete my entire file system by accident.

To mitigate that Claude code has a very detailed permissions model

and by default is very strict with itself with what it allows the agent to actually go and do.

For instance, I'm going to tell Claude code to run a bash command to run echo hello.

And because echo is an extremely safe command, Claude code thinks this command is fine for it to run.

But if I get it to do something else, such as run a type check on the project,

then it might do something differently.

We can see it's now requesting to run a command here.

So it's trying to run PMPM type check.

So we see a few things here.

We see first of all the command, the exact command it's going to run.

We then see the reason it wants to run it.

It wants to run a type check using react router type gen and TSC.

And we have three options here.

We can say, yes, you're allowed to do this this time or yes.

And you're allowed to then from now on, run any PMPM type check command inside this project.

Or we say no.

And inside here, we can do something clever.

If, for instance, we don't want it to do this exact command,

we can press tab and we can give a reason here.

For instance, we might just want to use NPX TSC instead for some reason.

And now it's asking us if it wants to if we can run NPX TSC instead.

So let's say we agree to this and we say, yep,

and you don't need to ask again inside this project, what actually happens?

Well, first of all, for some reason, it's actually failed the type check on this branch,

which is, I think, my fault.

As we can see, it actually reported the results from the type check

and they were reported back to the LLM.

But crucially, our preferences here were recorded inside a file just at the top here.

This is inside the .clawed folder and this is inside settings.local.json.

Here we have a permissions property on side this piece of JSON here.

And inside this allow array are all of the things we are allowing for this project.

The syntax is really important to understand here because we can actually edit this ourselves

if we want to ahead of time, allow things to happen in the repo.

For instance, if we want to, we can say bash here and just say, let's say, PNPM type check.

And this means that the PNPM type check command will now be automatically allowed by Claude code.

If instead we want to say that all PNPM commands are available,

then we can replace this with a wildcard here.

We can also disallow Claude from doing things by using the deny inside here.

For instance, we might not want it to run bash, let's say, git push, for instance.

And so git push with a wildcard would be a safe one here to deny it always.

However, it's not just bash commands that Claude code needs permission in order to be able to run.

Claude code can also search the web and fetch web pages in order to back up what it's seeing locally.

So for instance, I can get it to fetch info about React router type gen from the web.

And it's now asking me to do a web search for React router type gen.

If I say yes and don't ask again for web search commands,

then it's going to add it to the settings.local.json up here.

And we can see that it's then going to fetch from this website, reactrouter.com.

So now it's fetched from there and it's given me a summary of how React router type gen works based on the actual documentation.

The final thing to say is that these settings.local.json are in my project, they git ignore, so they apply only for me.

But if I wanted to share these with my team, let's say,

and have a specific set of things that were always allowed within this repo that were part of those project settings,

then I would rename settings.local.json to settings.json.

These can then be shared with your team or any Claude code instance that's running on your repo.

And they will pick these up too.

This can be incredibly powerful for anyone starting on your repo for the first time.

They just run Claude and Claude then knows what's allowed for that repo,

which can be a lot faster than having to manually set up the permissions for yourself each time.

We're going to be touching on permissions more throughout the course, of course,

but I just wanted to give you an intro so you understand what the approval flow looks like

and you can edit these permissions if you like.

Nice work and I will see you in the next one.


### 015-AI Coding for Real Engineers p15 015 The Constraints Of LLMs Day 1 Fundamentals

Before we even touch Claude code, we need to understand the constraints of LLMs because they come with some extremely strange ones.

A lot of people think of LLMs as like a really enthusiastic junior developer who can work 24-7, but it really is a lot weirder than that.

And understanding this stuff is so fundamental because if you don't understand it, you're going to end up blaming AI when in fact you're just working against how the models are supposed to work.

In this video, I'm going to walk through each of these constraints and explain how they affect your usage of tools like Claude code.

And let's start with the biggest constraint, which is the scaling laws around tokens and the context window.

The way that LLMs work is they take input text like this, they split it up and then they tokenize it into numbers here.

You don't really need to know why they do this. I've talked about this in separate videos.

But when you get these lists of tokens here, all of the tokens that the LLM can see are its context window.

We've only got three tokens here in this very small example, but a typical context window maxes out around 200,000 tokens.

Now, if we were to add another token to this context window here, you might think, okay, all we got to do here is just store an extra number in memory, right?

But that's not quite right. Not only are we storing the actual token in memory, we're also storing all of its relationships to every other token.

So for four tokens, that means six relationships.

For eight tokens, we've immediately scaled up to 28 relationships.

And if I were to draw 100 tokens here, that would mean roughly 5000 arrows here.

In other words, every time we add a token, the number of things the LLM has to track and keep hold of scales quadratically.

It's not like appending a character to a document.

It's like adding a team to a football league where the number of games played massively increases as you add teams.

Now, what this means in practice is as you're using your coding agent, as you're adding more messages to the context window, you are really putting a huge strain on the LLM.

And this means as you fill up the context window, the model will start to struggle and you end up in what I call the dumb zone.

In the smart zone, early in the context window, the LLM has lots of memory to spare.

Its attention relationships are not very strained and it can reason really clearly.

It can attend to all the information in its context window and in general it makes smart decisions.

But later, when it starts getting a little bit more strained, it goes up into the dumb zone.

This is where hallucinations start to creep in.

And reasoning gets a lot worse and sometimes it will struggle to recall information that's just sitting there in its context window.

Now, where this dumb zone actually starts is a matter of some controversy and it will probably change over time.

But I start getting paranoid around the 40% mark.

In other words, in a 200,000 token window, I would start getting scared around the 80,000 token mark.

Some might say this is too aggressive and that, you know, maybe 60% or 70% is where the dumb zone starts.

But everyone agrees that it does exist and whenever you're using LLMs you need to bear it in mind.

Now, the smart zone and dumb zone is the main constraint that we're going to be working against throughout this entire course really.

But I wanted to mention some others because they really inform how you use LLMs too.

One of the main failure modes I see is from people trying to use LLMs as a database to just perfectly retrieve information from its pre-trained knowledge.

That's because it's very tempting, right?

If I say to be or not to be, that is the question, whether it is noble or unreminded, to suffer the slings and arrows of outrageous fortune.

LLMs do kind of behave like a database sometimes, just spewing out information from their training data.

However, we need to be super careful when we think of LLMs as a database or try to use them in that way.

If we're training a relatively small model, we might take, let's say, 10 terabytes of training data, like all of human knowledge.

In reality, this data would be much, much bigger for the massive models, especially the ones we're using with coding agents.

And then we compress all of that down into a set of parameters, which is a decent enough size that it can fit on a GPU.

In other words, the right mental model for LLMs as databases is that they've seen all of human knowledge, but they've got it as a kind of fuzzy JPEG.

They've compressed it down to a point where it's hardly even visible to them.

So when you ask an LLM a question, it's not referencing the training data directly.

It's referencing this fuzzy JPEG that it has, which means that its answers are by design unreliable.

This is not true, however, of stuff in its context window. Of stuff in its context window, it has access to the entire raw information.

So if you ask it questions about stuff that it has in its context window, it's going to give you pretty reliable answers.

However, of course, the more you stuff the context window, the more you put it into the dumb zone, the less reliable those answers are going to be for reasons we discussed earlier.

Another key constraint that emerges from the way that LLMs are trained are knowledge cutoff dates.

This pre-training process we talked about here is prohibitively expensive, and the process for testing a model too is often really elaborate and expensive too.

So models are not kept up to date with the latest information when they're deployed.

If you have a model deployed in January, it won't know anything that's happened in the world since January.

For AI coding, this means it won't have any information about the latest React version if they've pushed that.

And so this all of human knowledge, it's all of human knowledge up to a certain date.

However, because LLMs are compressors anyway, and this is just like a fuzzy JPEG of all of its information,

I tend to put less focus on knowledge cutoff dates than other educators.

Because I distrust the LLM as a database so much that I wouldn't expect it to kind of have any background knowledge whatsoever.

That's the mental model I'm coming in with.

Finally, the weirdest constraint is that LLMs are completely stateless.

This means LLMs behave kind of like that guy from Memento, where every time he woke up, he would completely forget his entire life.

In practice, this means that as you're working with the LLM, kind of adding things and adding stuff into here,

when you clear the context, you completely reset back to nothing.

And you then need to build it back up again, right?

So when you clear the context and start fresh, you're losing the tribal knowledge that the LLM has built up over your code base.

This means that documentation and code base quality and organization become absolutely key.

But we're going to explore that more in the steering section.

So those are the main constraints of LLMs, that they have a smart zone and a dumb zone,

that they have seen all of the world's information,

but it's kind of like it was written scribbly on the back of a napkin somewhere and they can only half remember it.

And they were pre-trained at a certain point in time, which means that their knowledge only goes to a certain date anyway.

And they are totally stateless, which means that every time you clear the context, you are essentially wiping their memory.

All of their feelings, all of their experiences are just BOOM, gone.

As developers or as managers, these are the weirdest set of constraints we've ever had to work around.

When you have a new starter joining your team, at least, you know, they might rock up at 10am or something,

but at least they have a memory.

At least they can learn over time and at least they don't have such a narrow window in which to work before they just forget all of their memories.

During this course and throughout this cohort, we are going to be working with Claude Code to get the most out of these constraints,

because when you work within them, you realise, ah, there are actually many techniques I can use to get the most out of these tools without bumping into their weirdnesses.

Hello, folks. Edit Matt here.

Since this course was recorded, or rather parts of this course were recorded,

the kind of dominant context window has gone from 200k tokens to 1 million tokens.

And for most people now, the default context window size in Claude Code is 1 million tokens,

and that's what I've recorded some parts of the course with, but some parts of the course were recorded with the 200k version.

So you probably have an immediate question. What does this do to the smart zone, dumb zone calculation?

Is 40% still the correct metric?

Well, in my opinion, all that's changed with these big context windows is they've shipped a lot more dumb zone to you.

So now you can do a lot more work in the dumb zone, if you like.

But the actual size of the smart zone has not changed all that much.

Since the first time I recorded this video, we are now, I would say, at around 100k tokens is the smart zone.

So whenever you see a percentage calculation for the rest of the course,

remember that that was done with a 200k token window, not the 1 million token window.

So really now we're thinking in terms of just raw numbers of tokens instead of percentages.

So there we go. Edit Matt out.


### 016-AI Coding for Real Engineers p16 016 What Are Subagents Day 1 Fundamentals

Now we understand some of the constraints of LLMs, let's start talking about how

Claude Code tries to mitigate them.

Specifically, there's a super important strategy that Claude Code implements to

squeeze more juice out of its context window.

I've got a little visualization of the context window here.

We can imagine that each of these sections are different tasks that Claude

Code needs to do in that session.

This gray bit I'm imagining is the system prompt, the bit that we saw in the

context, the stuff that's always in there, the system prompt, the system

tools, the stuff that's always been passed to the LLM to tell it how to behave

like Claude Code.

Then the first thing the agent might need to do is let's say explore the

repo.

It comes in with zero memory, right?

So it needs to do a bit of exploration before it then goes onto the green,

which in this case is implementation.

And then in this example, this dark gray is stuff that's just empty space

in the context window that hasn't been filled up yet.

Now the dream for any kind of harness, any kind of Claude Code like

application would be to make these chunks smaller, right?

Because the less tokens we spend on exploration, the more tokens we have

available in the smart zone for the implementation.

But of course, if we spend less effort in the exploration mode, we were

probably going to end up with a worse exploration, which means probably the

LLM will have fewer, less context about our repo, which probably means a

worse implementation.

So it's hard to see how you bridge this divide.

So Claude Code and agent tools like it employ a really smart solution.

In the agent that you talk to, which is the orchestrator agent, it then spawns

a sub agent.

In other words, it creates a new context window and prompts that sub

agent to do this task here.

So the sub agent can then spend lots of tokens doing the task all within

its smart zone, and then it reports a summary of its results back to the

orchestrator agent.

In other words, this is a delegation mechanism.

It's kind of like the orchestrator is the lead developer and it just

pawns off a task to a junior developer to say, explore this repo for me, and

then report back your findings.

The orchestrator can spawn multiple sub agents too.

So you can have multiple sub agents doing work in parallel.

And when they're all finished, they report back to the parent

orchestrator.

These sub agents can be spawned with different system prompts and

different models too.

So we can even use a cheaper model for the sub agents.

If it's a relatively simple task like exploration, it's super common to

see Claude Code spawn with Haiku for instance, for exploration, which

is really fast and really high quality.

So this is what sub agents are.

They are a context saving mechanism for the orchestrator agent and

Claude Code uses them extremely aggressively.

So you're going to see them everywhere when you use Claude Code.

Nice work.

And I will see you in the next one.


### 017-AI Coding for Real Engineers p17 017 Codebase Exploration Day 1 Fundamentals

Of all of the constraints that we explored in the previous exercise, the most onerous, the strangest, and the one you have to think about first is the fact that the LLM is stateless.

The statelessness means that the LLM is dropped into your code base every single time with no memory of exploring it before.

This means that every time the LLM needs to get up to speed with the code base and explore it to understand its patterns, understand the way it's laid out and understand even what the code base does.

And this means that exploration is a foundational skill that you need to understand in order to get good with coding agents.

Unfortunately, we have a big old repo here for you to explore.

You should hopefully have had a chance to click around the app a little bit and understand kind of what it's doing at least at a basic level.

But in this exercise, we're going to use Claude to explore the repo for us.

I'm going to start by going into VS Code as we've done before and running Claude.

And I'm going to prompt it by saying, tell me what the tech stack of this repo is and what its intended purpose is.

Now, at this point, I'm going to pause and we are going to see what happens on my machine in the solution.

But I would like you to run the exact same thing inside the project and look out for some different things.

First, I'd like you to know when you think a sub agent is being used.

You might be able to tell this from the user interface.

So see if you can figure it out.

Second, when the LLM responds with a response, query it and ask it some more questions and then see what happens.

By the end of this exercise, I do want you to have a really good understanding of the repo.

So I've given you a bunch of questions that you can ask down below.

Once that's done, head to the solution and I will break down exactly what's happening.

So good luck and I will see you in the solution.


### 018-AI Coding for Real Engineers p18 018 Codebase Exploration Solution

All right, let's kick this off and let's see what happens.

We can see first of all that it's searching for two patterns

and reading six files,

and you can press Control-O to expand here.

If I press Control-O to expand,

I enter a kind of verbose mode

where I can see all of the commands that it's done,

where it's calling the bash commands,

where it's reading certain files,

and it gives me a brief summary of the repo,

including the tech stack here.

I'm going to untoggle this UI here

so we end up with the kind of default.

And what I can see here is that it did not spawn

any subagents.

So in my case, with this model,

with this version of the repo,

with this particular prompt,

it did not spawn any explore subagents.

And what this meant is we didn't actually read

that many files.

We only read six files throughout this.

That's not going to give me a full breakdown

of what's happening in this repo.

So let's go to the bottom here

and prompt it a little bit deeper.

I'm especially curious

about the power purchasing parity implementation.

And when I do this, I'm going to use a special word.

I'm going to use the word explore.

I'm going to say explore how PPP works

in this repo.

And if I kick this off,

we're going to see something really interesting.

Now what we can see here is that now it spawned

an explore subagents.

You see here explore with a kind of title

inside the brackets here.

And this explore is running a bunch

of different tool calls

and it's very aggressively searching for files.

If I press control O to expand here,

we can see, wow, it's reading a lot more files here,

searching for a lot more different things.

And I'll untoggle this to just let it run.

So what happened here under the hood

was that our orchestrator agent,

the one that we're talking to,

spawned an explore subagents

with a customized system prompt

to explore the repo for us.

We can see that inside the subagents context window,

it took 60 seconds to complete its task.

It used 64,000 tokens,

which is about 32% of its context window,

which is pretty gnarly.

That's a lot of tokens burned.

And it called 25 tools here.

So tools can be things like bash commands

or file reads and writes.

And then it came back with a summary

to our parent orchestrator agent

and the orchestrator agent spat out this for us.

This looks like a really in-depth exploration

for how PPP works.

Honestly, almost as good

as if we'd just written it ourself.

And so we notice how powerful that subagent is there

and how important our word choice was.

Here, we use the explore verb,

which kind of connected Claude code

and sort of triggered something in its latent space

to say, okay, I need to use the explore subagents.

Whereas first, in our previous prompt,

we just said, tell me what the tech stack of this repo is.

So that's a good hint when you want

a really in-depth exploration

is to actually use the word explore.

So now you should take the opportunity

to run any more exploration commands

that you want on the repo

to really deepen your understanding,

because soon we're gonna be getting to building features.

Nice work, and I will see you in the next one.


### 019-AI Coding for Real Engineers p19 019 Build A Feature Day 1 Fundamentals

Alright, we've explored the codebase. You understand the vague structure of what's going on.

Now it's time to build our first feature.

We're going to build a course review system where students can leave reviews on courses.

I've chosen this feature because it's fairly meaty.

You need to touch all areas of the codebase, but it's not that intense in terms of user interface.

To give you an idea here, we need to go into the Dev UI, log in as a student.

We are now Emma Wilson and then go to, let's say, Node.js for instance.

The idea would be that we want to be able to leave a review on this page as the user.

We don't want to leave a written review or anything like that. We really just need a star rating.

So the first thing you'll need to do is get Claude running inside VS Code again.

Or if you've got an existing Claude code set up, then run clear to clear the conversation history.

From there, we're going to put together our initial prompt, which is just going to be a couple of sentences about what we want to build.

I've gone for this simple prompt. I would like to create a course review system where students can review courses by leaving a star rating.

We don't want to add written reviews, just star rating.

These reviews will then be visible everywhere that courses are visible.

We want to show the average rating on the courses in the list page and on the course page itself.

Your prompt may look different from mine.

You may want to go further, add more detail or even pull it back and keep it simpler.

Now we're going to pause here, but once you have sent that, then I want you to start steering Claude.

I want you to be watching it closely, see if it spawns an explore sub agent, for instance,

and try to understand everything it's doing as it's going through.

It might start wanting to change files or ask you permissions, which you should be prepared for.

You should also make sure you're running forward slash context to check on your context usage as you're going through.

If you've built features with LLMs before, then this will feel familiar.

But the thing I want you to get out of this is the level of context paranoia that I have when I'm using LLMs.

Remember, around 40% usage of the main orchestrator agent is when we should start getting a bit nervous.

So let yourself be guided by what Claude does.

Just put yourself in a more observational mode, give it a little bit of steering,

but mostly we just want to observe the default behavior of Claude code.

Good luck and I will see you in the solution.


### 020-AI Coding for Real Engineers p20 020 Build A Feature Solution

All right, let's fire this off and see what happens.

We can see it's entered something called plan mode here,

which is fairly self-explanatory,

but we're gonna dive much deeper into that

later in this section.

And we can see it's kicked off

an explore subagents here, beautiful.

Let's check in again once the explore agent has finished.

Okay, it's now finished with the explore phase.

It had quite a meaty explore, which is nice.

It's now reading some key files

in the orchestrator agent.

And now it has come back with a couple of questions.

These are things which obviously were not present

in my initial prompt or not clear from my initial prompt.

I can navigate this by using tab or arrow keys

to navigate up and down.

And the first question it's asking me

should only enrolled students be able

to leave a star rating on a course?

That makes sense to me because only those

who've actually paid for the course

should be able to rate it.

That means that the reviews are gonna be more reliable.

So I'll press return to select this.

What star rating scale should we use?

A one to five stars, that feels most appropriate.

So I press return.

And should the dashboard page also display

average ratings on course cards?

Now I'm not actually sure what's shown

on the dashboard page.

So I'm actually going to ask the LLM here.

So I'm gonna press four and chat about this.

This should let me quit out of the ask questions flow

but it appears that I just seem to have

gone in there again.

So I'm gonna press escape and get out of there.

I'm just going to ask it

what is currently shown on the dashboard?

Give me a list of all of the things

that are shown there so I can work out

whether adding the star ratings would clutter the UI.

So you notice I can kind of kick off another exploration

or it might already have the information in its context.

I'm gonna press return here and just see what it does.

So it's given me a description here of the dashboard code

and what's actually shown there.

I think based on the fact that this seems

like a private dashboard to me,

I'm gonna say to it,

let's not bother with the dashboard page.

Let's only put it on places

where we're intending to sell the course.

So now I press return.

Now that it's got all of the information

from all of the questions that it asked me,

it should be able to come up with a decent plan

that it's then going to put into action.

So as we can see here,

it's kicked off now a plan subagent.

This is another context saving mechanism

where it dives deep into the files again

in order to read through everything,

design a perfect implementation plan

that it's then going to follow.

So let's wait for the plan agent to complete

and see what it produces.

Okay, the plan subagent has now completed

and it's now actually creating a final plan.

So this plan here is pretty meaty

and it is a multi-step plan.

It includes the code that we're probably going to add

to the schema here,

then the rating service

that follows existing service conventions.

When I'm reading these plans,

I generally just read the top level items here,

understanding all the steps are going to be completed.

So it's then going to update the course list page,

update the course detail page.

It's going to touch some files here

and then run some verification steps.

It's also important to check the top of the file too

just to check the kind of top level context here.

Students need a way to rate courses

with a one to five star rating.

Only enrolled students can rate.

Average rating should display on the course list page,

on the course detail page, the dashboard is excluded.

So this looks fine to me.

We can now scroll all the way to the bottom

and we can check out our options here.

We have four main options.

We have to say yes, go ahead and auto accept any edits.

In other words, I trust that this plan looks great.

Just go ahead.

I don't need to approve any file rights here.

Just feel free to write any code that you fancy.

Or we could say yes, go ahead

and I need to still manually approve

any stuff that you write.

Or let's clear the context,

put the plan into context only

and then automatically accept any edits.

Or of course, if I don't like the plan,

then I can type into number four

to tell Claude what to change

and it will update that plan.

So I'm deciding between one and two here.

One would clear the context

but two would just keep the current context

and then just barrel on.

In order to make that decision,

I need to check what current context we're on

because I'm feeling a little bit paranoid

about the context.

I can't exactly recall how to escape from here

but it's either escape, yeah, escape works.

I was gonna try control C if that didn't work.

This lets us quit out into Claude here

and we can run forward slash context

to check out what current context we're on.

And there we go.

We are at 36% context already.

We have a ton of messages in the context

and we're just pushing up

into the kind of bottom of the dumb zone.

We might be able to get away with this

but my context paranoia is starting to creep in.

So I'm gonna go back to where we were

by going down to the prompt and saying,

give me the chance to review the plan again.

This should just open up the UI,

yet here we go where it gives me the option

to clear context or not.

So because we're already pretty high on context,

I'm gonna accept, yes, clear the context

and then automatically accept edits.

So because we've now bumped it back

to only the context that's in the plan,

it reads some of the key files again,

it checks for existing patterns

and actually kicks off another explore agent.

So that's the downside there of clearing the context,

you then have to run the explore agent again

to catch up to where you were,

but it tends to be worth it to avoid the dumb zone.

All right, we are finally at the implementation stage

and it's now started creating a list of tasks for itself

and now it started actually implementing

and it's now referencing the steps in the plan

as it's going.

So it's added the course ratings table to the schema,

it has created the rating service

and it's really starting to cook now

so I'm just gonna let it run

until it reaches a stopping point.

Okay, we are now at a state

where it's done four out of five tasks,

so one is currently in progress

and the one that it's trying to run

is the database migration.

So this is the first time it's asked me

for a permissions thing.

Now database migrations are something

that I always want personal control over

so I'm gonna say yes,

but I'm not gonna give it the license

to always run it automatically.

It's doing the same with the dbmigrate command as well

to apply the database migration to my local database

and I'm gonna say yes, go for it.

Now I've hit a slight error in my local setup

where it needs to run like a manual SQLite 3 command.

SQLite 3 has not been found

and so I'm sort of walking through some steps

with the LLM here to actually just try

to fix my local setup.

We can see that here it's trying to run

an arbitrary script in order to get this fixed

and the interesting keeping this video relatively short,

I'm gonna skip over this fix

until I actually manage to get it sorted.

All right, that is now fixed

and it's now asking me whether I want to run

the database seed command,

so seed this nice fresh database.

Okay, and after a couple more permissions checks,

it is now complete.

If you ran into any issues with the setup

or with the LLM there,

then please go and ping in the Discord,

but hopefully the model that you're using

was smart enough that it was able

to navigate around them.

So now let's check our context one more time

just to see where we're at.

Nice, so we ended up on 32% usage.

That's good, that's nice and comfortably

within the smart zone.

So it was worth clearing out all that early context

so that our implementation stayed within the smart zone.

Nice.

So I'm gonna open up a separate terminal here

inside VS Code and I'm going to run

pnpm dev inside of it.

And when I go there,

I can see that if I log in as Emma Wilson here

and I check out some courses,

the ones that I'm enrolled in here,

then just under your progress here,

I'm able to rate this course.

Nice.

And now that my rating has been saved,

we can see it on this course up here.

If I change it to a three, for instance,

then it's gonna change on the global course straight away.

That's quite nice.

And if I switch now to Olivia Martinez,

who also has access to this course

and I give it a five star rating,

we can see up here it changes to 4.5 as the average.

So that to me is looking pretty good for a first pass.

What I'd now like you to do is go back to Claude

and just type in commit here.

This is gonna get Claude Code

to add the relevant files to staging

and then commit your code.

And we can see here it's asked for permission

to write a commit message

and I think yes, that looks good.

All right, so we have built our first feature

with Claude Code.

What I want you to do right now

is to open up a notes app

and write down anything that you noticed

about your session with Claude Code.

Write down any unresolved questions that you have

such as what is plan mode, for instance.

How do I successfully debug with the agent?

How much should I be reviewing the code?

We're gonna be coming back to these questions

throughout the course

and hopefully we're gonna get you

some good answers for them.

But well done.

This was a long solution video, a long exercise.

So hopefully the ones after this

should be a bit easier

now we've built the foundations.

Nice work and I will see you in the next one.


### 021-AI Coding for Real Engineers p21 021 Non Determinism Day 1 Fundamentals

I want to take a quick detour and talk about what you might expect from the outputs of your

agents you're using during this course.

Now when I ran this course the first time, the exercise we've just done is actually

the most talked about exercise.

So many folks were saying, why didn't my agents do the thing that yours did?

Surely given the same inputs, the same code base, I repeated your steps exactly,

surely it would act exactly the same.

And I want to hammer this idea into your head that agents are non-deterministic.

Agents are essentially next token machines, or rather LLMs are next token chooser machines.

And what they do is they choose their next token based on a set of a little bit of

probabilities.

It's not the same every single time.

This means that you can ask the same question to the LLM twice and it will give

you two different answers.

In other words, the responses that you're going to get from your agent at any point

in time are going to be somewhere on a curve, on a probability distribution.

Some of the answers you're going to get are really good and some of them mostly

will group towards the middle, the most sort of sensible route, but sometimes you

will get weird responses, weird little outliers.

When I first taught this course I taught it to around 2,500 students and a couple

of them had really strange experiences on some exercises where it was doing something

completely different to what I was showing.

What I'm here to say is this is a normal part of working with agents.

The non-determinism is baked in.

So what you have to do is ride the wave.

You can definitely make agents more consistent, especially when we get to the AFK phase,

when we start talking about feedback loops, but you will always get a little bit of

this behaviour where it just sometimes does something odd.

So hopefully that sets your expectations for the rest of the course and for working

with agents in general.

Nice work and I will see you in the next one.


### 022-AI Coding for Real Engineers p22 022 Showing Context In The Status Line Day 1 Fundamentals

One thing that drives me crazy about Claude Code's default UI is how hard it is to monitor the context usage as you're using Claude Code.

If you look at other tools in the space like Cursor or OpenCode, they're really, really clear about what your context percentage usage is at any time.

And so that makes it really simple to stay in the smart zone because you're able to see when you're going over 40 percent.

In the previous exercise, we had to exit out of plan mode, get out of our flow in order to run forward slash context in order to see it.

It was just gross. But fortunately, Claude Code gives us the ability to customize what we see in our UI via a status line.

And I'm going to be showing you how to use a community package in order to get the context window usage in your viewpoint at all times.

So just like me, you can max out on context window paranoia.

The first thing I'd like you to do is to clear your context window with forward slash clear here and then use shift tab to cycle between all of the different modes until you just reach the default mode.

So again, shift tab, just tapping between all of these different modes until you see the kind of like question mark for shortcuts button.

Now, what I'd like you to do is go to the page below where there should be a copy as markdown button.

And I'd like you to copy the entire article below into your clipboard so you can paste it into Claude Code.

Once you paste it in, you should see something like this.

Paste a text number one with 80 lines.

There might be more or less if I've edited the instructions since.

Next, you can go ahead and just press return here and then it will begin walking through the instructions in the article to set up this package for you.

This will set this up inside your global Claude installation, not inside the project, but inside your global Claude directory where you have your personal user settings, not the ones for your project.

I'm going to accept this first command where it's making a directory and then I'm going to allow it to read from dot Claude during this session.

Dot Claude is where my user settings for Claude are stored, so I'm going to allow it to do that.

It's now asking to make an edit from inside VS Code up here to add a status line part to the settings dot JSON up here.

This looks good to me, so I'm going to press save here and that should allow the diff.

It then went through and wrote a CC status line settings dot JSON to.

And actually, even before I've restarted Claude Code, I can see there is now a context window usage down here just below my prompt.

But just because the instructions tell me to, I'm going to cancel out of that, press control C twice to exit.

Now I'll open up a new session here just by typing Claude, and I should see that my context window starts at 0.0 percent.

Since I recorded this video on status lines, Anthropic announced a one million context window for Opus 4.6 and Sonnet 4.6, which means our previous reliance on percentages just isn't quite right anymore.

So instead of showing the percentage, I've now changed the instructions below so that they show this.

They show the raw token count here, followed by the percentage in dimmed little brackets there.

This is annoying because, like for the rest of the course, you're going to see me using percentages in the videos, but instead you will have this little display down there.

For your SmartZone dumbZone calculations, you should start getting worried when this number reaches about 80,000 to 100,000 tokens.

And if you want to do some mental maths to figure out exactly what I'm on in the video, then remember that I recorded it with a 200k token limit.

So for me, 40 percent is around 80k tokens.

So this context window number will update as we go through sessions and will allow you to keep a really, really close eye on what is happening inside your context window at any time.

If you had any issues with the setup, then please go to the Discord to figure out how to solve them.

Nice work, and I'll see you in the next one.


### 023-AI Coding for Real Engineers p23 023 Why Plan Mode Sucks Day 1 Fundamentals

Okay, now that we've understood how our agent behaves under normal conditions,

let's start imposing some practices on it.

And I want to talk about one specific mode that you can enter

that I used to recommend but I no longer recommend.

Most agents now ship with something called Plan Mode,

which we can access by shift-tabbing to Plan Mode here.

This is in Claude Code, this is in Codex,

this is you can build your own version in Pi.

This is everywhere in agents.

And the point of Plan Mode is that you create a plan before you go into implementation.

We even saw this in the previous video where it automatically went into Plan Mode

because it was detecting that I'd made a plan.

Now if we think about what the default mode is,

what I'm going to call Implement Mode,

you have essentially four buckets of things that the agent can do.

It can write files, it can read files,

it can run bash scripts, and it can call MCP servers.

If you don't know what MCP servers are, don't worry, we'll touch on those later.

But Plan Mode essentially drops the ability to write files

and discourages the agent from doing any kind of active changes to the code base.

So you end up with just the ability to read files,

run some bash scripts, and listen to MCP servers but not really make any changes.

Now the concept of planning is a very, very good one.

First of all, talking out the thing that you're building with an agent

will really, really help in understanding what you're building

and also help align you with the agent.

Not only that, but having a deliberate step to plan before you go into implementation

will help with exploration because it's a specific moment

that the agent needs to go and explore the repo,

gather all the needed context so that it can then implement properly.

So once you and the agent have figured out what you want to build,

and once it's gone and explored the repo, it then builds an implementation plan.

This plan is saved as a markdown document, usually inside the repo,

and it can then use that plan to go and implement.

It will often even ask you, do you want to clear the context

before going ahead and implementing the plan?

So much does it trust the plan that it's created.

So we can think of their inside plan mode as ideally being three phases.

You initially prompt the LLM with what you might want to build.

The agent goes and explores the repo.

It then interviews you about what you want to build and then creates this plan.

However, in my experience, this interview phase is often extremely truncated.

In many of my plan mode sessions, the agent will explore,

kind of maybe ask one question, let's say, or a couple of questions,

and then go straight into creating a plan.

You then need to review this entire wall of text

in order to figure out if you and the agent are aligned.

And this can be extremely frustrating, and it's very easy to just skip over things

in the plan and not realise that you and the agent are totally misaligned

and aiming in different directions.

And so you will inevitably hit this very common failure mode

where the agent didn't do what you wanted.

Maybe the implementation it created was totally different from how you imagined.

Maybe the feature doesn't behave how you imagined.

Maybe it got some tiny details wrong,

but those tiny details have a massive knock-on effect over the whole thing.

In Frederick P. Brooks, the design of design, he talks about this misalignment

and he describes it as lacking a shared design concept.

A design concept is not an asset, it's not a plan.

It's the ephemeral thing being shared between all participants of the design.

And when you're working with AI, you and the AI are collaborators

and there's a communication gap there.

And so you need to establish a shared design concept

before you go to implementation.

And so the failure mode that I so often see with plan mode

and why I don't recommend it anymore is because it skips the entire stage

where you establish a design concept.

It simply explores, creates a plan which the user is forced to review

and you don't know whether you're aligned or not.

The process that I now recommend looks something like this

where you explore the repo, you interview,

and that interview can often take a while,

and then you go ahead and implement.

The focus is on this interview because it's in the interview I've found

that it's the best place to get the shared design concept really solid.

What this looks like in practice is I have designed a skill

called GrillMe.

And GrillMe relentlessly interviews you until you reach a shared understanding

and until you're ready to implement.

GrillMe is fantastic because it's still planning.

It's just not so eager to directly create an asset.

It really sits with you and forces you to think about the thing

that you're building to not only make sure that you're aligned with the agent

but also that you've thought about all the unknown unknowns

that you can during the planning process.

And the thing that GrillMe does is it fills up the context window

with that conversation.

Really valuable intent from the user that you can either turn into a spec,

let's say, as we'll touch on later,

or you can directly go to implement.

Pretty much every single one of my coding sessions

and also a lot of my non-coding sessions start with a GrillMe.

And in the next exercise, we're going to look at how to use it.

Nice work and I will see you in the next one.


### 024-AI Coding for Real Engineers p24 024 The Grill Execute Clear Loop Day 1 Fundamentals

So at this point you are probably itching to try GrillMe, so I won't stand in your way.

Let's get started.

We're going to use GrillMe to build a lesson comments feature where students can comment

on the lessons.

I've deliberately left this pretty vague so that you will have to spend some time

with the agent to figure out what this looks like.

Are instructors able to comment?

Are they able to moderate?

Are they able to delete or hide comments?

Can students see other people's comments?

Are comments visible to anyone looking at the course or are they only visible to other

students?

You get the idea.

But what you're going to do is kick off a new Claude code session.

You're not going to use plan mode.

You're going to toggle probably to not accept edits on yet.

Certainly not auto mode.

I think just the default mode will be fine.

And then you'll be able to invoke the GrillMe skill here, which I have added to

the repo under .ClaudeSkills, GrillMeSkill.md up here.

We can give it a read just for now.

This is all the skill is.

It's incredibly, incredibly simple.

Interview me relentlessly about every aspect of this plan until we reach a shared understanding.

Walk down each branch of the design tree, resolving dependencies between decisions one

by one.

For each question, provide your recommended answer.

Ask the questions one at a time.

And if a question can be answered by exploring the code base, explore the code

base instead.

This means it's not going to ask you any erroneous questions that it could go

and check itself.

We're using the explore verb, so it should go out and actually do some exploration.

It's going to give us recommended answers as well, which is so convenient.

Oh, I just can't wait for you to try it.

I want you to treat this lesson like a sandbox you were just messing about with

GrillMe.

It will take a little while for you to reach a shared understanding.

And at some point, you'll be able to say, OK, we're ready to implement.

Let's freaking go.

Write down any observations that you have, write down any notes, write down any ways

that you think you might improve this skill.

And I will see you in the solution.

Good luck.


### 025-AI Coding for Real Engineers p25 025 The Grill Execute Clear Loop solution

Okay, I'm gonna start by providing a prompt to Grillme.

I'm gonna say, I want to add a lesson comments feature.

I'm not entirely sure of the scope,

but I want to make sure we reach a V1 pretty quickly.

And so I want to see something working.

The minimum is, I definitely want students

to be able to comment on lessons

and have instructors also comment on those lessons.

That seems fine to me.

Let's see what Grillme does with this information.

Okay, it's done a teeny exploration here.

It's found a quick layer of the land.

It's a React Router course app with students,

instructors, admins, per lesson routes, et cetera.

So for V1, the most foundational branch

I want to resolve first is who can see and write comments.

So here we go.

We've got Q1, who can post

and who can read comments on a lesson.

So already we're being forced to interrogate our design

and think about it.

It's given a recommendation, only enrolled students

and the course instructor can post and read.

Comment to scope to one lesson

and only visible to people with access to that lesson.

That looks good to me.

I'm gonna say correct.

This is my favorite response to Grillme

because it's just accepting its recommendation.

Okay, it's now asking about the threading model.

This is something we had not considered going into this.

Should we have like pure, like fully nested threads,

kind of like Twitter style?

Should we have just a flat list

with optional one level reply

or should we just go to pure flat?

This is interesting because when I'm thinking

about this, I'm thinking,

what's like an irreversible decision here?

Like one way we could get this wrong

is we could make too complex an implementation

that we end up not needing.

As it says, sort of fully nested

is probably overkill for version one.

So I'm interrogating myself here

and I think I'm gonna ask a follow-up question.

What do you think is a version of this

that would be hard to row back from?

Like fully nested might be overkill,

but maybe we can always go from pure flat

to one level replies later, right?

So let's submit that.

I'm doing this because what I see

a lot of people doing with the grill me skill

is just literally answering the questions like A, B, C

and not trying to drive the conversation themselves.

This is an interview, sure,

but you're also able to drive the conversation

from your side.

So it's giving us now a reversibility ranking.

Yeah, we can always go from a flat list

to one level list pretty early on.

We can always go to one level to fully nested,

also easy, but fully nested to anything simple is hard.

You'd have data whose meaning depends on depth

and collapsing it loses information, right?

So pure flat is the most reversible starting point.

So it's changing its recommendation to just pure flat

and I agree.

Correct.

It's now asking about the content format,

which is a really important detail here.

It's recommending plain text plus auto link.

I agree.

Correct.

We don't want a rich text, whizzy wig for version one.

We could do markdown, I suppose,

but plain text and auto link seems to make sense to me.

It's now asking about editing and deleting comments.

So yes.

Okay, there's lots here, right?

So the author can delete their own comments.

Instructors can delete any on their courses,

lessons, no editing on V1.

Hard delete versus soft delete.

I think we go for a reversible choice.

So soft delete is so threads don't lose context.

Deleted comments render as deleted placeholder.

That makes sense.

So if in future we need to thread off those,

although we're not doing threads, right?

We're just doing a flat list.

I think for version one here,

we should go with delete only, soft delete, no edit.

So yeah, follow its recommendation.

I'm gonna say correct.

One thing you might've noticed

about the grill me session here

is how little we have to focus on at a time.

Having just one question to deal with

means that our focus just shifts from question to question

and we resolve it in line.

If we had to just like do this in one big chunk,

in let's say a plan asset,

we would probably get pretty lazy

or we would deprioritize some of those.

But taking the time to think through each decision

is absolutely crucial

and means we're gonna get a really good alignment

in the output, I hope.

It's now asking where do comments live on the lesson page

and it's recommending a discussion section

appended below the lesson content quiz.

Absolutely, yep, hey, makes sense.

It's asking sort order for comments.

Yes, it should read like a thread.

Absolutely, we don't want newest first or oldest first.

Yes, absolutely.

It's asking a little bit of front end stuff now.

So visual distinction for instructor comments.

Should we have an instructor badge

next to the instructor's name?

Absolutely, yes, sounds good.

Again, these questions are often super easy to answer,

but like, you know, we're just seeing it come to life

really in our minds before we see it on the page.

It's asking about pagination.

So how many we want to see on the page at once?

I think load all is fine for V1.

Yeah, notifications when someone replies or comments.

This is something we will need to do eventually,

but it's definitely out of scope for now.

So no notifications recommended.

Yeah, seems fine to me.

Again, really great detail here.

It's asking about character limit per comment.

I'm fine with 2000 characters, that seems fine.

And it's now asking about moderation.

So this is something that we thought about

initially when we were designing the prompt.

And it's asking reporting admin deletes

or rate limiting.

I think it's, what's it recommending?

It's recommending to defer all of it for V1,

but I think I do want the ability for admins to delete.

So I think I'm gonna go for B here.

I'm gonna disagree with the recommendation

because admin's deleting stuff.

That just makes sense to me.

It just makes sense.

Why wouldn't you do that?

You know, it's just an extra little check

and admin's not being able to do something

feels super awkward.

All right, pals, we have done it.

Beautiful.

Resolve the consequential branches.

Here is the V1 spec.

It's just kind of giving us a really, really light plan

here based on everything that we've covered.

I generally don't review these

because I know that we've reached

a shared design concept now.

I can see the thing in my mind,

probably if you're following along, you can do the same.

And I have a feeling that what we're gonna get out of this

is gonna be good.

So yeah, it's recommending that I say ship it.

I'm gonna put it in accept edits on mode

by pressing shift tab, and I'm gonna say implement.

I feel pretty confident doing this

because we've only hit 40K tokens here.

So we're still comfortably in the smart zone.

And this means that I'm pretty sure

we're gonna get a good implementation here.

It's worth saying again, at this point,

you probably received different questions from me.

It probably took you in a whole different loop.

It may have, or you may have chosen different things

from me, that's absolutely fine.

But what you should have seen is had some kind

of grilling session with the agent.

And hopefully before you got to implementation,

you had a decent understanding

of what you were building in your head.

Okay, we can see it's added lesson comments

into the DB schema.

It's asked me to run db-generate,

and it's asking me to run db-migrate as well,

which is nice.

So it's migrating the database for me.

It's adding the comments table and the drizzle migration.

It looks like it hit an error for some reason.

Maybe it hasn't.

Okay, so the drizzle migration is complete.

We're looking good.

It's now implementing the comment service.

So we've hit around 60K tokens here.

It's now writing some tests to cover all that stuff.

It's looking at an existing one, very nice.

Okay, this is a decent chunk of work

that it's doing now.

We're onto the UI and we've got about 78K tokens

in the bank.

We're heading up to the sort of dumb zone section,

but I still think we're smart zoning,

so I think we're okay.

And it's now running the type checks,

and hopefully it's going to be running the tests now

to make sure everything is good.

Okay, all the tests are passing.

It's completed all of its tasks.

The type check is clean.

We are in a great spot,

and it's given us the summary.

So now we can go ahead and QA.

So I'm gonna click this dev UI in the bottom corner.

I'm gonna log in as Emma Wilson.

Then I'm going to Emma Wilson's dashboard.

She's got two courses.

Let's go to the Node.js course.

Let's go to, I don't know, setting up Express.

And we have a little discussion area here.

So we can say, hey, like this, post the comment.

And then we have Emma Wilson saying, hey.

If we take a look at this course, who's the instructor?

It is Marcus Johnson.

Let's go into dev UI.

Let's log in as Marcus Johnson.

Let's go back to where Emma Wilson's comment was,

and let's leave another comment.

We can see that when we're logged in as the instructor,

we have the ability to delete comments,

or we can say, wow, like this, post another comment.

It appears below it.

So we can delete comments with the instructor tag.

One second ago, we can delete our own comments.

We can delete Emma Wilson's comments.

Let's see what happens when we switch to James Park.

James Park doesn't have access to this course,

so he does not see the comments.

Does Olivia?

Yeah, Olivia does.

And Olivia should not have the ability to delete.

Fantastic, brilliant.

Let's just check that deletion works.

I'll go and go in as Marcus Johnson, like this.

Yeah, there we go.

It shows as deleted.

Then we can delete Emma Wilson's comment.

Beautiful.

So rather wonderfully,

we have a perfectly aligned implementation

to what we planned.

We didn't have to do any steering during implementation

because it was all nicely aligned

to the grilling session that we had.

We didn't even create an asset.

We didn't even create a plan.

We just had a conversation

and then produced an implementation.

Amazing.

So that is the Grill Me workflow,

and we're gonna be deepening this

and developing this throughout this course.

If you really fancy taking this lesson to the next level,

you could go back,

redo this entire lesson with plan mode,

and see if you have any different experience.

But overall, nice work,

and I'll see you in the next one.


### 026-AI Coding for Real Engineers p26 026 Compaction Day 1 Fundamentals

Throughout this course so far, I've been leaving something unexplained and it's time to open the lid and see what's actually in the box.

I want to talk about what happens when your context window goes all the way into the dumb zone and actually goes all the way up to the context limit.

In other words, you start your session in the smart zone, you do a good job in the smart zone, but let's just say you carry on, carry on, carry on through the dumb zone.

What actually happens when you reach the end of the context window?

In other words, you have spent 200,000 tokens in a single session. What is going to happen then?

Well, we can examine this by running Claude and inside our project, of course, and we can do a context command here.

Now, this context command shows the context usage that we have here. Currently sitting at 7%.

Very nice. But right at the end of the context, we can see an auto compact buffer here.

So this is 33k tokens. So 16.5% of the context is reserved as an auto compact buffer.

Now, this is not being used by the context window, so it's not affecting the LLM.

There's no tokens actually being put here. It's basically a stopgap.

In other words, when we cross into the auto compact region here, it's going to automatically run something called compact.

What is compact, you may ask? Well, let me show you what it does.

So I've gone back to a previous session here where we had used 49% of the context window.

In this session, we implemented the lesson comments table here.

We added the comment service. We added a lesson page, add and delete comment actions, and we had comment section, comment card components.

Now, let's imagine for a second that I wanted to carry on this session and give it some feedback on its implementation.

49% feels a little bit freaky deaky here, so I might be tempted to clear the context.

But clearing the context would mean I would need to explore the entire repo again.

I would lose all of this nice context of what was actually implemented.

My context window kind of looks like this at the moment where I have this nice watch of good context.

I just want to fit it into a smaller space so that I can do some work in the smart zone.

This is what compacting in theory does.

It takes a large watch of context here with a bunch of repeated tool calls, with maybe some stuff that doesn't really need to be there.

And it just gives you a summary of what the most useful stuff is.

And crucially, it uses an LLM to do this.

So this process of reducing the large context into a small context does cost you tokens.

But of course, exploring the repo again would also cost you tokens.

So I'm going to try this out by going into the Claw Code session and running compact here.

I now get the option to pass in custom summarization instructions.

This allows me to pass some information and maybe some guidance to the LLM that's doing the summarization.

And I tend to use this to tell the LLM why I'm compacting.

In other words, what I'm about to do after I compact.

So for this one, I'm going to say I've just implemented a feature and I want to do some QA on it.

That really is it. That's all the LLM needs in order to do a better job, I've found.

So let's actually run this and see what happens.

We can see a compacting conversation thing comes up.

This does usually take a fair chunk of time, maybe a minute, maybe two minutes, depending on the size of the conversation.

OK, and we can see it is now compacted.

There's a little bug here where it still shows the original context in the status line there.

So this is deceiving.

But we can see it also gives us a little printed summary here.

It keeps some of the main files in context.

So it keeps apps roots in context, keeps this lesson dot lesson ID in context.

It keeps references to some files as well.

So this file is not in context, but it's still referenced.

And it's also got the plan file referenced as well.

So it knows that the plan file is there.

We can also press control zero to see the full summary here.

So here we go. This is the full summary of everything that was in the conversation,

along with the files and the references above.

This is all the LLM has in its context.

And we can see it's simply a markdown file here.

So you see how little remains here.

I mean, like there really isn't that much.

It's just a set of bullet points and some code samples saying what was in the conversation.

We can see it preserves all the user messages here.

So anything that we might have said, I suppose.

And we can also see that there's a pending task to QA the feature.

The user's additional instruction says I've just implemented a feature and I want to do QA on it.

So there's our intention being preserved in the compacted conversation.

This is nice too. It also preserves the full transcript in a file.

So if it needs to reference anything that was said in the previous transcript,

it has a reference to it.

We can then exit out of here by pressing control O again.

And I'm just going to show you what's in the context by running forward slash context.

We zoom up to the top here.

We can see we are now at 12% tokens.

So we've compacted all that big conversation into just 23k tokens.

So this is what compacting does.

And this is what would happen if you were to hit the auto-compact buffer.

So a natural question becomes, why do we bother clearing the context at all?

Why not just allow the context to grow until we hit the auto-compact buffer,

then we zoom down again, zoom up again, zoom down again,

and just keep on going like this?

Well, the reason is that every time you hit the auto-compact buffer

and you go back and you compact,

it leaves what I like to think of as a little sediment inside the context.

When you then go up again and you hit the auto-compact buffer again,

you leave another little piece of sediment.

And these layer up and up and up,

and they affect the output in unpredictable ways.

Whenever you start a session with an agent

that has some of this sort of sediment in its context,

it means that it's in a different state from the way you usually work with it.

Whereas if you optimize your workflow to work with an agent

that always has nothing in its context,

then you find you end up with more predictable outputs each time.

Not only that, but you spend fewer tokens, of course,

because you're not spending tokens on compacting.

You're spending more time in the smart zone

because you've got more smart zone to work with

and less time in the dumb zone.

So your code quality outputs tend to be higher.

I have to caveat this with this is my mental model

and this is what I have found best results with.

In other words, this is my opinion.

It also happens to be the view of lots of people in the community as well.

So this is kind of an agreed upon idea.

However, there are prominent people that say you should just, you know,

continue working and just hit the auto-compact buffer

and not have to worry about context ever.

So the question then becomes when should you compact?

I find myself compacting relatively rarely.

It tends to be in cases like we discussed,

where I have just finished a large session

and I just want to add some extra feedback on top.

I've also found this really useful when debugging

or trying to solve a complex error.

For instance, you fill up your context window

with things that you've tried

and you don't want to lose them by clearing the context

and just going back to nothing.

So you compact, you say to the LLM,

okay, we tried these things, let's now try some more.

But you should notice that the times that I'm using compact

are times where I'm working with the LLM directly.

Our end goal with this course is to get to a place

where you should not need to touch the LLM,

it should be working relatively autonomously.

And so relying on compact for your workflows

means that you're also relying on you being there

to tell the LLM when to compact,

which of course is useful,

but not quite where we're going in this course.

So that's what compacting is.

It's a Claude code mechanism for essentially making sure

you can have an infinite conversation with Claude

if you want to.

Compacting multiple times over a conversation

is considered an anti-pattern by me

and lots of people in the community,

because you build up these horrible little gunky layers

of sediment in your context

from maybe unrelated conversations.

And what you should be optimizing for is a clean context,

not one that has a bunch of memories already in it.

When I do compact, it's usually only once per conversation

and it's usually only in cases where I'm working

on a difficult, long running task.

I want to stay in the smart zone

and just give it a bit of extra feedback.

In general, I organize my setup and my harness

and all the things I use with Claude code

to make sure I never have to compact.

And when I do compact,

I usually feel bad about it afterwards.

However, this is just my opinion

and you may find different results

and they may even improve compacting in the future

to the point where I actually like it and use it again.

Nice work and I'll see you in the next one.


### 027-AI Coding for Real Engineers p27 027 Handing Off Day 1 Fundamentals

In the previous lesson we talked about compacting and specifically the dangers of auto-compacting

where you pull in a bunch of context just to shrink it down again to create another

little layer of sediment that keeps growing and growing and growing.

Now the way to avoid this of course is just to clear the context every time so you

start with a fresh session.

But what happens in situations where you're halfway through a session, let's say, and

you think of an idea that you want to do.

Let's say you discover a file which needs a little bit of updating or a test that

needs fixing. You could do this in your current session of course but you don't

quite know how long it'll take and it might take so long that you don't have

any budget left to do the thing that you wanted to do in the first place.

It doesn't really make sense to clear the context in this situation because

you still need to complete the blue task here. It's just this little yellow

task also needs to be done at some point. And in fact this little yellow

task really just needs its own context window to complete. It doesn't

even need all of the context with the blue. It's just we happen to

discover it during this little blue session here. So what would be great is

if we could just take this blue session here and compact it into another

context window. Because then the blue could feel free to grow in its own

context window and this little yellow task over here, the bug fix or the

test fix, could just complete in its own context window. So I've been

messing about with this idea for a while and initially I thought this

needs to be called Compact to File but then I came up with a slightly

snappier name, Handoff. Handoff allows you to create a temporary

markdown file that you can use for handing off between agents. And it's

really really handy in a few different situations which we're going to talk

about. First let's take a little look at the skill itself. What the skill

says is write a Handoff document summarizing the current conversation so

a fresh agent can continue the work. We're saving it to a path produced

by make temp t Handoff xxxxx. In other words it's creating a file in

your temporary directory. Crucially it then says suggest the skills to be

used if any by the next session. So if you're doing a grill me then it

will suggest to continue doing a grill me. Don't duplicate content already

captured in other artifacts. This means that it will just add links to

other artifacts if there's important stuff inside them. And then if the

user passed any instructions treat them as a description of what the

next session will focus on and tailor the doc accordingly. This is

really important because the Handoff document will be tailored to what the

next session will be used for. For instance if we found a broken test

during our implementation of something else during the implementation session

we could say Handoff let's do a separate session to fix that test. That

would then generate a file like this which we could just then pass into a

new Claude session. This can also be super useful in planning. Let's say

you're doing a grill me session that gets a little bit long here and you

think oh there's like a really specific part of this that I need to

grill. So you could hand off to a new session that just grills about

that specific thing maybe even builds a prototype burns a ton of context

even does some research. And then once you've done that big session you can

then hand off back to the original session just by condensing everything

you learned into a little handoff doc. Overall handoff just allows these

obscenely powerful flows where you're expanding and then contracting

making these documents that you pass back and forth. And I wanted to give

it to you as an example of what you should do if a grilling session

goes out into the dumb zone and we'll be revisiting handoff patterns

as we work throughout the course. Take a moment now to just review the

skill and if you feel yourself throughout the course running out of

context window then consider it as a nice option to just hand off to a new

context window to fix a bug or just to continue working on the same thing.

Nice work and I will see you in the next one.


### 028-AI Coding for Real Engineers p28 028 What Is An Agents MD File Day 2 Steering

In one of the early lessons of this course, I talked about how LLMs just forget everything as soon as you clear the context.

And immediately you probably ended up thinking, okay, that sounds terrible.

That sounds awful constraint because I have preferences that I want to be able to teach my LLM or I have certain ways of working or certain patterns that the LLM maybe is not very good at by default.

It's going to be absolutely brutal to tell the agent every single time about what my preferences are before it goes and does its work.

It would be great if there was some kind of memory mechanism for Claude code, some way that Claude code could learn my preferences or at least my repose preferences over time and then use that to better improve its output.

Fortunately, there are multiple ways to solve this problem, both supported by Claude code and some supported by the community.

And in this section, we're going to walk through how to use these to the best of your ability and which ones to pick.

The first one we're going to look at is agents dot MD, which is a simple open format for guiding coding agents.

You can think of agents dot MD as a readme for agents, a dedicated, predictable place to provide the context and instructions to help coding agents work on your project.

The appeal of agents dot MD is how many places it is supported by or rather how many tools use it.

Gemini, CLI, Devin, Codex, cursor.

The very notable exception here is actually Claude code.

Claude code doesn't use agents dot MD and doesn't recognize it.

Instead, it writes it as Claude dot MD.

My desperate hope is that Claude code will start supporting agents dot MD because it's just so stupid that it doesn't.

And so because I'm very hopeful and maybe a bit naive, I'm just going to refer to it as agents dot MD, whereas in fact we will be writing Claude dot MD.

What we're going to do first is go into our project and run touch Claude dot MD here just to see how it works.

And we end up with an empty Claude dot MD file in the root of our repository.

I'm going to say to it, always reply to me in pirate language.

And then we're going to save this file and then open up Claude inside my terminal here.

I'll then say to it, hello, how are you doing today?

And when we run this, we can see that it is now replying in pirate language. Wonderful.

So we have successfully steered our coding agent.

There's a really important thing to note here, though.

I didn't at any point opt into this Claude dot MD.

It just was pulled in to the conversation.

In other words, things inside Claude dot MD are global for the entire repository.

This means that no matter what I do in this repo, Claude dot MD will now be responding to me in pirate language.

And so this is the biggest downside with agents dot MD or Claude dot MD.

It is global.

So this means that our Claude dot MD will be included in every conversation that we have with Claude.

I'm going to copy and paste this about a thousand times here until I end up with an enormous file just to show you the impact on the context window.

OK, we now have a 2000 line file where it just says always reply to me in pirate language.

I'm now going to kick off a new Claude code instance to make sure it picks up the changes in my Claude dot MD.

And we can see an error here saying a large Claude dot MD will affect performance.

If I go into my context here by visualizing the current context usage,

we can see that I have burned about 10 percent of my entire context here on this memory file, on the Claude dot MD file.

So everything you put in Claude dot MD costs you tokens.

And I have no joke out there in the wild seen Claude dot MDs that are not this stupid,

but certainly have around 500 lines or 1000 lines of stuff in them.

So my default attitude with Claude dot MD files is paranoia and not wanting to put too much stuff in there,

not only because it's global, but also because it costs you tokens on every single request.

You notice I have quite a lot of paranoia when I come to working with agents.

I think that's relatively healthy.

I especially have paranoia about a specific command that Claude bundles with, which is the init command.

If I run this here, you'll see what it does.

It initializes a new Claude dot MD file by looking at your repository, exploring it and putting some of the code based conventions inside of Claude dot MD file at the root.

We can see it's kicked off and explore sub agent here.

So we'll wait for this to complete.

You can try this too, if you like.

I sort of don't recommend you do it for reasons we'll explain in a minute.

OK, we can now see the edit that it has proposed to make.

And the edit is a pretty large Claude dot MD file.

If we open up Claude again, if we cancel out of it and then run a new Claude session,

we can see by running context just how much this is filling up our context window.

And we should see that the memory file, it's nearly a thousand tokens here that it's created.

Now, that might not sound very much.

That's just sort of 0.4 percent of the context window.

But if you imagine that's on every single request, that is just going to push you closer to the dumb zone and cost you tokens on every request.

And a lot of this stuff is just stuff that it could discover very simply by itself and stuff that will probably go out of date quite quickly, too.

For instance, the stuff inside the package dot JSON here is incredibly easy for it to discover.

Just check the package dot JSON file.

And if you ever change any of these scripts, you'll need to remember to go into Claude dot MD and update this, too.

So for that reason, I really don't recommend you run Claude in it, even though the UI will tell you to a bunch of different times.

It's also worth saying that Claude often actually ignores the stuff inside Claude dot MD.

Claude code injects the following system reminder with your Claude dot MD file in the user message to the agent, which is this context may or may not be relevant to your tasks.

You should not respond to it unless it's highly relevant.

In other words, Claude will just ignore anything inside your Claude dot MD file if it thinks that it's not relevant to its current task.

This, by the way, is from an excellent article from HumanLayer on optimizing your Claude dot MD file, which I'll link below.

So even if you put stuff in there, Claude has the option to just ignore it if it wants to, which means that steering it is not always reliable.

So now you understand a bit more of what Claude dot MD is or what agents dot MD is.

When should you actually use it?

Well, we're going to be getting into this and talking about it a lot more during this section because it's not an easy question to answer.

But anyway, let's summarize.

Essentially, agents dot MD and Claude dot MD are the same thing, except that Claude code never listens to agents dot MD and will only listen to Claude dot MD files.

Claude dot MD is often ignored, and that's kind of by design because Claude code actually tells the agent or tells the LLM, do not always use this.

And finally, Claude dot MD is global, so it's included on every single request you make to the agent.

So you better make sure that the stuff you put in there is relevant to every single request you're going to make of the agent.

So nice work, folks. I will see you in the next one.


### 029-AI Coding for Real Engineers p29 029 Steering An Agent With The Agents MD File Day 2 Steering

Alright, so we've learned what an agents.md file is, but let's now use it to steer Claude code to build some features.

To save you a bit of time, I've put together a plan that you are going to implement.

In other words, I've gone into plan mode and I've put together a bookmarks feature.

Bookmarks are private to each student, they persist until manually removed, and are inline only, so there's no dedicated bookmarks page.

I'll make this available to you below so that you can copy and paste this directly into Claude, as I'll be doing in a second.

Now we mentioned last time that Claude.md can be used to steer the agent, but what particular patterns do we want to steer it towards or against?

Well, I've added something to my Claude.md that is something that I really hate to see from AI agents.

It says here, when you have a function with more than one parameter with the same type, use an object parameter instead of positional parameters.

In other words, this first one up here is the bad version, where we have an add user to post, where we have user ID as a string and then post ID as a string.

It is very, very easy to call this function with user ID and post ID switched.

And so, in my opinion, it's much better to have an object as the parameter.

So you need to pass an object instead of positional parameters, because then you specifically need to name which one is the user ID and which one is the post ID.

When I was building this dummy repo, I put in lots and lots of these positional parameters in here.

So now in this exercise, there's going to be a funny conflict because the code base is going to be doing mostly this.

But we're telling the agent to do mostly the new good one.

This means that during its explore phase, it's probably going to see a lot of this, but its Claude.md file will be telling it to do something different.

So let's see which one wins.

So to set this up, I'm going to open up a new Claude session here.

I'm going to grab my plan here and I'm going to copy and paste it and then just go and paste it directly into Claude code here.

And it's now kicking off, as it will be for you.

I would like you to sit back and observe what you see from Claude code here.

Is it obeying the Claude.md file or is it obeying the stuff that's in the code base?

And while this goes on, see if you notice any patterns in the code that it creates that you would like to steer against in the Claude.md.

We're really developing an instinct for how to steer the LLM, even if, as we discussed, the Claude.md file is maybe not a perfect place to do the steering.

So best of luck. Follow the steps below if you get stuck and I will see you in the solution.


### 030-AI Coding for Real Engineers p30 030 Steering An Agent With The Agents MD File Solution

Alright, let's walk through what it's done so far. It started by exploring the code base.

In fact, it didn't end up kicking off an explore agent, I suppose, because we'd already done some upfront work

and because this plan was pretty detailed. It then added a bunch of tasks down here

and it's about to start kicking off the plan. So I'm going to press Shift Tab and just allow it to create all edits.

Now I can already see some promising signs here. Ooh, yes, lovely.

Inside Bookmark Service here is if we open it up by going Bookmark Service,

we can see that it's using this opts pattern that it's read inside its Claw.md.

It has a user ID of number and a lesson ID of number here.

And we can really tell it's doing the same thing as in the Claw.md because it's used the same parameter name.

So we had opts inside here, which is just my preferred way of doing it.

And this one has opts as well. We can see too it's actually done this for all of the different functions here.

So isLessonBookmarked and getBookmarkedLessonIDs all have this same pattern.

So I've now been sat here for a while and I've let Clawed code complete all of its work.

It added the schema, the migration, the Bookmark Service and the lesson viewer.

But one extremely important thing it didn't do is it did not add any tests to the Bookmark Service.

This is pretty bizarre to me because there were like there's tests for a bunch of other services inside here,

which is visible only from the file system.

But I suppose because we didn't specify in the plan, then it didn't end up writing any.

This would be a pretty high value instruction to add into a Claw.md file.

So let's actually go through search for Claw.md and add it inside here.

So here's what I'm going to add here.

Anything marked as a service by the name of the file, for instance, AuthTokenService.ts,

should have tests written for them in an accompanying.test.ts file.

This is a really high leverage instruction because it's just a small little hint to the agent that this is a convention that we use.

This is unlikely to rot away or go out of date because it's not actually specifying or naming any named files.

It's just really a piece of jargon in our application that is unlikely to change.

If you've ever worked on a complicated enterprise project, you know how sticky jargon can be.

And I feel confident that the word service will in general mean in this application a tested unit and a tested unit that provides a specific piece of functionality.

OK, now that I've updated this Claw.md file and saved it, I'm going to go back into my Claw.code and I'm going to say review your work with the updated Claw.md in mind.

The reason I'm specifically mentioning this is because if you make updates to Claw.md while Claw.code is running, it won't pick them up until you go into a new session.

I don't want to go into a new session because I want all of the context that we've had before.

I'm just about able to stay within the smart zone for this.

And I just want it to pull in the most up to date version of the file so it understands kind of what has changed and what I'm saying.

There we go. It's picked it up. The updated Claw.md adds a rule. Services must have accompanying dot test dot ts files.

It's looking for existing test patterns and then it's going to write some tests.

All right, now it's writing the bookmark service tests. Nice.

OK, all 10 tests passed. The missing test file from bookmark service dot ts has been added and all services must have accompanying dot test dot ts files.

We've stayed just inside the smart zone and we've successfully done a bit of steering.

Now the LLM will remember both of these rules about the positional parameters and it will remember anything marked as a service must be tested.

I've also just done a bit of QA on the feature and I can see that it is now working too.

So I add a bookmark here, adds a bookmark to the section header and nice. It seems to work too.

So we've successfully built a feature and we've improved the LLM's output potentially for next time.

Nice work and I will see you in the next one.


### 031-AI Coding for Real Engineers p31 031 Progressive Disclosure Day 2 Steering

All right, I've taken the Claw.md file that we had in the last lesson and I have opened it out a little bit more and added a bunch of sediment inside here.

Basically as if a bunch of developers had gone in and added their own ideas into this file.

If you've been using Clawed with a bunch of teammates, then you probably have one that looks a little bit like this.

Now, this is not exactly ideal for reasons that we've kind of already touched on.

We have put a bunch of instructions into the global scope here and not all of these are going to be relevant for every single request that we make of the LLM.

All of these instructions are going to be competing with the instructions that we give it in the prompt, for instance, in the plan.

And if we're only touching front-end code that maybe doesn't have any positional parameters, that doesn't touch any services, maybe we don't even need to do any importing,

maybe we don't need to add a new ID to the database, maybe we don't need to add a new timestamp to the database.

You know, all of these instructions are actually pretty narrow in the kinds of sessions that are going to need them.

I want you to imagine that each one of these instructions is one of these grey blobs in the context window.

Now, it might be that only these little blobs here are actually relevant to front-end code.

It might be that only these instructions are relevant for database code.

And maybe these instructions are the ones that are relevant for React Router.

Now, looking at all of these blobs, isn't it funny that we've got them grouped all into one file?

Wouldn't it make more sense if they were grouped together?

Since a session that needs one piece of React framework advice will probably need more React Router framework advice.

So what if we group them like this instead, where each one was in a separate file all located together and all of the unique ones were in their own file?

And then inside the Claude.md file, you would have just a set of links which linked you to the correct grouping when needed.

So these would simply be separate Markdown files and Claude.md would use Markdown links to link you to the right place.

Now, what we're organically discovering here is a really important concept that's going to recur throughout the rest of this course.

And that idea is progressive disclosure.

Progressive disclosure is actually an idea that comes from UI and UX design.

The idea is that bad UI involves putting all available actions into one huge screen that the user can scroll through and choose from.

If you've ever seen a menu of a bad website where it literally just has a hundred options up at the top in one single flat list, you know what I mean.

Instead, you should reduce the number of choices that the user has to make up front and then allow them to find kind of information based on that small number of choices.

So progressive disclosure of complexity is the name of the game.

Instead of throwing all the complexity out at once, you just sort of give them a map and you allow them to navigate through it.

This Claude.md file chucks all the complexity in at once.

And as this grows bigger and bigger, I would be much more likely to progressively disclose parts of it.

In other words, take it from the Claude.md, put it in separate files that aren't immediately visible to the LLM and then just link it from the information that it does have inside Claude.md.

Now, this concept of progressive disclosure is going to come up again and again and again throughout this course.

It goes into software architecture and code based design and all that stuff.

But in the next couple of sessions, we're going to look at this in the context of steering.

So nice work and I'll see you in the next one.


### 032-AI Coding for Real Engineers p32 032 What Are Agent Skills Day 2 Steering

So we've been talking about agents.md and progressive disclosure,

and we've been kind of like not very kind to agents.md.

It is not great that agents.md just puts everything into the global scope.

That is no fun at all.

So wouldn't it be great if there was a built-in solution accepted by the

community as the right way to do progressive disclosure when you're

steering agents. And that solution is agent skills.

This is an open format accepted across coding agents, including Claude code,

Anthropic were the ones that invented it, but they then gave it away.

It is a simple open format for giving agents new capabilities and expertise.

Agent skills are folders of instructions, scripts, and resources that agents can discover.

The key word there is discover because they are not forced to take this

information in, they're not forced to see it, but it is in a place that

they can easily discover it.

Let's take our example from before to illustrate what we mean.

Before all of these React router style instructions were just forced on

the agent like immediately they were present in its context window.

Same for all of these front end ones and same for all of these database ones.

All of the instructions were right there.

But what if instead we refactored these into their own file and we gave a

little bit of metadata to the agent to say, use this skill when you need

help with the React router framework.

Use this one when you need help writing front end code.

Use this one when you need help writing database or drizzle code.

And so all the agent would see by default would be the name of the skill

and then the description of the skill.

And then if it chose to inside the session, it could basically call the

React router skill and bam, all of the instructions would become available to it.

This is the idea behind skills.

They allow you to progressively disclose instructions and they allow you to

kind of build a user interface for your agent of all the information it

might need to know.

So inside the repo, I've added a couple of example skills.

These are skills that I genuinely found were very useful while I was

building out this application.

If we open up the explorer, we can see them inside .clawed then skills

here, and there are two skills here.

One for a better SQLite 3 rebuild.

And the first one we're going to look at is PNPM not found.

Notice how these skills, just like the Claw.md are inside the project folder.

Just like Claw.md, you can have them inside the project like this, or you

can have them scoped globally to your user.

In my setup, I've got some user scoped skills and some local skills.

Of course, the ones that are scoped to the project are much easier to

share with your teammates as well.

So that's worth thinking about too.

If we click into skill.md here, we can see that it follows a certain pattern.

It has a piece of front matter at the top here, which has the

name and the description.

Just like we mapped out earlier by default, only these things are

available to the agent, so it cannot see the rest of this file inside here.

The description says fix PNPM command not found errors by enabling

corepack, use this when PNPM cannot be found, corepack errors appear,

or the package manager is missing.

It turns out that LLMs really don't know about corepack and maybe you

don't know about corepack either.

But if you encounter errors like PNPM command not found, you can just

literally run corepack enable and then everything will wire itself together.

So this is a perfect thing to put in a skill because I don't want this

in a global claw.md file because the error really only happens very rarely.

But when it does happen, it's really high leverage for the

LLM to know how to fix it.

The other skill that I've got here is this better SQLite 3 rebuild.

Use when seeing errors about better SQLite native module, node module

mismatch was compiled against a different node.js version.

So it's a very clear description of when I want it to invoke this skill.

It's again, very similar to the other PNPM skill that we had there.

It's just trying to fix a relatively rare issue where if it's a node

of module version mismatch, then it should run NPM or PNPM rebuild.

These are perfect use cases for skills because we're just steering

the LLM in the right direction to avoid a rare issue.

Now you may be thinking, if you look at this diagram, how possible is it

to go even further in the progressive disclosure?

Is it possible within the React router skill to have other documents inside

there that might speak to specific weirdnesses with React router?

Could you potentially take the entire React router documentation

and put it inside a skill?

Well, you absolutely could.

For instance, if you wanted to just create an extra little file

inside better SQLite rebuild, perhaps just take this and just

imagine this is like a more complex script than you think, put it

inside script.sh and then you can just have the script in there

and reference it from this file.

The way you reference it is simply by using a markdown link here

that's very, very easy for the LLM to follow.

And so this is a great way of hiding complexity within your skill.

Your skill might want to bundle scripts.

It might even bundle images.

You could bundle anything you can put on the file system inside a skill,

but you don't have to put it inside the proper skill.md file.

So this is why skills are really so exciting because the progressive

disclosure inside them means you can fit really high leverage,

high power things in them and then bundle those up really simply

and share them with any coding agent and your team.

And so skills as a steering mechanism are really, really attractive.

I want to note something interesting finally, which is I think of there

as being two types of skills, skills that you want the LLM to invoke,

such as the ones that we've been looking at here, or skills

that you personally want to invoke.

You can invoke a skill in the same way that you invoke any command inside Claude.

We can actually use the skills command to list all the available skills.

You can see we've got some project skills here and I've got a bunch

of user skills up here and we can press escape to close this.

To invoke a skill, all we've got to do is just, let's say,

use one of these skills here.

So let's say we just invoke the better SQLite rebuild skill.

And I just pressed return here to figure it out.

And it thinks, you know, it's a little bit weird kind of doing it

in this conversation, but it sort of figures out what's going on

and it's going to run PNPM rebuild.

Hello, Edit Matt here.

Before when I was teaching this, I was teaching something inaccurate,

but now I found a better version of it.

Before what I was saying was to turn this into a user invoked skill.

You could actually just omit the name and description and turn it into this.

It turns out that agent skills, if you want to distribute them

and use them in lots of places, then you do actually need

the name and description.

So this is actually an invalid skill here.

Instead, if you don't want Claude to be able to run this skill,

you can specify some extra little front matter here.

You can specify disable model invocation true.

This means that the description won't be available to Claude code.

If you wanted to do the opposite and make it so only the model

could invocate it, then you make it user invocable and you say false.

This means that it won't appear on the list of commands

and only the LLM will be able to invoke it, which actually is kind

of makes sense for this because we never really want to call it

from within a session.

So it turns out the intuition I had about there being user

invocable skills and LLM invocable skills, then, you know,

that is actually something that's supported by the spec.

Very cool.

So that's what agent skills are.

They are a mechanism for steering the LLM using progressive disclosure.

And I think of there as being two groups, either user invoked skills

or LLM invoked skills.

Nice work. And I will see you in the next one.


### 033-AI Coding for Real Engineers p33 033 Using Skills For Steering Day 2 Steering

Now that we understand what skills are, let's actually go and write our own.

Now of course, what's the best way to learn how to write a skill?

It's to use a skill to write a skill.

So I've provided a writer skill skill with which we are going to write a skill.

And the skill we're going to be writing is going to be to take this Claude.md file just inside here

with a bunch of different coding standards inside this and try to organise this in a slightly more sensible way.

Putting everything in Claude.md is not very optimal because it means that every single one of these,

all of this hundred and something lines will be included on every request that we send the model.

And so what I prefer to do is to write a skill to encapsulate this in a coding standards skill.

This will allow us to wrap our coding standards up in a way where it's available if the LLM needs it,

but we're not actively pushing it to the context, which can be pretty wasteful.

So what I recommend you do is follow this process.

We're going to open up Claude and we're going to use the write a skill skill inside here.

We're then going to write a detailed description of what we want.

And what we want is to take all of these entries in Claude.md and find a way to kind of make them more progressively disclosed.

In other words, have sections for various parts of the coding standards,

organise it in a way where it's easy for the LLM to find information,

but we're not going to actively push it into the context.

Once we've done this, we should end up with a really nicely organised setup

and we should be able to delete the stuff that's in Claude.md and maybe just leave a reference to the skill.

I'm going to leave this description up to you.

And the conversation that you have with the agent here is going to be really important for developing your ability to produce skills.

But of course, you'll see what I say in the solution.

So best of luck and I will see you in the solution.


### 034-AI Coding for Real Engineers p34 034 Using Skills For Steering Solutions

Okay, I'm going to start by dictating my ideas into Claude code here.

I would like to take the instructions in Claude.md and create a skill called coding-standards,

which takes all of those disparate instructions and groups them together into different buckets.

For instance, we have some that are more useful for the back end, some that are more useful

for the front end, and I want to create reference documents outside of the skill that

the skill then references. This skill should be used whenever we reference coding standards,

whenever we'll need to conduct a review, and whenever we do implementation. So this should be

front and center of the LLM's mind. Once we've taken all of the stuff out of Claude.md,

we should be able to just delete Claude.md or maybe leave a context pointer from Claude.md to

this skill. Okay, let's take that and run it and see what happens. Okay, it has gone pretty

eager here and it said that it's going to group the rules into five reference files and

create a concise skill.md that points to them. Let's just go nuts here and we'll see what happens.

Okay, it went pretty wild here, so let's take a look at all of the elements it's written.

We can see inside coding standards up at the top here we now have database.md,

so we can see, wow, okay, so all the database coding standards have gone into there.

Front end in UI, there's a few little chunks here. Roots and forms, very, very nice,

looking good. And services and testing. Okay, so this is a lot more organized. This is now

the agent can pull what it needs when it needs to. If we take a look at Claude.md here,

then we just have this tiny little pointer focusing on the coding standards skill.

So it says load that skill before writing code, reviewing changes, or answering questions about

conventions. Skill.md indexes, I think we can delete this. Yeah, because that's kind of

implied just by the fact that we've created the skill. So I think that we're sort of doing

double duty here. We are saying, okay, we have this skill and that skill has a description.

We should probably go look at that description actually. So that's inside the, where is it?

The skills, coding standard skill.md. Here we go, it's quite a large description.

Project coding standards for this React router v7 code base, we could probably just say for

this code base, covers TypeScript conventions, database schema rules, testing. I don't think

we need that sentence either. Use whenever writing a review code in this repo, conducting

a code review or implementing any feature. And I think we can kill that line too. That line

there was read the relevant reference file before producing code. I don't think that's needed.

So now we just read through this skill to make sure it's all aligned with what we wanted.

The skill itself is nice and short. This description will be loaded into the context window

itself. So that will be handy. And the skill just is really just a set of reference files

that then link out to the coding standards. The setup we're creating here is kind of like

a file system where the agent can pull more information as it needs. So the agent sees the

skill description straight away. That skill description can then link to the skill.md

that then can link to the reference files. I call these little links context pointers

because they're pointing to something interesting that the agent might need for its context.

In fact, a more accurate version of this diagram might be this where you have the agent.

It has the skill description already that can link to the code standard skill.md. By adding

an extra little pointer in the claw.md, we kind of get to do double duty because this

little thing in the claw.md will be linking to the skill as well as well as the skill

description. This makes it a little bit more likely that that skill is going to be

picked up because it's got two context pointers pointing to it. And so we can be pretty sure

that our coding standards documentation is going to be used by the agent when it's needed.

And crucially, because we've got all this stuff saved in reference files, if those reference

files grow, it doesn't bloat to the parent's context because it's only using the stuff that

it needs when it needs it. I would recommend using this skill whenever you do any manual

reviews. You can just say, review this code, use the coding standards in this skill. And

overall, this is a great way to build up documentation about what you want your code

base to look like without drowning your claw.md file. This is even something that you could share

across an organization to make sure that everyone is doing the same coding standards

and all the repos mostly look the same. Nice work and I will see you in the next one.


### 035-AI Coding for Real Engineers p35 035 Automatic Memory Day 2 Steering

So far we've been talking about skills, we've been talking about Claude.md,

but we haven't talked about Claude's automatic memory function.

This shipped relatively recently at the time of recording,

and what this does is it actually allows Claude to steer itself over time.

We can discover this file by going into Claude here,

by just running a fresh instance,

and then by using the memory command here.

When we press return on this, we can see that we have user memory,

so this is your user Claude.md.

We have the project memory, which is checked in locally at Claude.md,

and then we also have an open auto memory folder, which we're going to run.

Now I've opened this in VS Code,

and we can see that there are actually no files in this directory.

So on this particular project, Claude isn't adding any extra memory files in.

However, I just ran this for a project that I actually work on for my job,

and on this one it did surface a memory.md file.

So we can see here for this project, it has written its own steering documentation.

It's pretty arcane and specific, honestly.

It has some stuff about using npm install force instead of npm legacy peer depths,

and then it does have some stuff on testing patterns, which appears useful.

Effects use or tests use effect vtest with it.effect.

dbtest use pg-lite, v.mock is hoisted.

So this will be put into the context alongside your Claude.md file.

Now this is still relatively new,

so I don't honestly know how to feel about it yet.

However, I would say that you should probably go in

and check on this file every so often,

just to see that it's not adding some weird crud inside here.

For instance, I don't think my LLM needs the hint about v.mock is hoisted.

I don't think it needs this thing about dbtest use pg-lite.

I think it can figure that out.

And actually, push schema has already been deprecated in my repo,

so I want to get rid of that.

And actually, soon we're going to be moving off Effect Platform Node anyway.

So what I recommend you do is every couple of weeks, maybe,

just check inside this memory.md file and see if there's stuff

that might be conflicting with things that you actually want your LLM to do.

Because the worst thing that could happen is this could just go out of date

with the actual state on your repo.

Which is, by the way, the thing that I always am worried about

when I see these kind of memory style systems.

So there we go. That's Claude's automatic memory,

how to find it and how to edit it.

Nice work, and I'll see you in the next one.


### 036-AI Coding for Real Engineers p36 036 How To Tackle Massive Tasks Day 3 Planning

Now so far in the course you've probably had or been infected by my context window paranoia.

I'm constantly thinking about the context, constantly thinking about the smart and the

dumb zone and with the current generation of LLM capabilities what I advocate for is staying within

the early part of the context window and this is okay for some tasks that can easily fit

into the context window. Small features and bug fixes. Well what happens when you try to do

something much much larger? Something that bursts its way into the dumb zone like the refactor that

we did in the previous section or something where it's just obvious up ahead that you're not

going to be able to fit it into even a context window let alone the smart part of the context

window. In other words what do you do when you're faced with a task that's just too big? Well

the way you do it is the way that devs have been doing it for decades which is you take

the big task and you break it down into small tasks. That way we can do all of the work for

this big task in the smart zone of the context. But the question then becomes what kind of planning

do you need to do to get this to work? Because so far our plans have only been the duration of a

single context window. We've not considered what it might look like to have some kind of

document or set of documents to span multiple context windows. Unfortunately the community has

kind of coalesced around a common set of patterns. Specifically two documents in particular.

The first document we need is some kind of description of the destination, the place that

we're heading. Because if we don't know where we're heading then how on earth are we going

to complete the task? Some people call this the spec, the specification for what we're building

and some people call this a PRD, a product requirements document. I'm using PRD here but

the name here doesn't really matter. Now writing really good PRDs is a really important skill

by itself and we're going to be covering that in this section. Hammering out exactly what

you want to build is super important and it scales to really really big tasks. Or you can

write PRDs for relatively small manageable tasks. And of course this is where you as the human get

to impose your taste on the LLM and get to hammer out exactly what you're building. But

there's a problem. If you only specify the destination here how does the LLM know or how

does your system know how to break it down into small chunks? In other words without a

description of the journey then the LLM might just try to tackle this all in one big context

window. This is why you will often specify a plan.md file next to the PRD. In other words you will

use one session to create the massive destination and then you might use the same session or you

might clear the context and then create the journey as well. You would break down the product

requirements document into a set of phases where you basically say okay in this phase we'll do

phase one, this phase we'll do phase two, phase three, phase four, phase five. And those really

are just the three ingredients in your prompt. You're just saying we're going to do phase N

then we pass in the PRD and we pass in the entire plan. Passing in the whole plan is really

useful because it means that these phases don't step on each other's toes. Because the LLM can

see okay we're doing that bit in phase three I'm not going to do that bit in phase two. So

learning how to build great PRDs, learning how to build great plans and learning how to

construct this prompt and understand how to best navigate your way through these massive

builds that is the topic for today's section. And it is a banger. Good luck I'll see you in the next one.


### 037-AI Coding for Real Engineers p37 037 Write Great PRDs With This Skill Day 3 Planning

Now we understand why we would want to use a PRD.

A PRD is a destination document that helps manage context over multiple sessions

and gives us somewhere to aim at.

And the question immediately springs to mind, how do I go and write one?

Well, it turns out there is a skill for that.

This is the 2PRD skill, which takes the current conversation context and produces a PRD.

The intent here is that you start your session with a grill me session to figure out where you're going.

And then if it's too big to actually implement it in the same context window,

you then call to PRD and you create a product requirements document from it.

It's a very simple two step process.

You explore the repo to understand the current state of the code base

and then use the template below to write a PRD and the PRD gets written locally.

Now this PRD template is something we can fight over.

We can, you know, discuss in the Discord, figure out the exact right shape of this.

I think this is something we're going to be arguing about for years.

But this is what I've got so far.

We essentially have the problem statement,

the problem that the user is facing from their perspective,

then the solution to that problem from again, from the user's perspective,

and then a long numbered list of user stories.

We'll look at this template a little bit more in the solution,

but you can see it's nice and meaty here.

There's enough that anything picking this up will get a really nice sort of injection of information

to complete the implementation.

Now though, we need to test this out.

So what we're actually going to do in this session

is we are going to be creating a new feature.

This feature is an instructor analytics dashboard.

The dashboard for instructors is pretty lame at the moment.

All they've got is like track their learning progress.

We need to give them something so that you can see how many, you know,

users are kind of in their courses, how much they're earning, all that stuff.

They might want to see completion rates or quiz score rates,

and they might want to see which lessons caused a drop off, that kind of thing.

Overall, an analytics page is so huge and bulbous

and could potentially grow into all sorts of different shapes

that I think it's quite a good candidate for a grilling session followed by a PRD

because we need to actually shape it into something reasonable.

So just like our previous grilling session,

we are going to start with a grill me here.

We're going to grill until we reach a shared understanding

or until you feel like you're ready.

And then instead of going to implementation,

we are going to call the to PRD skill instead.

And that should create a PRD for us locally.

When you've finished, when you've actually made the PRD,

jot down any notes that you think about it,

any observations that you had throughout the whole process,

and consider what you might add if you were designing a PRD template yourself.

Overall, you want to see,

does this PRD actually capture our shared design concept?

And remember, we are not yet implementing this PRD.

We're just going to create the PRD and commit.

Nice work, and I will see you in the solution.


### 038-AI Coding for Real Engineers p38 038 Write Great PRDs With This Skill Solution

Okay, let's kick off this grilling session.

I want to build an instructor analytics dashboard

so that instructors have something to look at

on their dashboard.

Instructors need to see various types of metrics.

They need to see how their course is selling.

They need to see completion rates.

They need to see lesson drop-off points.

And any other ideas that you can think of

could be welcome.

Let's kick it off like that

and let's see what it says.

Okay, so it's grilled us on what's the scope here.

Where does the dashboard live?

Analytics consists of three levels

and answer different questions.

Per course analytics or cross course overview.

I was picturing a cross course overview

when I thought about this.

So I'm going to say B for this one.

The theory here is like, which course is my best earner?

That's definitely a question you want to answer.

How is my whole catalog doing?

I kind of just want to see one thing

to see how much I earned from all the many courses

I've put together for Cadence.

So it's now asking to replace or coexist

with the current instructor page.

I was imagining a new analytics route,

mostly because it might kind of outgrow

the current instructor route at least.

And so I think I'm going to say B here

even though it's recommending C as a sort of hybrid thing

because I think now I'm sort of wondering about it.

I think maybe admins need to be able to see

the instructor analytics page

and sort of, because if there's a problem

with the instructor analytics page,

first of all, the admin needs to be able to observe

that and have a look.

And the admin may simply want to drill down

into the instructor to see how they're doing.

So having it just be the instructor page

doesn't seem right to me.

Okay, it's now grilling about the metrics set.

So the three you named sales, completion rate

and lesson drop off, yes.

Then we've got average rating per course.

I agree, that's very high value.

Quiz performance, very high value.

Geographic bank down of sales.

Purchases.country is already captured,

trivial to surface.

I say, hell yeah.

Yeah, it's got a nice recommendation here too.

So tier one plus four rating plus six geo, okay.

I think I'm actually most tempted to pull back here.

And I think I'm gonna say,

this is primarily a revenue focused dashboard

with maybe a bit of rating sprinkled in.

I think geo might spiral out of control

and our IP collection is not terribly reliable.

So I just think focusing on revenue plus ratings

might be the way to go.

An analytics dashboard like this

always turns into a big ball of mud.

Like you're always adding features on top.

So why not start small first?

Here we go, clarification needed before I move on.

Your opening message said instructors need to see

completion rates and lesson drop off.

I think I'm saying to pull back

to just revenue and rating there.

That seems fine to me.

Again, notice how I'm steering the conversation here.

I'm the one in charge, not the agent.

That's pretty important.

This is a nice little thing.

It's actually just checking a schema detail

before asking the next question.

So part of the grill me skills approach here

is that if you, like if it can answer the question

with the code base, it does.

And so that's an example of what we just saw there.

Okay, it's now asking about time dimension for revenue.

So whether we do lifetime totals only, no way.

A fixed recent window with a plus or minus.

That might be interesting.

I think a time series with a range selector,

that's kind of what I was thinking.

Yeah, a bar chart of revenue over time

with seven days, 30 days, and 90 days.

All time toggles shows trend and seasonality.

Yep, that's kind of what I'm thinking here.

Okay, let's plug this in.

That looks good.

I think I wanna go with C,

but I don't wanna do the Delta comparisons number.

I think I just wanna keep it pretty clean.

And I want the time series to be seven days, 30 days,

one year, and all time.

As an implementation detail here,

I want to make sure that the time series

is kept in the URL as a parameter.

So seven days, 30 days, 12 months, or all time.

Don't be afraid to specify implementation details here.

If you have an idea of how you want it to work,

then just go for it.

Okay, next up it's asking about aggregating the chart

versus a per course breakdown on the chart itself.

I think probably a single aggregate line

to just see their revenue makes most sense.

I don't think multiple lines

tracking each individual course makes sense.

And then we can see at the bottom,

maybe a kind of table with all of the courses

and how they've done.

Let's go with A and let's have a nice

sortable table at the bottom.

That feels fine to me.

Okay, let's see what it says next.

One extra little tidbit is I often like to do

two grilling sessions at the same time,

sometimes three if I'm feeling spicy,

literally just having one in the left panel,

one in the right panel.

And while one is going off and doing something,

then I'm planning with the other one.

Okay, what's it gone and said now?

So table columns.

This is tricky because this is really a UI thing here.

So I'm just gonna splurge out what's in my head.

So I think we need the list price of the course in there.

We need the revenue for that period.

We need the amount of sales.

Sales are different from enrollments.

So we probably also need the enrollments as well,

because you can purchase via a team.

And then finally we need the average rating

and the rating count as well, the number of ratings.

I don't think we need a status badge here

because this isn't like a course authoring part

of the platform.

This is just literally how much money

did my published courses make?

Okay, let's see what it says here.

Again, notice how important it is

that I understand my domain really deeply.

Like I understand that you can purchase via a team.

So it means that enrollments are different from sales.

So it looks like two final columns here.

We've got, or two final questions.

Filter to publish courses only, yes.

And enrollments column in range.

Yeah, obviously makes sense.

So, okay, go with a one, which is published only,

and then go with enrollments in range.

Those two make sense.

But I get the feeling when it starts asking

more obvious rapid fire questions,

then we are probably in a pretty good spot.

We're starting to reach a shared understanding.

Okay, it's now asking for a KPI strip above the chart.

Again, a sort of, you know, UI thing here.

I think, yeah, some little cards above summary cards

would be quite useful.

This sounds good.

I think that total revenue, then total enrollments,

then average rating makes sense

for the summary cards at the top.

That sounds fine to me.

Rock and roll.

Okay, question nine, maybe we're not at the end yet.

Chart bucket granularity per range.

So for seven days, it's saying seven buckets.

For 30 days, it's saying 30 buckets, 12 months, 12 buckets.

It looks like it's kind of landed on a bar chart here,

but I think it should probably go,

yeah, chart itself a bar chart.

I think a line chart is probably better.

You know, you see the line go up.

Yeah, the number of buckets looks good there,

and I think we should use a line chart

instead of a bar chart.

And then if a bucket has zero dollars,

then it's just, you know, it's still rendered.

So we should still just render zero dollars

for that bucket.

It's interesting, this grilling session

is a lot more implementation focused actually,

because maybe the implementation

is just a bit more complicated.

There's a bit more front end stuff to do.

Okay, now it's checking out the charting library.

It's saying there's no shanxi and chart components

scaffolded, we'll need to add one.

I think I would prefer actually just going

for bare recharts.

I'm not necessarily a fan of just like

wrapper components, wrapping libraries.

I think we should just go be bare recharts.

No need to pull in a larger dependency than we need to.

Now come on, is this over?

Is this over?

Can I go and have my lunch?

Okay, still going, we have a navigation entry point.

We have a new sidebar item or a tab,

a sub nav on instructor or a button on instructor.

I think a new sidebar item makes most sense.

I'm just gonna go for A here

and the root is instructor analytics.

All right, two questions here.

We've got the default range with no range.

So it's asking either seven days, 30 days,

12 months or all.

I'm gonna go with its recommendation of 30 days.

That's fine.

And then it's talking about empty states.

I think we can simplify what it said here.

30 days as a default makes sense.

With the empty states, just simplify it.

If there's no data or if there are no courses,

just show a page saying no revenue data yet,

publish a course to start seeing analytics.

What do we think?

Is this the last one?

Is this the last one?

We're always playing this game with GrillMe.

It's ridiculous.

I've had people who have had GrillMe

ask them like a hundred questions,

maybe like nearly up to 200 questions.

I'm gonna go with recommendation on no data.

I want to make sure I read you right.

It seems to be making a distinction between

there's no published courses, has published courses,

but there's zero lifetime purchases,

has lifetime purchases,

but zero in the currently selected range.

Yeah, yeah.

So obviously we want the empty state

only when there's no published courses

or zero lifetime purchases.

I 100% agree.

That's exactly the kind of thing

that would get really fuzzy

if you were just reading a plan, right?

Whereas actually having the thing ask you

really socratically adversarially ask you these questions

just really makes it work.

Okay, guess what?

We have reached a shared understanding.

It has stopped grilling us.

Incredible.

We have a very simple V1 spec

and it's time to do the magical thing.

We are at 52.2K tokens,

which is actually pretty light

given how much ground we've covered.

And we're gonna run to PRD.

So in theory to PRD,

we don't need to specify anything else.

It should just read everything

that's in the context already.

Maybe do a little bit of exploration itself

and then just slam a PRD.

So here we go.

And just like that, we have got one.

We have our PRD.

Let's zoom out a touch.

So we've got a problem statement.

Instructors on the platform had no visibility

into how their courses are performing financially.

Correct.

There's no way for instructor to see total revenue,

revenue trends over time.

Admins similarly have no way to view

an instructor's revenue performance.

That's right.

So the solution is a dedicated analytics dashboard

for instructors that provides a revenue focused overview

of all their courses on a single page.

Cool.

So we have a numbered list of user stories.

And this is really useful because

when we go to break these down into tasks,

we can reference these user stories.

These are basically like things

the finished feature should do.

As an instructor,

I want to see my total revenue across all courses

for a selected time period

so that I can understand my overall earnings.

It's who is doing it,

what they are doing,

and then why they want to do it.

If we zoom down past user stories,

we'll end up at implementation decisions.

So this categorizes all of the main modules

that need to be edited or managed.

So we have an analytics service here, which is new,

a deep module that encapsulates

all database query logic for the dashboard.

We are creating an instructor analytics route,

an admin instructor analytics route as well,

a shared admin analytics component.

Very nice.

And some technical decisions too.

So a list of time period filters,

one period drives the whole page.

We have the list of table columns that we decided.

We have table sorting.

This is a big old document here.

And I've also got some testing decisions as well.

We'll look at these a bit more later

when we cover feedback loops.

I'll just kind of collapse those for now.

We've also got a big list of stuff

that's out of scope too.

So this makes sure that the PRD stays constrained

and we don't try to do stuff that isn't there.

So depending on how your grilling session went,

you will probably have landed

on slightly different decisions from mine.

I've also got, by the way, just to complete this,

a further notes section for any stuff

that doesn't fit into the other sections.

And so there we go.

We have successfully figured out the destination

for where we are going.

And like me, you're probably itching

to take this document and actually bring it to life

and put it in code.

So nice work.

I will see you in the next one.


### 039-AI Coding for Real Engineers p39 039 Split Features Across Multiple Context Windows With Multi Phase Plans Day 3

Alright, so at this point we've created our PRD, which is our destination, but we've not

yet created the plan. Now I'm going to argue throughout this section that there's a good

and a bad way to do this plan.md. Or perhaps let's say a good way and a naive way. And

so we're going to start by doing it in the naive way. I would like you inside

the repo to open up a new Claude code session, and you're going to then specify the PRD

instructor analytics dashboard, and we're going to use the at symbol to pull it

directly into context. And then I'm going to say, turn this into a multi-phase plan

and save it as a local markdown file. That's all we're doing. I'm not going to specify

anything else. That's all it is. And we're going to run it. As this is running, what

I want you to do is note down how you might improve this. Note down the thing that it

creates, because we're probably going to get quite divergent responses. And you should

probably do some thinking about how big you want the tasks, how big you want

the phases to be, because task sizing here and what you do within that context

window is really important. So walk it through, see what it creates, and I will

see you in the solution.


### 040-AI Coding for Real Engineers p40 040 Split Features Across Multiple Context Windows With Multi Phase Plans Soluti

Okay, incredibly, it is actually already ready to go. What it did while I was actually recording the

problem is it did an explore on the code base and then it just wrote down plans in structure

analytics dashboard.md. The first thing I noticed here is how quick it is to go and actually make

changes and eagerly produce an asset before even grilling me about it. With the writer

PRD skill we were really spoiled by the fact that we had a really enriching conversation with

the LLM whereas this is just spitting out something immediately. But I'm going to see

what it's done to see how good it is. We can see first of all it's put it inside the plans directory

here and I'm just going to collapse all of these phases here so that we can understand what it's

doing. Okay, the thing I'm noticing here is that it's gone for four phases, which is nice,

but it's doing it in quite a horizontal style. The four phases are that it's created the

analytics service separately first. This means that every single thing that we need from the

analytics service will be done in one phase. All of the backend architecture will be done

there. Next it's going to create a shared dashboard component and install recharts,

but then it's not until phase three that it's actually going to use that UI in a root and then

it just creates the admin analytics route and the user page link as phase four. Inside each

of these phases here, okay, it's actually got all of the individual steps mapped out here. So

this is almost as if it's giving us a pure implementation guide, a user manual here for

all of this stuff. What I notice here is that I am a little bit scared by all of this

implementation information actually inside the steps. The reason I'm scared by that is because

I'm a developer by trade and I know that you can't purely, you can't get all of the designs

right before you actually go in and implement. Phase one, you can maybe do it because you're

just making changes to the code base as it is right now, but if we look inside phase three,

then yeah, like this might end up with referencing functions that don't end up existing

in the implementation. So this makes me a little bit nervous too. I do like the acceptance criteria,

that's really nice. I also don't like that it's not referencing the user stories in the PRD

because those user stories were ones that we sweated over, right? So all of these here,

I would like to see that actually referenced inside the plan itself so that we can actually

link them back to the why. But anyway, let's go back and see more of what it's up to.

We zoom down to the last one here, is there anything egregious inside here? Again,

it's still doing this kind of like referencing previously created functions, but we're not even

sure if they're going to be created by that point. This is especially true if like during

phase one, we step in as the human and we decide, no, I actually don't want to implement

it that way. In other words, these specific functions here, they will go stale very,

very quickly if we decide to change anything about the implementation in earlier phases.

However, I do think it's got the sizing of the tasks quite nicely. If I zoom back up to the top

and fold them all up again, we can see just sort of what we're up to. None of these look too

large, except possibly for phase one where the analytics service and tests might be harder

than expected. But I suppose since we're only querying the database, maybe it won't be that

tricky. So we have created a relatively naive plan here. It's doing all of its work in

horizontal layers, which will explain why that's bad in the next couple of videos.

The plan is a bit too specific with the implementation. In other words,

it's actually naming functions which might not exist by the time we get to later phases.

However, it is fairly nicely sized and maybe we could even condense phase three and four,

since that's going to be a lot of similar work. Hopefully you reach some of the same

conclusions as me and I would love to hear your thoughts in the Discord if you noticed

anything different from how yours turned out to how mine turned out. Nice work and I will

see you in the next one.


### 041-AI Coding for Real Engineers p41 041 What Are Tracer Bullets Day 3 Planning

I'm really excited about this one because this lesson gives me a chance to talk about one of my favourite discoveries when working with AI over the past, you know, a few months.

And that is that with two words, two well chosen words, you can completely change the way that AI prioritises tasks and you can change the way that it plans.

These two words come from this book, The Pragmatic Programme by David Thomas and Andrew Hunt.

This is a 20 year old engineering text and it has a ton of awesome insights, so I definitely recommend you pick up a copy.

And the two words that we're going to steal from it are Tracer Bullets.

Now the first idea behind Tracer Bullets is that systems have layers.

These layers might be different deployable units like we have here database and an API and a front end, or more likely they're different services within the application such as we have in our project.

But either way, these layers are things that you need to integrate in order to build something that works.

You might have a tiny feature which is front end only, but more likely you're going to have features that touch the front end, the API and the database if they're going to be anything worth using for users.

Now what I have noticed, in fact what we noticed in our previous exercise, is that LLMs tend to code horizontally.

When they're designing the plan, they tend to think about it in terms of layers.

If we have a look at the plan, then we have analytics service plus test, then phase two is an entire component, then phase three is an entire route, phase four is an entire another route.

This is kind of crazy because we're not getting any feedback on whether the whole thing is working until we reach one of the later phases.

Sure, we've got some tests written for the analytics service in phase one, but those tests are kind of meaningless if the design for the service is not going to match up to what we need in phase three or four.

We need early feedback and we need feedback as often as possible.

So this idea early feedback and feedback as often as possible is what comes from the Pagmatic Programmer and Tracer Bullets.

To explain the metaphor, Tracer Bullets were what the anti-aircraft gunners in World War Two used to put into their guns.

They would load in a special bullet every six rounds or so that instead of firing an actual proper bullet that was meant to hurt the planes or something, it would just fire out a kind of phosphorescent beam from its backside.

And so you would see these streaks of Tracer streaking through the sky.

And it meant that the anti-aircraft gunners could look up, could see where their bullets were going and adjust accordingly.

In code, this looks like this, where instead of phases that span an entire layer, we now have phases that actually go through each layer.

Another idea, another name for this concept is vertical slices, where instead of just coding the horizontal stuff, we make sure each phase in the plan touches every layer.

That way we, as the human, are able to go in and like take a look and provide feedback if needed.

But it also means our design actually encompasses all the layers that we need.

And so we're less likely to make mistakes in our architecture because what we're building touches all the integration layers.

What makes this so cool to use with AI is that AI already knows what Tracer bullets are.

It's a relatively famous concept within software engineering.

So all we need to do is just say the words use Tracer bullets and maybe a little bit of brief explanation.

And then the AI just gets it.

I have found that this massively improves the way that AI builds software and we're going to use it throughout the rest of this course.

Hopefully this clicks for you.

But if you have any questions, then do ask them in the Discord.

Nice work and I will see you in the next one.


### 042-AI Coding for Real Engineers p42 042 Use Tracer Bullets In Our Multi Phase Plan Day 3 Planning

All right, now we know about this golden tracer bullets approach.

I want you to open up a new Claude session with zero context in it.

And we're going to use a new skill that I just added to the repo saying PRD to plan.

I wrote this using my skill writing skill, and it has copious mentions of tracer bullets in it.

I would like you then very simply to go into this Claude code instance to say PRD to plan here

and passing in the PRD just here and tabbing to autocomplete.

We're going to run this skill and we're going to see if the output is any better or makes more sense

than the one that we did the naive plan that we already created.

And actually probably as a bit of just sort of sanity checking,

we should probably go inside the plans and delete the original plan.

Because in a sort of to make this a fair test,

we don't necessarily want to have the previous one in the context for the LLM to read and manipulate.

Let's just make this a clear run to test out our new planning skill against the sort of default setup for Claude.

As you're going through this, I'd like you to notice the differences between this new plan and the previous plan

and see if this plan actually does make any improvements or see if you could maybe think about how to improve it further.

Good luck and I'll see you in the solution.


### 043-AI Coding for Real Engineers p43 043 Use Tracer Bullets In Our Multi Phase Plan Solution

Okay, let's run it and see what happens.

Now, of course, predictably, it's doing an explore phase,

which is fantastic.

So exploring the code base architecture,

we can even see that it's using the Sonnet 4.6 model,

which is nice.

I always love it when it uses a cheaper model

for these explore phases,

because it just seems like a good use of resources.

So let's wait for it to complete.

Okey dokey, it's now complete,

and it's come back with a proposed phase breakdown.

This is the way I've designed it

so that it actually asks you for feedback on the phases

before it actually commits to building the plan out.

So phase one is a lot more interesting and very, very meaty.

We have an analytic service

plus an instructor route plus summary cards.

So this is a definition of a vertical slice, right?

We're doing the service plus the route

plus some UI as well.

We can see the way that it's defined that down below.

Phase one is the tracer bullet

that wires up the full stack

with the simplest possible data, three summary numbers.

Each subsequent phase extends the service

and dashboard incrementally.

Now that is exactly what I'm looking for.

By the end of phase one,

we will know if the whole thing works, essentially,

whether we can connect the analytic service

up to the instructor route

and sort of what weird caveats there are there,

and we'll have discovered all of the weirdness

to do with this feature.

In other words, all of the unknown unknowns

will have been flushed out.

Now I'm looking at this immediately.

I'm thinking five phases might be a bit too much.

Phase one, I think, is packed in nicely.

I think that's a good meaty amount.

If anything, it might be too big,

especially if we encounter any issues,

but maybe it's okay.

I'm gonna say it's okay.

But I think we can group phase two and phase three together

since they're both UI concerns,

and then maybe phase four and phase five

can also be grouped together.

Like they're definitely unrelated,

admin access and versus empty states,

but they both touch the same area of the code base,

so it makes sense to do them in the same session,

and they're both pretty small.

So that is what I'm gonna say to the UI.

Group together phase two and phase three,

and then make another grouping for phase four

and phase five, resulting in three phases total.

So now if I run that,

it should give me a new set of our new plan.

Okay, it's now going ahead to write the plan file,

so let's see what it cooks up.

Okay, it has spat out plans,

instructor analytics dashboard.md, beautiful.

And we can see it looks somewhat different

from the previous plan.

First of all, the phases down the bottom here

are nicely laid out.

So we've got our three phases,

and we can see a description of each phase,

in other words, what to build,

and the user stories that they reference

in the parent PRD.

We can see, too, that there's not a ton

of implementation like leakage inside here.

In other words, the previous plan

was almost an implementation just in pseudo code,

but this is a lot more just text essentially.

It's a description of the feature.

Now the reason for this is that in the skill itself,

I actually added some instructions

to basically only make durable decisions

that will definitely work across all phases.

If you look inside the skill here,

where is it inside PRD to plan,

then we say, identify durable architectural decisions

before slicing, identify high-level decisions

that are unlikely to change throughout implementation.

In other words, we are planning what we can.

You do want some implementation information

in the plan itself,

because it just helps keep everything on rails

and means that what comes out is more predictable.

But what we're saying here really

is don't plan what you can't plan.

Lots of stuff will only become apparent

when you start actually going in and implementing it.

So to head back to the actual plan that we have,

yeah, we can see the durable decisions

are the instructor analytics at this route

in this particular file.

In the schema, okay, there's no changes.

In the service, there's a new analytics service.

We're just sort of like pulling in

like information about the authentication,

get current user ID from the repo

and stuff like dependencies that we're adding.

Very nice.

But of course, the proof of the plan is in the pudding.

In other words, we should actually go

and implement this to see how it works.

And of course, your plan may look different to mine.

So what did you notice about your plan

that you liked or maybe didn't like?

Is the level of detail too high or not high enough?

What do you think?

Share it in the Discord.

I would love to hear your thoughts.

Nice work and I will see you in the next one.


### 044-AI Coding for Real Engineers p44 044 Executing Our Multi Phase Plan Day 3 Planning

Okay, we now have our PRD inside PRD forward slash instructor analytics dashboard.

We now have our plan inside instructor analytics dashboard in the plans directory.

Our job now is to open Claw code, enter a new session, and we are going to prompt it using this.

We're then going to pass in a couple of files to it.

We're going to pass in the PRD, of course, and then we're going to pass in the plan.

And finally, we're going to say do phase one.

As a final thing, I'm going to press shift tab here to accept edits on.

We're not doing plan mode here.

We are just getting it to churn out some code immediately.

Now, what I would like you to notice is what happens.

Will it do an explore phase first?

Probably yes.

What does the code look like?

How is it doing?

And now once you reach the end of phase one, you get a choice.

You can either clear the context, run the same prompt again, but say do phase two instead, or you can just go,

Okay, you've got all the information in your context.

Just carry on to the next phase.

Or if you're not sure, just default to clearing the context at the end of each phase.

I also recommend that you commit at the end of each phase too.

That will give you just a nice safe point to go back to.

And that's what I'm going to be doing.

Other than that, enjoy.

This is a really, really fun way to build because we've already done the legwork.

We already know what's needed.

We've spec'd it all out.

We've got the plan and now we just get to watch it roll down the hill.

So good luck and I'll see you in the solution.


### 045-AI Coding for Real Engineers p45 045 Executing Our Multi Phase Plan Solution

Okay, let's run it.

I'm assuming it of course it's gonna do an explore phase.

Yep, there it is.

As soon as I mention it, there it goes exploring.

I'll check back in with you once it's complete.

Alrighty, it has now completed the explore phase.

It did that fairly quickly, took about a minute

and it's created a bunch of different tasks for itself.

For the first thing it's done

it's created the analytics service here.

I might just give us a cursory review.

So we are up here inside analytics service, services.

Let's just check how big it made this

and what it added to it.

Yeah, we can see here that it's really not providing

that many analytics.

In other words, it's only put in here enough features

to satisfy the tracer bullet.

When we finish,

this is probably gonna be a pretty big file.

But for now, Claude is happy just to leave it be small

because we specified it should be a tracer bullet.

Fantastic.

It is now running the tests too, which is good.

So all 12 tests passed.

Now let me build the UI component.

So it's only built 12 tests here.

With the previous plan,

it would have spent a lot of time here

building out the whole horizontal level,

but we now have just enough signal to know that,

okay, we're on target, we can proceed.

It's now building out the analytics dashboard.

That's good.

And now building out the route.

We are now approaching 32%.

So we're doing pretty well staying

inside the smart zone here.

And we've covered a lot of ground.

Okay, very cool.

It's now given us a total description

about what's been happening, which looks all good.

I'm gonna say commit this code.

And now I can go in and actually QA this.

So it's looking pretty nice, kind of pretty sparse.

I don't love that we've got free

being the total revenue here.

This is probably a bug from somewhere.

We will look at how to do bug reports

within these loops a bit later.

But so for now,

I'll just have to sit there and rankle with it.

We are getting some money shown up at 12 months.

And if I hide my face here,

we can see that if we switch to Sarah Chen,

who's the other instructor,

then we see other information here.

So average rating is four,

and she's got four enrollments.

So that's looking great.

So notice how quickly we're able to gain confidence

in what we're building

by building this tracer bullet early.

Okay, I'm gonna call that phase one complete.

And this now,

this is the decision that I was talking about.

34.3% is, oh, I mean,

I probably would definitely clear the context at 40%,

right?

And maybe definitely at like 35.

So I think I am going to clear the context here

and free it up for a new phase.

I'm then just going to press up a couple of times

until I get to my prompt here

for the plans and the PRD.

I'm gonna say instead of phase one, do phase two.

Now, of course, then because we cleared,

it's then going to explore

the phase one implementation again.

So it's gonna look at all the same stuff

that we just cleared out of the context.

So that's what's annoying about clearing the context,

right?

Because we then have to spend 30 seconds

just catching up with what the phase one

implementation actually was.

But now by the time we're actually going to implement,

nice, we're only at 15.5% context,

well in the smart zone.

So I think we've got the picture now

as to what it does when it's implementing.

So I'll join you once it's finished implementing.

Okay, we have now finished phase two.

That's pretty cool.

We've got a new analytics service,

a dashboard component, a route and some tests.

And as we can see on the analytics dashboard,

we now have a chart here of sorts

and we have a per course breakdown at the bottom here.

Now we do actually have a show stopper bug here,

which is that there are no lines on the chart.

You can hover over them by just doing this or whatever,

but you can't actually see the data.

So I'm going to go back to Claude here

and I'm gonna say,

you can't see any lines on the chart, please add them.

And I'm gonna run this and I'm gonna see what happens.

Now I feel confident doing this

within the same context window

because we're only at like 30% here.

We've got another 10% context window to play with.

If I felt that we were straying into the dumb zone here,

I would clear the context and commit the code

and then get it to create a new session

based on just this bug probably.

Or I might batch a bunch of bug fixes together

so that it does them all together.

Okay, it's proposed to fix.

And if we go and take a look at it,

we can see that it's actually managed

to find a really good fix.

So if we look at 30 days potentially,

yes, we've got a nice little thing here, that's cool.

Now at this point, I do have a lot of budget left.

So I've still got, you know,

I would say 10, 20% of context left.

I could do some more QA on this commit

before I commit it.

Or I could just keep plowing on with phase three

and QA all at the end.

So I'm going to commit this

and then I'm gonna clear

and I'm gonna complete phase three.

By the way, I do like using Claude code to commit

because it just writes really detailed commit messages

that then future Claude instances can go and read

and understand what was done.

Your commit history ends up being really, really important

for Claude code because it's a really high value signal

because the code and the reason for the change

is tied together really closely.

So yeah, what's old is new again, you know,

commit messages are important again, all that.

So I'm going to clear the context

because that commit worked fine.

And now I'll go upwards

and I will go and do phase three instead.

And again, I will see you when this has completed phasing.

Okay, all done.

Here's a summary of what was implemented for phase three,

admin access and empty states.

We now have an admin route

that enforces user role.admin,

validates the instructor ID.

Okay, we've got a completed analytics service.

Time to get QAing, I think.

So I've gone to the application

and the dev UI I've logged in

is Alex Rivera, who is the admin.

I've gone to the manage users page here

and I can see that there's a view analytics button

next to the instructors.

And look at this, that's really nice.

I get a breadcrumb up here of all the places I can go

and I get to see exactly the same information

as Sarah Chen does.

If we look at Marcus Johnson here,

I can view his analytics too.

But if I change to,

why don't we change to James Park here?

Then it says that only admins can access this page.

I'm not really in love with this, I suppose.

This should probably be a 404 rather than a 401.

In other words, we want to say

this page doesn't exist

instead of this page does exist

and your attempt to hack in is not working.

But either way, that's something

that can go on a backlog later.

But I am happy enough with this to call it done, I think.

So I'm gonna go back in,

I'm gonna tell it commit the code

and after that, I am done.

What you probably notice here

is how hands-off the implementation stage actually is.

There are certainly moments when we need to jump in

and add our inputs and add our taste.

But for the most part,

because we've written such a clear destination

and we've specified the journey,

the agent is basically just able to get on with it

and it understands where it's gonna go.

Now this approach scales to really, really big builds.

All we need is a bit of a longer, more in-depth PRD

and more time spent thinking about the journey there.

But once those two documents are in place

and we've taken the time to think of a really good plan

that involves tracer bullets, early feedback,

then we can really start cooking.

Nice work and I will see you in the next one.


### 046-AI Coding for Real Engineers p46 046 Ask User Question Day 3 Planning

Something that came up a lot in the previous cohort was a

Claude specific UI that some people really like and some

people really don't like. And this UI is specifically for

asking the user questions. For instance, I can get Claude here

to ask me my eye color, and it will probably just respond

with a simple question here. So it just says what's your eye

color. But now if I say ask me my eye color again, and I'm

going to say use the Ask user question tool here. And this

Ask user question tool is a specific Claude thing. And it

shows this really nice user interface here. So I can select

what my eye color is from these options, or I can type

something in here, or I can chat about this, for

instance. And here it says the user declined to answer

questions. So this Ask user question tool here is just a

UI that you can opt into in basically any skill, any prompt,

simply by saying use this. Now this is 100% personal

preference from me, but I really don't like that UI.

The first time it happened, it was like, wow, this is the

coolest thing ever. It's asking me questions in a

multiple choice format. But I've just found it a little

bit harder to navigate than just reading what Claude says.

And in fact, this is a bit of behind the scenes magic. I

actually have this in my global Claude.md here saying,

don't use the Ask user question tool because I dislike it so

much. And so now you know, if you don't like that UI, you

can put this in your global Claude.md to add it there and

never see it again. If you do like it, then you can add it

to your skills, add it to your prompts, all that stuff.

And as far as I know, this is Claude only, although

probably by the time of recording, lots of other

people will have implemented it as well, but with maybe

slightly different naming schemes. So there we go, a

nice little aside for you. Nice work, and I'll see you in

the next one.


### 047-AI Coding for Real Engineers p47 047 AI Coding for Real Engineers Office Hours (Day 1 Morning)

Hello pals. Good morning. Welcome to the cohort. Welcome, welcome, welcome.

We're starting a couple of minutes early just because why not? It's fun.

You tell me how does the audio sound first of all? Am I cutting a little bit?

I think it might be a touch high. Let me just bump it down a touch.

Hello, hello, hello. That sounds reasonable.

What's up, Fuzzy Fox? Great to see some old faces in here.

It got scary. Sorry. It's like when you join a Zoom call and you're like 20 minutes.

I always do this. I always join 20 minutes early to every Zoom call I can.

And then very occasionally there'll be someone mad like me who joins that early too.

And we just have to have this 20 minute conversation. It's all good. Good audio.

Good, good, good, good. Well, welcome. Welcome, welcome. Tell me where you're calling from.

First of all, I am here in Oxford, UK. It's sort my lighting out actually.

That's a bit better. KSA. Where's KSA? KSA Google Maps. Nice.

The go-to waiting topic of conversation. I'm not sure actually.

100 of you already. Beautiful stuff. This cohort is, I mean,

considering we're carrying over the around 2,500 folks from before and we've added probably of the same number again,

which I was not expecting. I was expecting this to be a slightly smaller sale because, you know,

we just didn't give it the big razzmatazz we did last time. We're going to have about 5,000 people in this cohort, which is wild.

It's going to be awesome. I mean, already the density of discussion and the quality of because you've got a whole bunch of people who've already done this before.

You, if that's you, thank you so much for joining again. I'm excited to give you the updates.

I'm so excited for the new people to get in on this. That's not three million for me.

Like, you know, loads of people have paid for this with PPP. Loads of people have done sales discount. You get the idea.

Yeah, good. I'm glad you're excited. I'm super excited. So, I mean, with all of these office hours, I always have a debate.

I'm always really tempted to try and use like the Discord native kind of setup here.

I've made this cohort office hours questions channel here, which you can upvote questions in.

But I think the thing that just worked really, really well last time was using Slido.

So I think we're probably going to use Slido for this. Slido is a question answering application.

It means that you can vote on the best questions. The best questions immediately get surfaced to me.

And my job here is basically to answer all of your questions.

So, yeah, Cologne, Germany, just heading back home after an anime convention.

Athens, Greece. What's up? Palestine. What's up? Yeah, Slido is good.

I think Slido is the way to do it.

I'm sort of scared because there's 200 of you in here. 200 of you in here. Fantastic.

I'm sort of scared because I'm not paid for Slido. So if anyone has like if anyone hits any limits here, just let me know.

And I'll get my credit card out midstream and I'll pay for Slido so we can all join. I think it has like 150 limit.

If you go to slido.com, enter the code, you'll be in.

I'm going to bump down the audio just a touch because I saw it clipping there.

Melbourne. What's up Melbourne?

Hello, hello, hello.

So we've shipped all sorts of improvements to this cohort.

This is instead of using Docker Sandbox, for instance, we're using Sandcastle.

I spent a solid kind of a solid week improving Sandcastle,

ironing out all the bugs, adding support for more coding agents.

It's in a really nice place right now.

The oven is off.

I have an issue with my oven, which is it very occasionally trips the electrics and that happened during a cohort office hours twice.

Twice it happened.

But the oven is off.

Hello from Germany, from Thailand, from Belgium.

Alright folks, join here and you should be able to ask me some questions.

If not, I might not have set it up properly so let me just set it up.

Ah yeah, here we go. Audience Q&A. Here we go.

So we should have audience Q&A open.

And you should be able to ask me questions.

243 of you. Wonderful stuff.

Why don't we, while you guys are kind of checking that out,

why don't we just do a little kind of walkthrough of what's in the course?

Yeah, it is on top of that. I mean, you just go to slido.com basically.

Here we go.

Oh, that shouldn't be there actually.

That shouldn't be there.

I assume these are unlisted.

Yeah, that shouldn't be there. I need to ping my team about that.

Anyway, so folks.

We have essentially six days of content spread out over two weeks.

In previous cohorts I've done it where every day you get a new day of content and that's fairly wild.

We've expanded this in all sorts of places.

The main one in the day one fundamentals, for instance,

is we've replaced a lesson about why plan mode is great with why plan mode sucks.

You know, you will still have access to the course after it's done.

Absolutely. So this is this is probably, I mean, the biggest early change.

I've really got frustrated with plan mode, having used it a bunch.

And actually in the course we show how plan mode worked and then we moved away from it.

So just replacing it early in the course sort of makes sense here.

We've added lessons on handing off to.

I've added sort of a bit more exploration about a non determinism, about how that functions.

And then we go into steering, which is relatively unchanged.

So steering is all about now kind of steering the agent through Claude.MD, through agents.MD and via skills.

And then day three is all about planning.

So how to tackle enormous tasks, how to write great PRDs and using something that I think is just critical

for getting the most out of multi agent sessions, which are traceable.

It's traceable. It's allowing you to slice work into vertical slices and essentially find the correct path

through a large amount of work, which can be applicable to any time you want to do a large amount of work with AI,

whether it's goal, whether it's AFK agents, which I'll show you part in the course.

So how are we doing? Yeah, we got questions.

OK, so the point of these questions is you can upvote them here.

So this one has 19 votes and we shall be answering them one by one.

I'm going to try something a little different this time, which I'm going to try recording this on my recording software at the same time.

So yeah, let's just give this a go.

All right, so let's yeah, I can still see the chats, can still see you guys.

Let's go for this one.

What has been the biggest change in the world of AI that has changed my workflows over the past month or two?

Well, my attitude here is that I tend to not pay that much attention to the world of AI, which is a strange thing to say.

And I think that paying too much pathological attention to new model updates is missing the point.

What you're really getting excited for when you look at a new model update is the new capabilities that the model will bring.

And, you know, like so far what we've seen, I mean, obviously when Opus four point five came out, I consider that as the moment when AI coding really became viable.

And so everyone's sort of waiting for that big next step of the big moment.

And that really only shook out about a month after release as people really started to use it.

You start to see a groundswell of people going, OK, this has really changed something.

So I think that paying pathologically deep attention to every new model release and every new harness that comes out is bad.

I don't think you should do it.

The main reason being that it distracts you from what you should actually be doing, which is paying attention to your own skills and your own understanding of how these systems work.

And like looking at what cool stuff people you respect are doing essentially.

So the biggest personal change for me has really happened in the last couple of weeks, which is I've started using GitHub as a first class runner for my agents.

A lot of the stuff we do in this course is focused on local development, on focused on running things in Docker sandboxes.

And I've started using Sandcastle inside GitHub actions.

So when I trigger like a label on an issue, it fires off a GitHub action to do various things.

And we can explore that kind of in these office hours.

It just came too late to make it into the course, basically.

But that has probably been the biggest change for me is starting to rely more on plain GitHub instead of doing the local stuff, really.

But that's not come from an AI model.

That's come from a conference I went to when I saw someone doing this and I thought, God, that's a really good idea.

So how much time should you allocate during this and next week to this course Min and Max?

I find this question so hard to answer.

We basically have a kind of guide which is around eight hours a week.

There's slightly more content in this course than there was last time.

The thing is here that you have interactive lessons which can expand and contract based on how much attention you give them.

You can literally just watch the content and not do any of the exercises, you know, but then why are you doing the course?

You can participate in the discussions or you can not participate in the discussions.

And so it really is a course where you're given a load of stuff, a load of playgrounds to mess about in.

And it's up to you how long you spend in them.

And eight hours is my vague guide per week.

Benefit of running agents in the cloud versus running harness locally.

So I've found that you essentially have two types of tasks that you need to accomplish.

The two types of tasks can be divided into human in the loop tasks and AFK tasks.

I talk about this during the course.

Human in the loop tasks, HITL, are tasks where you and the agent need to be in the same session.

So, for instance, grilling is a great example because it's an interview back and forth chatting.

And so during the grilling session, you're able to kind of talk through discussions

and talk through ideas that you might miss if you run AFK.

You sort of can't run that AFK.

AFK away from keyboard is longer sort of sessions,

longer pieces of work that are well specified that you can get the agent to do without you being there.

And for those running in the cloud makes a ton of sense because you can kick off an AFK session,

let's say to implement some work or to review some work.

And you can just come back to when it notifies you.

So it's not so much benefits, let's say, but it's more different strokes for different folks, really.

The cool thing about running agents in the cloud is you don't need to worry about isolating work trees from each other.

You can just spin up another sandbox, let's say.

So Versal sandboxes or GitHub actions or anything that spins up servers, you know, Kubernetes or something.

They can just spin up a server.

The agent can work in that server and it's isolated from everything.

Whereas you have to manage that isolation on your own machine, which can be a little bit onerous.

Good question.

How do you determine when to just do something with full human loop versus triggering AFK workflows?

So in this course, we're going to talk about AFK and human loop a lot,

because I think that AFK is the best way you can scale yourself and scale a team and scale your development workflow.

So let's say I'm in a cloud for the first time the other day.

I hit my limits on 20x max.

I'd never done that before.

I'd never hit my limits on 20x max.

And I did it with hours to spare.

And the way I was doing that was I was kicking off a bunch of background jobs at the same time, a bunch of AFK workflows.

And I've started to get it.

So it's sort of really cheap for me to do that.

And I get a lot of value back out of it.

So that just means that essentially what you're doing with an AFK workflow is you're delegating your delegating work.

And that delegation is incredibly useful and incredibly time saving.

And I believe is the way that you can get the most out of AI.

Essentially, you're planning with human loop and you're executing with AFK.

And you're also often reviewing human loop as well.

Claude 20x max is their top billing option.

Can you describe your thought process when writing skills, tips and tricks, best practices, etc.?

Yeah. So my thoughts here are evolving.

For those who don't know, my skills repo has gone absolutely nuts.

It's on like 114k stars or something.

Maybe a lot of the reason that you guys are here, especially the new folks, is that.

And that's amazing.

It's been awesome for me.

And it is literally the skills I use every day.

So just seeing people really dig in that is awesome.

When I'm writing those skills, I really am developing my thoughts here.

So I'm experimenting all the time with different skills.

I'm not sure if I can recommend best practices.

I do think, though, you need an attitude of deleting as much as you can.

If you get an AI to scaffold your skills, which is often what I do,

you will find it has a ton of duplication.

It has a ton of just useless words.

And deleting as much of the skill as possible is really useful.

What you end up with is if you have long skills,

there's a lot inside the skill that's competing for attention.

There's just a lot of content in there.

And so finding the important bits in the skill is quite difficult for the agent

who's receiving the skill, who's consuming the skill.

And so short skills, I find, are better because then it's easier to...

You can imagine the words inside the skill as kind of like peaks and troughs.

As like, this is more important, let's say, than this bit.

You might have a key instruction in the skill,

and then you might have some supporting information.

Some people have managed this through all caps.

You say, you must do this. You must do x, y, x, y.

For instance, in Grill Me, I could have said,

interview the user relentlessly about x, y, and z.

But I find if you're doing that, it's kind of like you're using the...

Anyone who's done CSS, it's like the important marker in CSS

that clobbers all other styles that are related to it.

So you're essentially using a hammer when you should be using a chisel

or a scalpel, a more precise instrument.

So I think choose your words very carefully with your skills.

Refine those words over time.

Make sure you're adjusting as you notice things immediately.

And keep short skills, keep concise skills,

and don't go too hard with instructions

because they tend to dominate the rest of the skill.

But my thoughts here are revolving.

Can you explain some of the first principles of good software design

and the different frameworks for harnessing B-mad superpowers and your own?

Okay.

I do touch on this in the course.

I mean, first principles is really tricky

because what you have with software design is a ton of trade-offs.

What you're always trying to do

is you're trying to make code bases that are easy to change.

That is the definition of a good code base.

That is from...

In fact, let me dig out a book.

Are you ready? It's the first book wave.

Wee! Refactoring by Martin Fowler.

With contributions by Ken Beck.

Refactoring is a classic.

The definition for easy-to-change code bases are found in

John Osterhout's philosophy of software design,

but refactoring also mentions it.

If you have a code base that's easy to make changes in,

then it's easy to adjust,

easy to modify features in without causing bugs.

If you have a code base that's hard to change,

then it's hard to do that.

How do you make code bases that are easy to change?

Well, you design them so that if you make a change in one place,

it doesn't ripple out to a thousand other places, right?

If you have automated tests, let's say,

where you can see if a change causes a bug,

then that's very good.

That makes your code base easier to change.

So I think of those as kind of being different to,

like, B-mad and superpowers, et cetera.

I mean, B-mad and superpowers, like,

how much you impose software fundamentals on them

is kind of up to you, really.

The truth is that I've not really used them

because I've been too invested in creating my own set of skills,

which mirror my preferences.

But the reports I've had on them,

especially people who've taken this course,

are that B-mad and superpowers both really like to grab the wheel

and like to essentially try to steer you,

whereas I believe you as the user should always be in control.

I'll just quickly answer this one.

Do we in Cohort 4 get access to future cohort material?

I gave, because Cohort 3 to Cohort 4 was a relatively small jump,

I've given folks in Cohort 3 free access to Cohort 4,

but that's not guaranteed in the future.

So you've bought this cohort, this is the cohort you get.

What are the most effective methods for describing how code should be written?

I find it very difficult to get codexed CC to code exactly like I want it to.

So, hmm, there's two things here,

which is that if you're delegating work,

whether you're delegating it to a human or you're delegating it to an AI,

there's such a thing as micromanaging.

You do not want to micromanage your AI.

You don't necessarily want to force it to code exactly how you want to in every single way.

You should allow it to somewhat adopt its own style,

as long as that style is something that you approve of

and that's sort of within the bounds of acceptability.

This means that you probably need to widen the bounds of acceptability a little bit.

However, there are things that the agents will do that you don't like

and you think will cause issues in the future.

And those issues will be material issues,

like they'll make the codebase harder to change or they will cause bugs directly.

In those cases, for instance, I have a React application,

and in that React application I use React Router.

And for whatever reason, the agent loves using useEffect

instead of using React Router-like primitives.

So there I have a specific instruction that I want to say to the agent.

I want to say, OK, don't use this, use this instead.

Now, at what point in the process is it a good idea to tell it that?

So let's actually put up a diagram here.

So essentially we're talking about steering, right?

We're saying, do this, don't do that.

Now, when should we add this instruction?

There are several places we could do it.

We could do it during planning, right?

When we're grilling or when we're creating the PRD,

we could say, don't use useEffect, use React Router-primitives.

So we could bake it into our plans.

That's something I do for some things, not something I do for everything.

We could have it available in claw.md or agents.md,

where we put it into, essentially, we push it to the agent.

And we say, OK, every single time you run an agent in this codebase,

don't use useEffect, use React Router.

That seems a little bit heavy to me.

We could do it during implementation.

So we could say, in, let's say, the skill that we use for implementation

or the prompt we use for implementation,

let's say when we're running an AFK agent, we could say, do this thing, right?

We could give it the instruction then.

Or we could run it in review.

So when we run automated review on our codebases,

we could add the instruction then.

Now, in my opinion, planning is the wrong place for this.

The reason it's the wrong place is that you don't...

Hmm, what's the right way of saying this?

When you're planning, you're really thinking about things

from the user's point of view.

You're thinking at a very, very high level.

And adding implementation details like this is a little bit flaky for me.

It doesn't feel like the right place.

Because if we think about this instruction,

this is an instruction that we've got to add

on top of all of the other instructions, right?

Every other thing that we say.

And planning is often when you have the most density of instruction, right?

You're specifying everything that you need to

about the app that you're building or the feature that you're building.

And so planning doesn't feel like the right place either.

Claw.md is a terrible place to put this

because it pushes it to every single session.

This is a...

We might be talking about a tiny little tweak that we want to make.

Having it in Claw.md will mean it's pushed to every single session,

whether it wants it or not.

That's not good.

During implementation, I also think is the wrong place for this

because during implementation, this is probably the place

where the context window is going to be the most strained, right?

Because we're pushing out a ton of code.

Not good.

So, you know, do we want to add this instruction on top of there?

I don't think so.

If we're running automated review anyway,

then automated review is a great place to add this instruction

because we want the automated review to make changes to the code

and say, OK, boom, like, let's do it.

Let's...

We need to give it license to change things.

And so I think review, the review stage is the best place to do this.

Now, when you do review, it's like, you know,

you could have it, let's say it creates a PR,

you add a label to that PR, it then reviews the PR

and applies these kind of steering instructions to it.

So in my opinion, review is the best place to add this kind of steering logic.

What's been my biggest aha moment

while putting together the latest course material?

I hate these questions because they're so wide.

I mean, it's objectively a good question, but it's like,

what is the biggest aha moment?

I suppose it's the plan mode thing.

I suppose it's the plan mode thing.

I don't know.

I mean, every time I put together course material,

there's always aha moments.

Like, my job is just trying to find the aha moments, really.

So they're all aha moments.

You're quite vocally a fan of using claw code.

Have I tried any other agentic harnesses?

What makes you keep coming back to claw code if so?

I mean, claw code is fine.

Like, I don't know if I'm particularly vocal about it.

If anything, like just yesterday,

I posted a tweet how much I hate a particular thing that they've added.

I do use it just because I've baked it into all of my workflows,

but the tools that I've built,

like Sandcastle, are harness agnostic.

So you don't need to plug them in, basically.

So yeah.

What makes me keep coming back to claw code?

Because I've got a subscription, I suppose.

When in June 16th,

they're going to change the way that AFK runs work with clawed,

and that will probably tip me over the edge and push me into codex.

I've got a codex subscription.

I just don't use it that much, and I probably should.

Really, I'm just...

I have a sort of responsibility as a teacher

to use the thing that most people are using,

you know, so I can teach it effectively.

And so that's kind of why I use claw code, really.

It's not a particular preference.

What's my view on the recent change Anthropic made

to using OAuth token from setup tokens to run clawed P?

This sounds like it will affect AFK agents.

Yeah, this is what I was just referencing, actually.

My view is that it's an enormous cut

to running AFK agents framed as a bonus.

I made a YouTube video about it when it happened, actually,

so you can check out the YouTube video.

What do you do if you find your context window has too many tokens?

So this question, I assume, is,

what do you do if you're hitting the dumb zone?

Right?

This is something I talk about in the course.

What do you do when you feel like the AI is getting dumber,

the attention relationships are starting to degrade,

it's starting to lose track of things you've told it,

and it's starting to lose track of its steering instructions

making strange decisions?

What do you do?

So you have really two choices, three choices, probably.

You can... Why don't we add another one?

What am I doing?

Let me find some old diagrams.

So the first one is that you can hand off.

Let's actually do this one.

So let's say you're in a grilling session, right?

You're grilling and you're building up this blue context window here,

and you've got a sort of idea in your head,

which is this little dotted line of where the dumb zone is.

Now, you're grilling, grilling, grilling, grilling, grilling,

and you realise, oh, there's a question in here that I need to sort of answer,

but if I do some prototyping here, if I try to build something,

then I'm going to go way over the dumb zone.

I need to hand off to a separate session in order to achieve that.

Well, you can use my handoff skill,

which is something I teach in the fundamentals,

and you hand off to a separate prototyping session.

Where inside here, you can go, right, I now have a new context window.

I can do whatever I want with this.

I can just go nuts.

I can do a load of prototyping,

and then maybe I can hand off to the original grilling

in order to carry on my session.

Or, let's see if I've got another diagram here.

Let's just use this one.

Yeah.

Or you can compact.

So again, this is something I talk about in fundamentals.

This is common to all agents, all coding agents seem to do this.

You're adding tokens to your context window, continuing conversation,

tool calls, web searches, file rights, all that stuff,

and you sort of start getting into the dumb zone.

You get a little bit scared,

but let's say you're doing a debugging session

and you want to just continue where you left off.

You want to say, okay, I want to remember the conversation,

I don't want to be in the dumb zone anymore.

You can run compact and there we go.

Back to here.

And we essentially compact all of the session history

that we've had so far into a smaller space.

We summarize it,

and so we can continue the same conversation.

What is the most high leverage AI coding skill in your opinion?

High leverage.

You mean skill like,

this is a tricky question to answer because it's just,

do they mean skill like personal skill or literal skill?

Grill with Docs has been my, an incredible one for me.

It's certainly the skill that I use most often.

Yeah.

120K is about right for dumb zone.

That's, that's my current thing.

That's my current thinking on where the dumb zone is.

Any takes on having docs of patterns on a specific folder

of the project versus having them in doc Lord rules.

So one thing I talk about in the course is progressive disclosure

and progressive disclosure is essentially,

let's see.

Let's add a new diagram.

Progressive disclosure is the idea that let's say you have

the agent's context window up here,

and then you essentially have choices

when you have this context window.

You can either expand it with more information,

or you can leave little pointers inside here.

And let's say a pointer looks like this,

and it points to another file.

So this file here will have more information,

and this file may itself point to other files, right?

And in this way, you can build up a kind of network

of different files throughout your repository,

all of which, you know, let's say this is the main one,

this is the context window,

and all of this stuff is other files.

So when I look at this, I look at Claude rules.

Claude rules just dump themselves into the context window.

So there's no context pointer here.

It's literally just like you're expanding this,

you're making it bigger.

You're stuffing more stuff into the context window.

And the context window,

especially at the start of your session,

is very, very precious,

because the more guff you have in your context window,

the closer you are to getting into the dumb zone

before you've done any real work.

I've seen people who have 250,000 tokens

in their context window when they start coding,

which is mad to me.

That's crazy, because you're deep in the dumb zone.

You're never going to get anything out of AI that way.

So docs of patterns in a specific folder of the project

that to me sounds like this,

where you have, let's say, your context window.

Inside Claude.md, you have a pointer to,

let's say, docs, codingstandards.md,

something like this.

And that pointer just points to that file.

And inside codingstandards,

you might have a further file down here,

which points to, let's say, docs,

react, don't use effects, or similar, right?

So in this way, you can build these networks

of different connected files throughout your repo

that the agent can easily reference,

because they've just got these little context pointers

pointing to them.

This is a TLDRAW whiteboard

that I've customized to add persistence

in the way that I like it.

What do I think about AI reviewing production PRs

without human in the loop?

AI automated review is an essential tool in your toolbox.

It's not something I covered during the course,

but it's pretty simple to set up.

The reason why I haven't covered it in the course

is because my skill for it is not quite ready yet.

Review is something I'm finding really hard

to make recommendations over,

because everyone's review style is so different,

and the kind of things that people are looking for

are so different.

But what you essentially do is you just run an agent on,

let's go back, let's go to here.

So let's go to these stages of this phase.

So you have just implementation and review.

Let's change this to automated review,

and then down here, let's go human review.

So you have the implementation that produces some commits,

then you immediately go into automated review.

Automated review then produces some commits

that just get committed directly to the branch,

and maybe some observations and some stuff like that,

and then the human review comes in

and does the final checks.

Now it's the job of the automated review

to make the human review as easy as possible

by catching all of the really obvious

stuff by doing obvious security stuff inside here.

Now you can use things like code rabbit or whatever,

but I tend to prefer building rather than buying

at this point.

So yeah, automated review,

if I just go back to what the question was saying,

what do I think about it?

I think it's an essential tool

for improving the quality of the implementation.

Really, the human should only be touching stuff

that the AI has already reviewed.

So let's go back to the previous stage.

So let's go back to the previous stage.

So let's go back to the previous stage.

The AI has already reviewed.

Is Soundcastle making any adjustments

for the post-June 15 Claude licensing changes?

Yes, we will.

I just don't quite know how they're going to land

and what the mechanism is.

So once I do, then I'll be able to make the adjustments.

Why do I think that the Grill Me skill is so impactful

in spite of being so brief?

Anything about prompt engineering we can learn from it?

Yes.

touches on what I was talking about before, which is that people think that skills need

to be huge. They don't. Like, if you think about the most impactful, I don't know, sentences,

paragraphs, pieces in world history, they're not very long, you know, the Gettysburg

Address is not that long, right? You can pack a lot of punch with a short set of sentences.

So I think Grill Me is a great example of a skill that's just big enough. The shorter a skill is,

the easier it is to maintain, the easier it is to security vet, and I think the more focused

output you get from the agent. So yeah, short skills are great. Short kings.

Memory MD feels like it bloats over time in my context. It adds stuff mentioned once,

but was specific to the session. Real benefit versus putting it in Claude.md. Kill it.

I really distrust any memory system, actually. I think the agents being stateless in your code

base is a good thing, because it's easier to optimise for the stateless version of an agent

than it is to optimise for a stateful version of an agent. A stateless version of the agent,

just essentially, what am I saying? It works the same way or within the same set of bounds

again and again and again, because the setup is the same. Whereas a bloated one, or sorry,

a stateful one, will work differently, because the state that it's relying on is different

every time. So I just really don't like these auto memory tools. I think you should be very

carefully managing your own context window and not delegating it.

What is the difference between using a goal and a Ralph loop in Claude code?

Which would you use for AFK implementations and why would you use one over the other?

So what I've noticed with goal, I've used it a few times now, and every time I use it,

let's go back to my context window diagram. Every time I use it, it just does this.

Right, it just blows through the context window and it does automatically compact,

but oh my god, it's just so wasteful in terms of like, you know, like I've had sessions that go

up to 500,000 tokens, you know what I mean? Which is just alien to me. And so what I

really dislike about it is just the way it's implemented. Why don't you just compact a bit

earlier? Why don't you, you know, it seems crazy to me. So with AFK agents, you have much

more control because you can slice the tasks how you want them to. And this means that each time

you run one, let's say you just, let's say we have a task that requires five or let's just say

three vertical slices, right? You have your three vertical slices like this, and then you can

sort of, you know, one might go into a little bit into the dumb zone. Maybe the second

slice is a little bit smaller. Maybe the slice is sort of bang on. You just have a lot more

control over this. And this, this way of doing it is a lot cheaper than doing it with

the huge context window because you know, you're just like the cost of tokens compounds,

the further you get into the context window. So having a, making a model request

when you're this far into the context window, when you're 400k tokens in, let's say,

is a lot more expensive than making it when you're this far in. So yeah, the fact you

get a lot of control, the fact that you get more work done in the smart zone, that's why I think

I get better outputs from using AFK agents or using a Ralph loop, let's say, or just

essentially dividing it into multiple sessions than I do getting it in one big session.

Have I tried coding with Kimi or other Chinese models as well as Mistral's models?

Claud and Codex have their price tag. I've not. No, I've not. I'm mostly not focusing on cost at

the moment. I mean, like, I'm sort of gated by my subscription anyway, so I'm only paying,

you know, 200 pounds a month. What is it? 180 pounds a month or something.

So which I consider cheap, you know, in my circumstances. And

let's see. So I have not just not tried really working with open weight models. Everything I'm

hearing is that they're just not up to snuff and they can't do the things that

that Opus and GPT 5.5 can do. What are my top MCP servers for developing with AI? How do

you ensure that AI fetches relevant documentation for a particular library or framework? I don't

use MCP servers, really. The only MCP server I might use is one that connects my

agent to front end code. And for that, you could just use the agent browser CLI or use

the Playwright CLI directly. So yeah, I don't really do that. I also think that we're going

to look at research phases. Maybe I can pull up my seven phases doc. Yeah, here.

Where's the full one? This one. I have here, you may have already seen this,

my seven phases of AI coding. One of these phases is research. Now, research is a place,

let's say you grill on your idea, you create a product requirements document from that,

you break that into issues, you implement it in a Ralph loop or an AFK agent loop,

and then you review the work. That's the basics here. Now, once you've grilled the idea

that you want to create, you may want to do some research on external libraries. Now,

what I recommend you do is you just devote a period of time, you know, it really doesn't

take that long to just researching the documentation that you need and saving that

in an asset somewhere so that the agent can reference it. I don't think that because once

you have that, then that's something that the implementation can use every time.

I don't think that you need an MCP server for that or something that permanently adds something

to your context window that are like a context pointer to go and grab documentation. I don't

think that makes sense to me. It makes more sense to cache the research that you need to

do in a local markdown file that just gives you exactly what you need at that moment.

So I think being more intentional about research is, in my opinion, better than using the MCP

server. And I assume the MCP server you're talking about is contact seven, which I've

heard a lot of people really like. I've not really used it.

When you're learning something genuinely hard and knew yourself, what's the method I used

to learn? So I've recently been playing around with a skill for this, a teach skill.

If we go into skills here, this is in progress teach. Now, this skill,

because I've been a teacher for a long, long time, I was a voice teacher and singing teacher

before I became a dev. So I was a dev for about seven years. Teacher six years before

that, I've been doing this for four years, if that all adds up. So I've been a teacher

for around 10 years. So I know a thing or two about teaching. And teaching is just

learning, but it's like someone else is tying your shoelaces for you really.

So what this skill does, and I'm still messing about with it, is kind of encodes my

teaching practices into a skill that you can use to get the agent to teach you something.

So when you learn something, you need three things. You need knowledge, which is in this

course taught through explainers. You need skills, which in this course is taught through

interactive exercises. And then you need wisdom. And the wisdom here is interacting with

real world, stuff in the real world. And that's the hardest one to teach. And in this course,

wisdom really comes from the discord, from people chatting to you, and you sort of engaging

in the discussions and seeing that. That's why I'm so excited that there's 5,000 people

in this discord, because the amount of wisdom that's going to be shared is going to be huge.

You need a mission. You need a reason that you're interested in learning about the topic.

I could learn about the history of fruit flies or something, but I don't have a mission that

connects it to something that I care about. And so why would I want to learn it?

Finally, the user should always feel as if they're being challenged just enough, right?

So they're in the zone of proximal development. This is something I obsess about when I consider

how to design my courses, is that I need to make sure you feel challenged, but not overwhelmed.

And that's really hard, especially when you have different levels of people joining the course.

So all of this is kind of encoded into this skill, which I am working on at the moment,

that you can grab and see how it works for you. And yeah, I'd love to know how you get on with

this skill. I'm currently using it to teach me about a kind of area that I know a little

about, but not a lot, which is Linux and user permissions, because that's something that

I'm facing with Sandcastle. That's my mission, is that I'm getting a lot of bugs in that

area because I don't understand it very well. So I'm using this skill to teach me about that.

And I'd love to know how you get on with it. Where are we?

Do I think code quality matters anymore? Right? We're heading into the last little

bit of this office hours. Let's finish on this question because I love this question.

And yeah, this question is really why I made this course, actually.

Do I think code quality matters anymore, or is it better to leave code generated by AI,

since it will be consumed by AI anyway? A code base that's easier to change for humans will

be easier to change for AI. It seems to make sense, right? Because the things that

humans find hard are the things that agents also find hard. They've done research on this.

If you have global state, global variables in your application, then you are going to have

a worst time as a human monitoring that because the dependencies are hard to see,

and the agent will also have a hard time seeing that because there's no context

pointers pointing there. They can't see the global state or the things that are interacting.

So if you have things that are overly coupled, again, that's going to be hard for agents to

work with. So I think with a human, a human can kind of cope with bad code quality,

because you can just bang your head against the wall again and again and again until you

reach the point where you go, okay, I think I understand it now. And you develop memory

about that. And human memory is a lot better than agent memory. Agents, because they are

basically, they're essentially an external contractor on their first day, every single

time. They're a new starter to your code base. Every single time you drop them in,

code quality is enormously consequential to them. Because if they have a code base

that's hard to make changes in, AI is not going to produce good code. So in order to

get the most out of AI, you need a high quality code base. That means that a quality code base

matters more than ever, because if you can get agents to run AFK and produce quality code in

a quality code base, then you've done it. You've unlocked the bounty of AI. It's available

to you if you have a good code base. So I think it matters more than ever.

Okay, thank you so much. That was really fun. Practical question for the course. Can you

explain and demonstrate reset, cherry pick and pull? There's a video that does that for you.

So good luck. Best of luck with the course. I'm going to be hanging out in the discord

all day and all week. So any questions that you have, feel free to ping me.

Thank you so much for joining along. Yeah, code base. Exactly. So garbage in garbage out.

Exactly. There are 335 of you in the chat. This VOD is going to stay where it is on YouTube.

So you'll be able to see it and enjoy it for all time. You have lifetime access to the

content and yeah, see you in the discord. Nice one, pals.


### 048-AI Coding for Real Engineers p48 048 AI Coding for Real Engineers Office Hours (Day 1 Afternoon)

I was very briefly streaming onto the wrong thing. I streamed onto the office hours morning chat.

But hello everybody, we're here. Thank the Lord. I was just talking to myself in a very lonely way.

But now I can see we have a wonderful chat going. We've got extremely well populated Q&A.

So well done everyone for coming ahead of time, getting all your questions in.

And hello. Welcome, welcome to the afternoon session of Cohort 4.

Hello. Montreal, Canada. I saw Nice earlier. I've been to Nice.

Cordoba, Brazil, Oslo. How we doing? Germany.

I did feel very lonely, extremely lonely.

You know, there were 350 of you in the chat this morning. This is big.

Some biggest, my biggest cohort have ever run.

I'm hoping that means we get better questions.

Tokyo, Uruguay, Texas, Sao Paulo, Ohio, Argentina, Colombia, New Hampshire, Rochester, Poland.

Where in Poland are you? Poland, a deeply underrated country.

Some of the best devs I know come from Poland. New York.

Okay. How are you enjoying the cohort so far?

Have you had a chance to look through some of the stuff yet?

You've got a whole bunch of material to go through until between from now until our next office hours.

We are going to work through these questions.

I'm hoping I'm going to be able to answer them in a way that's illuminating

and point you back to the course where needed.

Simon Wallace, Oxford UK. I'm in Oxford UK.

What are you doing over there? You should just be, you know, you should just listen at the door.

Right.

Rod's Love. Yeah, I was in Rod's Love.

I've been to Rod's Love. I've got a very good friend in Rod's Love.

Right, folks. Well, let's do it.

Let's get it going.

Let's see.

270 of us. Wonderful.

Well, then let's go to question number one.

How do you ensure that your agent will code in DDD and respect the best practices?

You seem to be against rules and large skills.

So how do you do that?

So DDD, for instance, for those who don't know, is domain driven development.

It's essentially a quite wordy.

This is the blue book of DDD.

And it's quite a wordy and in-depth way of thinking about code and thinking about architecture.

And it happens to be absolutely brilliant.

It's very, very good.

Now, when you think of DDD, it has a lot of concepts that the LLM probably knows about,

but it might know about them in its parametric knowledge.

If you think of agents, they've got two sources of information.

They've got their parametric knowledge and then they've got their contextual knowledge.

Parametric knowledge is stuff they were trained on.

The contextual knowledge is stuff that has been passed into their context.

Right.

So when you're working with your agent to try to follow a set of best practices like DDD is,

how do you get it to do it?

And the way you do that is basically every session that I do with an agent has some kind of skill running in the background.

It's either going to be a grill me skill or a grill with docs skill.

It's going to be a diagnose skill if I'm diagnosing some bug.

Might even be a do work skill, which we'll talk about in the course.

But there will be some rule running in there and particularly a review skill as well.

So how do you get the agent to follow along with your best practices is you make sure they're encoded in each of the skills that you use.

You make sure that if you really care about something, it's mentioned in the planning phases.

For instance, I've started really caring about test seems recently, which we'll talk about in improved code based architecture.

Test seems are the places at which you write tests for your application.

And so now I've made sure that everything that sort of touches code that touches planning mentions test seems.

And hello from Chiang Mai.

I've been to Chiang Mai too.

So it's not so much I'm against large skills.

I think if you have a software practice and you want it to be coherent, you need to encode it into every skill that you use.

And if you're if it's still not working, then I would invest more tokens in review.

This is something I've been doing quite recently.

I might add another appendix onto the onto the course, actually, to talk about this.

Because as I've what I've noticed is as I spend fewer tokens in implementation or let's say cheaper tokens in implementation,

maybe use a slightly crapper model during implementation, I can actually if I do that and then have an expensive agent review it,

review it against the spec, review it against my coding standards, review it against my best practices.

I tend to get better output than if I just try to stuff all of those instructions into the implementation.

So I might add an appendix to talk about that.

So that's what I think is you should essentially encode it into all of your skills and it doesn't have to turn them into massive skills

and use a review agent to make sure that they're working properly.

To ensure the code quality, would you recommend to use TDD method in order to create only the code needed to get the expected behavior?

Yes, we talk about test driven development in week two.

That's in the feedback loop section.

So I will defer to that.

I found that TDD and especially red green refactor is an amazing way of getting higher quality code because you're essentially agents do really well

with feedback loops and you're just giving it the feedback loops it needs to succeed and then it just goes and succeeds.

So pretty sweet.

Do I have a good setup for sharing coding standards via skills between reposing keeping them updated?

Not really.

Not really.

I'm looking I'm hoping this is something that tooling is going to solve.

I don't have a huge problem with this because I only have like two or three repose that I actively work on for my job.

So no, I don't have an amazing setup.

Also, I'm only one team member really.

So I don't have anyone I need to share these skills with.

I think there's lots of different ways you could do it.

It's essentially code, you know, so you could have an NPM package which you just get people to update and on a post install hook could, you know,

just hook it into the project.

That's one way of doing it.

But I don't have a sort of thoughts on best practices here.

Maybe I should.

I'll have a think about that.

Installing skills.sh over time will fill up your local env.

How do you keep things tidy?

Remove unused, avoid mixing up the wrong ones, etc.

You've just got to be really, really paranoid about your context window.

This I hope is something that you will get from this course is feel nervous every time something enters your context window and you don't want it there.

Right. So skill descriptions are in your context window.

This is something I've been trying to improve with my skills recently is the descriptions were a little bit wordy.

Some things are in the context window that don't need to be there.

And so you just got to be super vigilant about all the skills that you put into your context window really.

And I would be especially nervous about full on frameworks that are just kind of hanging out in your context window ready to be used if needed.

Unless you're going full on and like, you know, you know, okay, I'm using superpowers.

I'm going to use superpowers all the time.

Just get rid of them if you're not actively using them.

This is a great question. Do you worry about losing your ability to code?

How do you prevent that? Let me just get up a diagram.

So I think of there as being two types of coding.

We have essentially tactical coding and then strategic coding or programming.

This is a definition that comes from John Osterhout's philosophy of software design.

Now, if you think of tactical programming, it's kind of like the sergeant on the ground.

They are the ones running about doing the shooting, doing like, you know, corralling the local troops.

They're trying to win the battle.

It is short term. It is just focused on the here and now.

It is trying to get the thing done.

Then you have strategic programming.

You have the general who's not just thinking about this battle.

They're thinking about the war, right?

They're thinking about the long term.

They have big picture.

They're not too focused on the ground.

Now, I think that some people identify more as a tactical programmer.

They are, you know, a code monkey.

They're just trying to fix the thing that's right there in front of them.

And tactical programming is relaxing.

Actually, it's pretty chill, you know, you just got to do the thing that you,

you know, like the ticket says to do, right?

You have a, you know, a very narrow thing that needs to be done and you go and do it.

Strategic thinking is difficult.

Strategic thinking is very difficult to develop as well because the feedback loop is really long,

you know, if you choose to design the thing this way, how will you know if the design is wrong?

You know, it might take a long time for that design to turn out wrong and that might only

bite you so nine months down the line.

There used to be a running joke where, I mean, maybe it's still running,

where developers would often, you know, make these strategic mistakes and they wouldn't

know that they were mistakes until like they because they'd switch jobs too soon for

their strategic mistakes to bite them again.

So they'd never learn.

So going back to your question is I think of development and I've to be honest,

always thought of development as strategic, right?

Which is that I've always loved that part of it.

Thinking about how to improve things over the long term, thinking about improving

velocity, not just solving the problem today, but solving the problem next week,

next month, next year.

Tactical programming is obviously fun.

You know, I like it, but it's not the reason that I love being a dev.

I love the strategic side of it.

Now, the danger of AI is or the danger of identifying as a tactical programmer is

AI has eaten tactical programming.

Tactical programming is now best delegated to AI.

There's no reason why you should be doing tactical programming yourself

unless it's a really, really hard bit of programming.

You know what I mean?

You need to be in the loop with the with the agent or whatever.

So it's, you know, it's eaten 90% of tactical programming, 95%.

But AI is not very good at strategic programming yet.

You need because AI is kind of limited in its context window.

It's very good at that kind of narrow firefighting approach.

It's less good at thinking long term, understanding the roadmap.

And the strategic programmer now is the one who's going to be best able

to get the best use out of AI.

And so I think of myself, I've always thought of myself as a strategic programmer.

So I'm not really scared about losing my skills because I know that these skills

that I've developed are very, very important and useful.

But and the tactical stuff is fun, but it's not why I got into programming

to begin with, you know, hopefully that answers your question.

Where I am, there we are.

Re referencing edit in day one, if expanding the context window

with newer larger models only adds to the dumb zone, what is really the point?

Well, I don't know because I don't work at Anthropic.

I think that having a 1 million context window limit is good for marketing.

There's lots of decisions that go into where that's where they put the context window, right?

The higher you have your context window, the if people go into like the later parts

of that context window, you know, like this, then you can charge them more, right?

Because they're not just charging for these tokens.

You're charging for this whole stack of tokens.

That's nice.

Like this idea of the smart zone dumb zone is my working assumption and I use it

and I like it and I think you should use it too, but it's not universally shared by everyone.

So there's, you know, this and the smart zone will probably creep up to that point.

So it might be a kind of optimistic thing that they're doing that.

But yeah, I don't know if there is a point really like it's not.

Yeah, it's sort of marketing is a bit of fluff.

I don't know why they've done it.

You know, GPT 5.5 as far as I know just goes up to 400k tokens,

which feels more reasonable to me.

So I don't know.

When a new Opus model is released, do I start using it in my existing workflows automatically?

Do I evaluate it first?

How do I evaluate it if so?

I like to be on the state of the art for these things mostly because I'm just scared of being left behind.

I'm my incentives are slightly different to other people's,

which is I want to be teaching the most up-to-date thing.

So yeah, I pretty much adopt them day one.

I don't do any evaluation on these models.

I think of model evaluation really as like employee evaluation, you know,

I think I mentioned this in the Discord actually, which is that

sure, one employee might be different to another employee,

but you should be setting up processes so that any employee can succeed in your workspace.

You know, you should be at a level above the model in terms of your thinking

so that you can slot in different models and sure,

you can evaluate them maybe and just sort of gather data on how they're doing over time.

But you should be able to switch model providers quickly.

What is my approach to writing skills and knowing when to surface a new one?

Mine seem to be extremely concise yet effective.

I am still working on my guidance here in terms of how I recommend you think about skills

and how skills...

Hmm, what's the best way of saying this?

Yeah, and what the best practices are for skills really.

Like, I think it seems obvious that concise skills,

if you can get away with it, are better because shorter skills mean easier to...

What am I saying? My brain's gone.

They're easier to evaluate. They're easier to security check.

They're easier to change as well because there's fewer things going on.

And so, yeah, I tend to write skills when I find a gap in my process

that I think needs a reusable command to sort of go again and again and again.

So, for instance, I wrote a diagnose skill relatively recently

because I wanted to improve the way that my agent was diagnosing bugs.

And so this one, it sort of attaches a feedback loop to the whole thing

and it goes through and fixes the bug using that feedback loop.

So I think there's a mind virus out there that skills need to be long.

I don't think skills need to be long. I think concise skills are great.

But beyond that, I'm still working on my guidance

on how you should write skills and think about them.

How to best manage multiple parallel agents,

some dedicated orchestration tool, simply multiple workflows.

We're going to touch on this in the course.

Soundcastle does a great job at this.

You can run multiple agents with work trees, just like ploughing through work.

Yeah, we'll touch on it.

How would you handle context over a workflow spanning multiple humans

with separate AI tools, from product owner to design team to devs?

So, it's a tricky question to answer.

Essentially, you need to think about there being...

Every time you touch an AI or every time actually you do anything now as a team,

you need to generate some kind of handoff artifact.

So let's say that you get on a call with a bunch of devs

and you chat about a thing that you want to build.

Then you can take the transcript of that call, summarize it with an agent,

and then boom, you've got a handoff artifact

that you can then pass to a grilling session to hammer that out.

I would need to know a bit more about your workflow, I think.

But essentially, what you need to be doing is capturing the information

that you get from conversations, from collaboration,

and saving that somewhere that's accessible to the agent.

Shouldn't be just in the repo, but maybe accessible via a custom MCP server

or something similar to that,

where you have some kind of context pointer

that the agent can use to grab that information.

Let's say that you have a GitHub issue,

and that GitHub issue is describing how to implement something.

Then you can essentially use a context pointer from that GitHub issue

to link to the transcript of the thing that you talked about originally.

So the agent can fetch the deeper knowledge if it needs to.

In school, we learned about primary and secondary sources.

The primary source is the actual conversation that you had.

This is like in history, right?

Like two people actually chatting to each other,

you get the transcript of what they said, that's a primary source.

You have someone that summarizes that for you, that is a secondary source.

So you can think about the agent having the primary source being the code base,

but then links to maybe a secondary source of a summary of the conversation

linking to the primary source, which is the actual conversation.

And that kind of progressive disclosure,

which you may have learned about from the stuff if you've been through it already,

that's really, really useful for giving the agent what it needs.

It's a long answer, but you get the idea.

Should I just grill with docs to PRD two issues in one session or in separate sessions?

Grill on the resulting issues again or just TDD?

So the way that my setup works is that you use grill with docs to essentially,

if I pull up the diagrams actually,

let's see, in the seven phases.

Here we go.

So in my seven phases of development,

the first one is you grill on some kind of idea.

So you use grill me or use grill with docs,

and you essentially create this context window full of questions and answers

about the thing that you're going to build.

From there, if we ignore research and prototype for a second,

you should in that same context window,

create some kind of handoff artifact.

So you need to take that and turn it into a product requirements document.

Because if that's the primary source, the grilling,

and you're creating a secondary source from it,

a sort of summarization of it to then go and build something from it.

Now, once you've got the PRD,

it's debatable whether you need to clear the context for issues.

If you have context window left over before the dumb zone,

let's say, then you don't need to clear the context before you go ahead and do issues.

So you're just turning the PRD into individual tickets from there.

Oh, sorry, turning the PRD into individual tickets from there.

So I would recommend if you can get away with it doing all of them in one session,

but you definitely never want to clear the context between grill and PRD, right?

If I just mix these up.

If you clear the context here,

then you're just getting rid of all of the amazing context

that you generated during the grilling session.

Because the grilling session doesn't itself create a handoff artifact.

Like the PRD is the handoff artifact.

And if you're just creating a PRD from nothing,

then what's the PRD going to say?

You get the idea.

Oh, sorry, there was another part to that,

which is should you grill then on the resulting PRD?

I don't think so.

I think you can get a bit too hardcore with like grilling the plan,

you know, or grilling the summarized artifact of the grilling that you've already done.

At that point, once you've decided where you want to go,

just implement the thing.

And once you've got a working implementation,

you can do QA after that.

What are the strategies best for tackling the dumb zone problem in medium to large projects?

My code base takes 30k tokens to start leaving me 70k smart zone.

So I think there's a misnomer here,

which is or something you're getting wrong in this question,

which is that if you have a large project,

it doesn't necessarily take more tokens to explore than a smaller project, right?

Let me explain what I mean.

For those who've done the day one material,

you'll have seen that if we look at this as our setup, let's say.

Now, let's grab a few of these.

So let's say this gray one here is going to be the system prompt

and like all of the stuff that comes by default in your harness.

So skill definitions, system tools, all that stuff.

Then this blue one here, actually, let's make this.

Yeah, let's make it blue.

This blue one is the exploration phase.

So in the exploration phase, it's looking for information

that's information in the code base, looking for the correct files to find.

And then let's say we've got this yellow one, which is implementation.

And then let's maybe say a pink one, which is review, right?

And that's kind of how a normal session should look, right?

Now, if we think about large and small code bases,

do we always think that a large code base

is going to mean more reviewing time or more exploration time?

I don't think so.

I think that large code bases can be easy or hard to explore.

I think a large code base can be easy to explore

if you've correctly set up your agents.md to point it to the right files,

if you've got it well organized in terms of file structure,

if you can find things, and if it's not kind of like rotting

with excess documentation.

Whereas a small code base equally can be hard to,

hard or easy to explore as well.

So what I would say is you need to think about

making your code base easy to explore,

which is something we do touch on in the course

in a couple of different ways, both with a shared language

so that you can, like you and the AI are both talking the same language.

That means that because you're talking the same language,

it can use that language to find correct terms in your code base,

find the correct implementations based on things,

and also that you use deep modules as well

to make sure that you're essentially able to,

instead of having lots of tiny modules which are hard to explore,

have fewer large chunks which themselves then break down into smaller ones.

That will become clear during the course, I think.

So,

tackling the dumb zone problem in medium to large code bases,

I think is the wrong way of phrasing it.

I think you instead need to think about

easy or hard to explore code bases.

Are there meaningful differences between using handoff

versus forking the current conversation with branch fork

and then running compact?

Yeah, there are a couple of differences.

Handoff is just more flexible.

My handoff skill, if you've not used it yet,

it just creates a markdown document based on the current conversation.

So it creates a handoff artifact.

Let's go with this one.

Just like that.

So let's say we've been in the grilling session,

we create a handoff artifact,

it saves it to a temporary directory,

and it's just a markdown file with what was talked about in the conversation.

Now this means that you can do a few things with it.

You can, don't need to save it into a markdown document,

you can save it to a GitHub issue.

You can pass it to a different agent.

So you don't need to like do it within Claude,

you can say, okay Claude,

hand off to Codex for the implementation,

and it will do it because it's just a markdown document.

You can also say, I found a bug in a different project

or a different folder, maybe that I'm relying on,

let's say, let's hand off so we can fix it.

So it's just very, very flexible.

Whereas if you were using the branch fork,

then it's only within the same project.

And it's only within the same agent.

Thoughts on using an expensive agent for planning

and a cheaper agent like DeepSec v4 for running the AFK task

for those who want to optimize on cost.

Now, it's not a very fun thing to say,

but I think at this moment in time,

you should not be optimizing for cost,

you should be optimizing for quality.

If you're optimizing for cost,

you're going to end up with shipping,

as you reduce the quality to reduce the cost,

and let me get the phrase right here,

to reduce cost, you're going to need to reduce quality.

And as soon as you get under a certain bar

in terms of quality,

you are then going to need to spend more time

fixing the code that the agent wrote

than actually that you save by having the agent run AFK.

And that's incredibly dangerous.

And it's also hard to spot.

Because if you optimize for quality instead,

if you instead go,

okay, I'm just going to throw a bunch of tokens at this

to make sure that we get high quality,

it means that you are saving your own time.

But if you don't do that,

if you optimize for cost instead,

then you are going to be spending more of your time

in order to fix the stuff the agent broke.

And essentially, I value my time too much

to want to spend it fixing agentic mistakes.

I just don't want to do that.

What I want to do is I want to see working code come out,

and that's all I want.

And I'm willing to spend a little bit more to get it.

I think that's what most enterprise folks should be doing.

Could you provide a complete roadmap for absolute beginners

with zero coding background and relying on AI in this cohort?

Where should they start from?

So zero coding background,

I think one of the prerequisites for this cohort

is that you should be able to read code, right?

You should be able to have a,

like, have a sense for what a variable is,

have a sense for what Git is,

have a sense for all that stuff.

I would be really interested in getting your feedback

on a new skill that I've been putting together.

I'm just checking my...

Something looks slightly wrong.

Hang on, two seconds.

Oh, yeah.

The light in the background there is actually very responsible

for the colour balance of the shot, if you believe it.

That was just... I saw that on the thing.

It was bugging me.

What's up from Medellin?

I was talking about...

I would be really interested in you testing out a new skill

that I've been putting together, which is my teach skill.

Now, this teach skill essentially teaches you something.

I've kind of put myself out of a job here in terms of

getting AI to...

I've encoded my best teaching practices in an AI for you,

or in a skill.

And what it does is you run it inside a workspace,

inside a folder that you dedicate just for this,

and it will create long-running resources

to track your progress, to track good resources.

And I'd be really interested to see how you get on

using this to learn to code.

Because really, your mission...

I believe that every time you learn something,

you should have a mission about it.

Your mission is to essentially get really good at agent encoding

so that you can build something, right?

And if you figure out what your mission is,

then you'll be able to use this skill really effectively

to just learn to code.

I'm really intrigued by how you get on with it,

and I'd love to hear any feedback you have about the skill.

So I'm sort of deferring to AI here.

I hope you don't mind.

It is something that's on my mind.

I do have a lot of kind of complete beginners

wanting to take this course,

and I don't have any content that I've produced

that is the complete roadmap.

And maybe I should produce some.

So I've been using...

Okay, next question.

I've been using Anthropics' own skill creator skill

to create new skills,

but they look much more verbose than yours.

Should I write them manually instead?

I believe that every skill you write,

you can have a first pass with an AI

to sort of generate some, you know...

have the sort of first basic idea,

but definitely you should line by line

check every line of it

because it's very easy to get duplication.

The skill creator skill uses like evaluations.

I just wasn't too keen on using it.

That's why I wrote my own.

Yeah.

How to efficiently use the handoff skill?

Paste the handoff inside a new session

or tell the agent what to do,

and it should be picked up.

Just...

You can, I think, follow my tutorial in the course,

but yeah, you just paste the link

from the markdown file you've created

into the new session

and it will pick it up.

How can we meet career progression expectations

in this new era?

How can we demonstrate our worth and seniority,

especially if our manager sees it as all AI?

Hmm...

It's a good one.

First of all, I think that career progression expectations

have probably changed a bit.

You know?

I think that...

It's going to be...

easier now to see...

I think that AI makes really good developers

a lot better.

It means that if you can demonstrate

these kind of like strategic skills...

Where did they go?

I don't know where my strategic skills went.

Yeah, here they are.

If you can demonstrate strategic skills,

then wow, you are going to be like

extremely good with AI

because all of this tactical stuff

that usually takes the time in development,

you're going to be able to

just pull in an entire army of AI

to handle the tactical stuff for you.

So...

And again, this is an optimize for quality thing.

If you can optimize for really high quality code,

then you can produce so much more than other people.

So these skills will make you stand out because

I mean, if management thinks it's all AI

and you know, you can just like

go away, you know, you're not needed anymore.

That's crazy because

you just got to be talking about the strategic skills

that you're demonstrating and

talking about how you've created these

sort of outer harnesses for AI to harness them.

So

personally, I think that, you know,

career progression is often all about

how much you talk yourself up

and you've just got to be talking up

these skills to management saying that

yeah, the AI is doing it, but it couldn't do it without me.

It's doing the tactical stuff while I'm doing the strategic stuff.

What techniques can limit the scope of PRD files

and maintain a good size when sliced?

I'm considering context and perhaps the need for more micro tasks.

I think the

the vertical slice is traceable.

It's stuff is this week, I think

and that should answer it for you.

Do I think the memory.md managed by Claude code is useful

or does it cluster the context window?

Do I ever update it and manipulate it in any way?

I hate it.

I hate it.

They used to have a config option to turn it off.

I think in the course I mentioned that I sort of,

you know, you might like it

if you do X, but I've just grown to hate it.

I have this context paranoia that any time

that something enters the context window

and I don't know about it, I hate it.

You know, I want full control over the context window.

I want to know everything that's going in there

and this memory.md is just always crap.

Like every time it intervenes, every time I notice

that it's managing something, I just go in and delete all of it

because it's just garbage.

So no, I don't like memory.md at all.

Rant over.

How do I see AI changing the software development life cycle

like design, handoff, QA, testing, et cetera?

Well, I'm sorry to harp on about this, but like

how do I see it changing it?

Before you would have if we imagine that

let's just go down here.

Let's say that in the early stages of a project,

you've got a period which is like planning, right?

Let me use this one.

You've got planning and then you go ahead

and you've got some coding, right?

You've got coding and then you've got some QA, let's say

and usually these things are sort of happening

simultaneously as well relatively.

So you're QA-ing the one thing while they're planning the next thing.

And usually you would have fairly long breaks,

you know, maybe days where you're just coding, you know,

and then you do a bit more planning, do a bit more QA.

And if I just sort of expand this out a little bit.

Now the way this now goes is that implementation

has essentially gone to zero time, right?

Or very little time.

You can essentially just say, okay, because we've got AFK agents now,

you can just do this.

And now the lifecycle now looks more like this.

So there are far fewer breaks when it comes to implementation,

you know, before you would have this sort of natural gap

in the process where you needed to actually implement the thing

and that would usually take a lot of time.

So we are now going to be doing a lot more planning

and a lot more QA because that's just because implementation

now takes zero time in theory.

So yeah, that's going to change things, right?

Because how we estimate things is going to go out the window

because implementation is so important to,

used to be so important to how we implemented stuff.

So yeah, I think the main stuff though,

like the planning is all going to be pretty similar to how it was before.

AI assisted, of course, and AI kind of like filling in some of the gaps

and maybe I think making things better.

But yeah, it's going to change a lot, especially on how we estimate things.

How do I use AI for learning or researching information?

How do I take notes and create diagrams, pictures for learning?

I do all my research without AI actually.

So I just read books and I contribute to an obsidian graph,

which is what I use to build my stuff.

I think of my learning as my own really.

I think of my skills as sort of very important to cultivate

in a way that's very intentional.

I don't want AI sort of flooding me with a bunch of stuff

and taking charge for me.

I've tried to encode that in my teach skill as well.

Yeah, I just take notes in an obsidian graph basically.

What's your take on the hammer nail scenario

that people have ended with in the workplace

where everything should be a skill or everything should be AI first?

I think, yeah, we've got a golden hammer now, basically.

Why wouldn't you try to hammer every nail that you can?

If we hurt our thumbs a little bit, then, you know,

it's still pretty cheap to try, right?

So there is definitely a thing of squeezing AI into every possible place.

I'm definitely feeling that.

But also, when I try to do things like that,

half the time they actually work and they're really good.

So, you know, for instance,

I've been playing around with this thing over the weekend

where I would label a task in my Todoist app,

which is what I use, and then that would get picked up by a webhook.

It would go to a server and the agent would essentially help me

to not complete the task, but give me everything

I need to make completing the task easy.

So searching my Gmail for the correct emails,

searching GitHub for the correct repo,

for the correct line of code,

searching the CMS for the AI hero to figure out exactly what I need to change.

So kind of like you just label it

and it will go and explore on a kind of remote server

using Soundcastle and ping back the info.

So I haven't done it yet,

but that's something that I'm wondering,

that's a hammer that I'm applying to this interesting little nail

and it might change my life forever, you know,

like it might just be something that I use every single day for the rest of my life.

So the cool thing about AI is that it turns tasks

that were previously immersive, tasks that you needed to be there for,

into process tasks, into tasks that you can just kick off

and then they will just complete on their own.

So it turns things from human in the loop to AFK essentially,

and that's incredibly attractive because,

I mean, it just is, right?

You just save a bunch of time, you become so much more efficient,

you get to do a lot more useful things with your time

than just trying to find the bloody email in Gmail or something.

So, yeah, that's my take really,

is that it's kind of, we've got a golden hammer,

let's hit some stuff with it.

Mark has answered. There we go.

What is my approach on boarding an existing project?

Grill with Docs is good for build, scratch,

and the ecosystem needed for developing new consistent features.

Yes, so Grill with Docs, you can just essentially say,

create me the documentation needed

and it will grill you about what it needs basically.

So, yeah, the idea of the skill,

it's supposed to be incrementally adoptable.

If you're not touching or not touching parts of the system

that you don't sort of fiddle with very much,

then you probably don't need a shared language

for talking about them.

You only need a shared language for things

that you're actually going to edit and implement.

So, yeah, in theory, you should just be able to adopt it.

Apart from skills, what are your favorite

most used prompt add-ons?

Steal man this and go up a layer of abstraction.

Please list all.

Hmm.

Most of the things I do, I turn into skills

because I just like to have them there to remember them.

But yeah, I've definitely said steal man this argument

a bunch of times.

Oh, commit this, I suppose,

is another one I use every time.

I sometimes say zoom out as well.

I think I actually did put that in a skill.

Um, I don't know.

It's a good question, but I don't have any good responses.

I'm sorry.

Yeah.

What are the best strategies to convert a pre-AI code base

to be AI ready?

We're going to learn about this in week two, actually,

which is that good code base design for humans

is also really good for AI.

So what that means is if it's a legacy code base,

if it's a code base that's really hard to manage

and hard to work with, then the same stuff

that worked with humans is going to work with AI.

So essentially, the same stuff that Michael Feathers

was talking about in 2004, working effectively

with legacy code, adding more, adding test scenes

so that you can test parts of the code

before you make changes to it, before you refactor it.

All of that stuff is still going to be great with AI.

Essentially, the end goal is you want a code base

that's easy to make changes in.

And if your code base is not easy to make changes in,

then AI is going to struggle and you're going to struggle.

So essentially, the best way to do it

is to improve your testing, improve your feedback loops,

improve your automated checks.

And that's kind of how to do it, really.

You have a commit subagent ref? Oh, honestly.

So what are my thoughts?

Let's have one more question and then I'll zoom off.

What are my thoughts about the new dynamic workflow?

Would it make Soundcastle obsolete?

I don't know, to be honest.

I haven't sort of messed about with it very much.

It seems to be really good at sort of fanning out

lots of parallel stuff.

I am intrigued by it, but I've not really tried it yet.

So there we go.

That was 45 minutes just flies by, doesn't it?

I mean, these questions are so, so good.

Thank you so much for asking them.

I'm really excited to see how you guys do this week.

I'm going to be in the Discord all week chatting to you.

Thank you so much, 300 of us,

314 of us concurrent viewers in the chat.

This is brilliant.

Honestly, I love running these cohorts so much.

It's so great seeing people work through this material,

bringing up these questions and kind of,

I always find it really enlivening.

Always gives me tons of ideas for new content,

all that stuff.

And I hope that you got your question answered

or you had some interesting,

interesting, oh God, my brain's really gone.

What happened there?

We had some interesting discussions.

We definitely did.

Thank you so much.

This will be available for view in future.

You just come to this page again and it will be here.

Nice work, pals.

See you very soon.


### 049-AI Coding for Real Engineers p49 049 Is Code Cheap Day 4 Feedback Loops

I've got a thought experiment for you. There's a lot of people out there who are saying that

the AI age is a new paradigm for software development. That we need to chuck out all

of our assumptions about how code works, what good code bases look like. Because

agents are so fundamentally different from people, you know, from human developers,

that they need entirely different guardrails, entirely different setups. In other words,

the old rules are for boomers, and now, you know, we need to find new ways of

And a lot of this comes down to the mantra that code is cheap. When you have an AI agent that can

basically churn out tons of code, then the production of code is now so much cheaper,

so we don't need to worry that much about bugs, because the AI will just be able to blast

through code and create code faster than we've ever been able to see before. And so,

the argument goes that software quality matters less because you can just always churn your

way out of software quality issues. If you've got a bad code base, then the AI would just be

able to fix it by just blasting out more code. Now, I think this is incorrect. I think that

software quality matters more now, and that AI agents are more sensitive than humans to software

quality. And this massively affects how we should design our code bases and design our

systems to take advantage of AI best. But first, let me start off by defining what I

mean by software quality. Is the code base easy to change? This definition comes from this

book, The Philosophy of Software Design by John Osterhout. I've probably absolutely

murdered his name there, so sorry, John. But John makes the argument that if a code base is easier

to change, then we can think of it as a better code base. In other words, is related information

grouped together in the code base? How likely is it that the change you make to the code base

will have unintended consequences that ripple outwards? And also, what are the feedback loops

like in the code base? If you make a change in one place and you accidentally cause a bug

somewhere else, how likely are you to find out before you ship to production? Now, in a perfect

world, we would always have perfect code bases. In other words, our code bases would never be

hard to change. They would always be well designed and really easy to change with great

feedback loops that we would always be able to catch bugs with. So the truth is that most

times most people are touching a code base, they are making it worse, not better. If you

thoughtlessly make a change in a code base in order to fix a bug or like build a new feature,

let's say, and you're not thinking about continually improving the code base or keeping it

in this easy to change mode, then you are probably making that code base worse, not better. This

concept comes from the pragmatic programmer and this is called software entropy. This is the

idea that software tends towards getting worse, not tends towards getting better. And for anyone

who's worked on any reasonable size of code base, this will ring true to you. Software

developers don't work in a vacuum. There are pressures on you. There are time constraints.

There are times when you just need to ship something immediately and you don't really care

about the long term consequences. Or there are times where you're just having a bad day and you

just need to get your work done. And on those days, then you are probably going to be having

a negative effect on the quality of your code base, even though you're shipping features.

We can think of this kind of like a clutch meter where we have it just slowly rising here

on every single commit. Now you can intervene and do refactors and redesigns that help stop

the clutch, such as this commit here, which might introduce a new part of the test suite or

refactor the code to make it easier to change. But every commit that is not this thoughtful will

eventually be increasing your software entropy again. Now guess what? In the AI age, AI massively

increases the amount of commits you can do, but currently it does not do a great job at these

commits, the kind of entropy saving commits. Figuring out a better software design to prevent

software entropy is one of the hardest tasks a software engineer can do. It's harder than

building new features. It's harder than fixing bugs. And so it makes sense that AI is not

very good at this yet. And so in its current state, AI is a software entropy accelerator.

This is especially true when you think of the three things that go into any AI coding session.

You have, of course, the initial prompt, the thing that you're trying to get the agent to do.

You then have any steering mechanisms you're using like skills or Claude.MD. But the biggest

one, the most important one is your code base. Agents are much more likely to copy your code

base than any steering that you do because the code base is the source of truth. And so if

there are bad patterns in your code base, even if you're explicitly warning about them in your

steering, it will tend to copy the code base by default. This means that AI is maybe even more

susceptible to cludge than human developers because it will just blindly copy whatever's

in your code base without applying its own taste to it. And an AI in a bad code base will

have access to way fewer feedback loops. And so it won't know when it's writing bad code.

Humans, because they can develop memory about a bad code base, can kind of survive it and

work around it. And because they can understand what weird patterns a code base has, they can

produce fewer bugs and higher quality features within a bad code base. But AI, remember,

is stateless. So again, it is more susceptible to a bad code base than a human is. A code

base that is hard to change is a killer for an AI agent. I mean, it's a tale as old as time.

You put garbage in, you're going to get garbage out. So in my opinion, because software

entropy is a fact of life, and because AI is just not really capable at the moment of creating

these beautiful code base saving commits, and because it's so unusually sensitive to code base

quality, then I don't think we can say that code is cheap. Cheap code will just accelerate

you to the point where you've just maxed out your cludge meter, where the code base is

complete garbage and impossible for an AI to change. I know that you have worked in code

bases like that. I have worked in code bases like that. And the only way you can get around

it is by banging your head against the wall repeatedly until you're able to make the change

or able to function within that code base. AI, because it has no memory, has no chance.

And so in the AI age, code quality matters more. And in this section, we're going to talk

about increasing the quality of your code through feedback loops, which are the essential

way to prevent AI from increasing your software entropy. Nice work, and I will see you in the

next one.


### 050-AI Coding for Real Engineers p50 050 Steering Agents To Use Feedback Loops With Skills Day 4 Feedback Loops

Now we know how important software quality is.

How do we keep the agent on the right path?

How do we increase the quality of what the agent is producing

so we don't end up in a software entropy death spiral?

Well, one thing we have already learned how to do

is to proactively steer the agent

by using agents.md files or using skills.

But this kind of increases the probability

that an agent will choose the right path.

Wouldn't it be better if we could deterministically

always enforce something for the agent

to increase its quality?

So this is where feedback loops come in.

The agent produces some code.

We give some feedback to the agent

based on the code that it's produced.

And this then helps the agent to produce more code

which goes again through the feedback loops

until it's produced something of sufficient quality.

Now this, of course, is something that we, as humans,

have been doing for a long time.

Great engineers don't trust their own instincts

and don't trust the quality of the code

they're producing.

So they produce a lot of feedback loops

in order to improve their own quality.

So we're just taking the same tried and tested

software practice and applying it to agents

instead of humans.

Now the more feedback loops

and the better quality feedback loops you can produce,

the better the output is going to be.

A classic one is using a strongly typed language

like TypeScript instead of a weekly typed language

like JavaScript.

With TypeScript you're going to get errors

if you create a typo or you use the wrong type

which is feedback the agents can use

to write better code.

Another really important one

is any kind of automated testing.

Automated tests actually run your code

and check that the logic works how you expect it to.

And so the higher quality test suite that you can produce,

the more signal you're going to be giving the agents,

the better feedback, the better quality code.

And so testing strong types are essential

for getting high quality code out of agents.

Inside our repo, we've already got some type checking

and tests set up.

We already have a script for type check here

which runs React Router TypeGen and TSC.

In other words, it sort of gets the types

ready to be run and then checks the entire repo

using the TypeScript CLI.

Then we've got this test command which runs vtest run

which runs essentially the entire test suite

in the repository.

You may already have noticed that we have services

inside our application which each have some kind

of test service next to them.

For instance, purchase service

has purchase service.test.ts.

The question then becomes how do we encourage the agent

to use these feedback loops to improve its code?

How do we get it to work in this fashion

where it basically asks for feedback

on every piece of code that it produces?

Now of course we could add these instructions

into a claw.md file and so it's in every single session.

But not every single session needs

to run the feedback loops.

So what I prefer to do is create a skill instead.

In nearly every one of my repos

I have this do work skill which I invoke

every single time I make a change to the repo.

This do work skill basically has a list of instructions

for the LLM to follow that mimic how I work

when I'm contributing to a repo.

In the first part of the skill I get it to plan out

what we're going to do.

This is not always necessary because sometimes

I'll be working to a pre-written plan.

Then I'll get it to implement the change.

Then I'll get it to seek feedback

on what it just implemented.

And then I'll get it to commit the code

to the repo with a commit message.

This is the nicest way I've found to steer the LLM

to use feedback loops and to use a kind of loop

in the repo that I can then iterate on.

And in the next couple of exercises

we're going to build our own

and use it to build the feature.

Nice work and I will see you in the next one.


### 051-AI Coding for Real Engineers p51 051 Building A Do Work Skill Day 4 Feedback Loops

All right, now we understand the benefits of a do-work skill, let's actually implement our own.

We're going to go into the repo and use our writer skill skill to write a skill.

To do that, you'll need to go into a Claw Code instance and we'll need to do write a skill here.

And then we're going to say something like write a skill that creates a do-work skill

that represents a unit of work within this repository.

The skill should instruct the agent to plan out the piece of work, then implement the work,

then seek feedback via the feedback loops in PMPM type check and PMPM run test.

The final step in the do-work skill should be that it commits the code.

Once that's done, then you should end up with a nice little do-work skill in the repo,

which we will then put into practice in a minute.

So best of luck and I'll see you in the solution.


### 052-AI Coding for Real Engineers p52 052 Building A Do Work Skill Solution

Okie doke, let's run this and see what we end up with.

Now it has, of course, entered an explore phase where it's exploring the repo structure

and it's just checking out all the stuff it needs to.

And as usual, we'll check back in once it's complete.

OK, it's come back here and it's trying to put it inside my user directory instead of the project.

I want this one to be in my project because it's kind of going to be tied to the structure of my project

because it's going to ask for specific feedback loops.

So I'm going to select no here and press tab to give it some more information.

I'm going to say put it inside the project directory instead.

So let's run this and see what happens.

OK, cool, it's now doing it inside the project.

OK, it's now come back with a skill here, which is inside Do Work inside the repo.

So we can see it's doing this nice little workflow here where it's understanding the task,

read any reference plan or PRD, it's then planning the implementation, then implementing the plan.

I don't necessarily love that it's added all of this stuff to do with specific files in here.

I don't think the convention stuff belongs here.

You can be really, really concise with this Do Work skill.

You don't have to be too in-depth here.

Then it says validate. That's lovely.

And it's doing this. PMPM run type check, PMPM run test.

It's actually mentioning the things by name. That's important.

Now we are repeating ourselves a little bit here.

We're repeating until both pass cleanly.

Do not move on until both commands pass with zero errors.

In my experience, you don't need to be that harsh with AI.

Like this should be enough that it will just kind of continually run the feedback loops until it's all good.

I also don't think we need this section too.

I think we can just ignore that.

That feels too much like the default behavior.

Notice here, I'm taking a light hand in steering it.

I'm not steering it too harshly.

Once type check and test pass, commit the work.

I don't care whether it uses imperative mood or not.

In my experience, you don't need to tell it to stage only the files you changed.

And in fact, I generally don't want to give it any advice about the commit message.

Like, I don't care about the commit message that much, even if it's super long, actually, that's really beneficial.

There's one other thing I want to tweak in here too, which is just at the top, this plan the implementation.

Now this do work skill, I could run it without creating a multi-phase plan first.

Like I could run it on a small enough task that it would just be able to do it within a single context window.

But most of the time, I'm going to be running this do work on a large PRD or running it on a multi-phase plan.

So I'm going to say that this section is optional, because if we've already planned it, then we don't need to replan it here.

And I'm then going to change this top line to if the task has not already been planned, create a plan for it.

We could also optimize this section further by introducing stuff about tracer bullets and creating good plans.

But to be honest, I kind of tend to just to delete all of this guff and have a really simple instruction here.

I really, really like concise skills like this.

We're now down to just 35 lines.

The really important part here is really just the headings, you know, this five step workflow,

which will take it through understanding the task, planning it, implementing it, validating it and committing it.

Now, I'm really interested in how your skill differed from mine.

Did yours look more verbose?

What did you add in here that I didn't?

I would love your thoughts on this in the Discord.

But I bet you're now itching to test out this skill and see if it actually works, which we will do very soon.

Nice work, and I'll see you in the next one.


### 053-AI Coding for Real Engineers p53 053 Using Our Do Work Skill Day 4 Feedback Loops

Okay, we have our do-work skill cooking and I have prepared for you a PRD to test it out on.

This is the in-app notifications PRD. Instructors on the Cadence platform have no way to know when

new students enroll in their courses. They must manually check their student list or analytics

dashboard to discover new enrollments. They miss the opportunity to engage with new students

promptly. So we're going to create a notification section for instructors. I've created a PRD for

you and I've also created a plan too. This is not a massive piece of work so it actually

only comes down to a single phase here. And so it's perfect for testing our do-work skill.

So let's open up a fresh Claude code session. We're going to invoke the do-work skill. We're

going to pass in the plans in app notifications and then pass in the PRD in app notifications.

And then just like we did before, we're going to say do phase one. Now as this is happening,

I would like you to observe whether the agent is actually following your do-work skill,

following the steps you laid down. And we definitely want to check if it's running the

feedback loops too. So good luck, write down anything you notice and ask in the

discord if you run into any issues. Good luck and I'll see you in the solution.


### 054-AI Coding for Real Engineers p54 054 Using Our Do Work Skill Solution

All right, let's rock and roll.

Now it's kicking off with an explore phase, which is good.

That's what it usually does.

But we also said that we wanted to do that

in the do work skill.

So it's hard to tell whether it's obeying its own commands

or whether it's actually listening to us

and doing it because we put it in the do work skill.

Okay, we can see that it's not choosing to plan here.

It feels like it has full context.

It's now creating tasks and starting implementing.

So that I don't get in its way,

I'm gonna turn on edits for this session.

I'm gonna turn on shift tab.

So I'm just gonna let it run.

Now it is really roaring through this task list,

which is great.

And we can actually see that it's got

validate with type check and tests

already in its list of tasks.

So this is good.

Our do work skill is doing a bit of work here.

Now it has completed all of its work

and it's now asking to run PMPM type check.

And the version of Claw code that I'm on

is doing this weird thing

where it's being a bit too eager

with these permission requests.

So I'm gonna say yes and don't ask again for PMPM run

and then immediately go up into clawed settings.local.json

and modify this to PMPM run type check instead.

Because if I just allow it to do PMPM run this,

then it will be allowed to run everything,

including migration scripts and things like that.

While I'm here,

I'm also going to add PMPM run test just below it

because I want it to be able to run that anytime.

And ha ha, look at this.

It's now asking for approval for PMPM run test.

So it should in theory do that

or not need to do that next time.

So there we go.

We do have a failed test now up here.

So something is not quite working here.

The ordering test fails

because both notifications get the same created at timestamp.

I'll order by ID descending as a reliable tiebreaker.

I don't love this because it's a weird dependency to have

for the notifications order

to depend on how we're doing IDs.

But however, because we have a feedback loop covering this,

I feel a bit more okay about it.

Because in future, if we do change the setup of the ID,

then that test will probably break

before we head to production.

So let's see where it's got to now.

Okay, it is now committing the code.

A lot of people feel quite squeamish

about allowing AI to commit to the repo,

but you can always just roll back the commit, right?

Commits are totally immutable.

So in general, I like adding the git add wildcard

and git commit wildcard into the permissions allow.

Because otherwise I would just have

to manually tell it to commit afterwards.

Okay, let's do some QA here.

I'm gonna log in as James Park.

I'm gonna go to a course

that I haven't purchased already, the Node.js course,

which is run by Marcus Johnson.

And I'm going to enroll now for $60 fake dollars.

So James has now enrolled.

I can now log in as Marcus Johnson.

And hey, would you look at that?

I've got a notification.

James Park enrolled in building REST APIs with Node.js.

And if I click on this, I can go to my student roster.

Now, like usual,

I can see a couple of little paper cuts here.

This bell is not quite visually aligned

with this cadence title up here.

But overall, I'm happy with the results here.

And on the backend, it seems to be working fine.

So we have successfully used our do-work skill.

This is exciting because it's going to be a canvas

that we can then build and layer on

as we increase the complexity of our workflow

and especially increase the complexity

of our feedback loops.

Nice work, and I will see you in the next one.


### 055-AI Coding for Real Engineers p55 055 Fixing Agents Broken Formatting With Pre Commit Day 4 Feedback Loops

This do-work skill that we've been working on, you might notice that we are really encouraging

the AI to use the feedback loops, but we're not enforcing that the feedback loops run on every

single commit. Wouldn't it be great if before every commit we could just deterministically

check if the repo is good, and if it's bad then we report that back to the agent. Well,

guess what? There is such a thing using Git hooks. Git hooks allow you to run a script

when certain events happen within Git. For instance, here we have a pre-commit hook.

This runs automatically before you commit, so we can run something that might fail,

like a type check or tests, and put that inside the pre-commit hook. Now,

experienced developers are probably looking at this going, what? You're recommending pre-commit

hooks? Are you crazy? Because pre-commit hooks are famously really annoying for human developers.

Because human developers might want to push to the repo for all sorts of reasons, but they

don't necessarily want to have to wait three minutes every time they commit for their types

and tests to run. But for an agent and for Claude, this doesn't matter because Claude

doesn't care how long it takes to run the tests. It doesn't get frustrated by things taking

a long time. It's just going to just wait and see what happens. So the friction that's

really painful for a human developer is actually perfect for an agent. And so in this lesson,

we're going to set up a pre-commit hook that is going to deterministically enforce our

feedback loops. So all we're going to do is click on use with AI, copy as markdown,

and then we're going to paste it inside a fresh Claude code instance in the project,

and then just say, implement this in my project. I'm then just going to shift tab. So I accept

edits on and we should be good to go. So it's detected that we've already got typescript.

We've already got V test. It's now asking to install a couple of dependencies, husky

and lint staged. Husky basically helps us manage our pre-commit hooks in a really simple way.

And it's now asking to execute husky init, which is what you want. Lint stage does a

really nice command that only runs linting on staged files. This is going to be really,

really useful in a second. It's then written three lines to lint staged rc here. This is

the configuration file for lint staged. And what this basically says is on every single file

that's staged, we are going to run prettier on it. Now prettier, if you don't know,

is a code formatter that basically means that your entire repo corresponds to a certain set of

formatting rules that you encode locally. If you've never heard of prettier, what are you doing with

your life? It's the most incredible thing and it's been around for years, but combined with

lint stage, we're basically making sure deterministically that the AI cannot commit

unformatted code to the repo. Okay. It's verified. Everything works by doing a quick dry

run and crucially, it's also given us a file inside dot husky forward slash pre-commit,

which basically runs the three things that we've just been talking about. This now runs

npx lint staged. It runs pnpm type check and it runs pnpm run test. This means that every time

we commit, then these three are going to be run. So now I'm going to get it to commit the

code here. And if we zoom down here, it looks like it's already completed its work. It added

all the relevant files it committed. And we can see that the pre-commit hook ran all three

checks, lint stage formatting, type check, and a bunch of tests. And they all passed. I'm

now going to say to it, test that the pre-commit hooks work by trying to push a commit with a

failing test. And I'm going to submit this and check that it works. So it's now gone into the

coupon service and updated that. And we can see that it's now staged the files and tried to

commit, but the commit was blocked. The hook caught the failing test, expected X to have

a length of 99.9, but got five. It's now gone back, updated the thing again, and it's

now in fact going to restore the original test file, which is good. So there we go.

That is exactly what we want. It caught the error and it prevented us from committing.

And it told the AI how to fix it. A beautiful deterministic feedback loop that you should

have in every single project. Nice work. And I will see you in the next one.


### 056-AI Coding for Real Engineers p56 056 What Is Red Green Refactor Day 4 Feedback Loops

We now have our do-work skill and at the moment it's kind of vanilla.

It's not exactly optimized for what I think is the best way to build code.

For instance, we aren't giving it any kind of instruction on how to implement the plan.

However, the debate on how to implement code is almost as old as software development itself.

And there are a ton of great techniques that allow you to not only build out the code,

but do it in a safe way that increases the value of your feedback loops as you go.

We want to push this implementation step to increase our code quality, not diminish it.

And the technique I'm going to teach you about is Red Green Refactor.

Time for me to wave another book at you.

This is Extreme Programming Explained by Kent Beck.

Kent Beck is a prominent advocate for something called test driven development.

And the foundation of TDD is that tests are really important and should drive your entire development process.

This is even more true in the age of AI, where feedback loops are so important.

One of Kent's main techniques is that you have this Red Green Refactor loop while you're implementing.

It's very tempting when you're building stuff to just dive into implementation.

And this is what AI will do every single time you ask it.

But what Red Green Refactor does is it says you should write a failing test first.

And not only should you write the test, but you should run the test to see that it fails.

This is phenomenal when you're bug fixing because you prove the bug exists and then you go to fix the bug in the green phase.

In the green phase, you write a minimal implementation to make CI go green again.

In other words, you just try to pass the test.

And then in the refactor phase, you go and look at that code, refactor it, kind of put it in a prettier state and try to increase your code quality.

All the time running the feedback loops to make sure that you're keeping the CI green.

And by the way, when I say CI, I mean continuous integration.

That's kind of a shorthand that devs use to basically mean types and tests.

So why does writing a failing test first matter so much?

Well, for AI, it's incredible because it gives the AI the ability to run the code and test the code even before it's written the code.

And not only that, but it forces the code that the AI creates to be testable.

And if a piece of code is testable, then it's easy to write tests for and so easy to change later because the tests will catch any bugs with the code.

And having a failing test in place first means that the AI can instrument the code and add logs and understand the code really deeply while it's implementing.

Personally, I have found that using red green refactor in my implementation phases increases the quality of AI's code so much.

I've also found that combining red green refactor with tracer bullets is an extremely good way to go.

With this set up, the agent creates one failing test, then creates a minimal thing to pass that test.

Then it creates another failing test, then creates the minimal implementation needed to pass that test.

In other words, the first test here is a tracer bullet test.

It's just testing one vertical slice of the entire setup.

So getting AI to work through and just create one test at a time, it has been so good because this reduces the likelihood that AI is going to spray a bunch of tests in a horizontal layer into your code base, many of which might not actually be testing a real thing.

Finally, from your perspective as the user, actually seeing the failing test and then seeing the test succeed is a really good way to just feel confident about what the LLM is doing.

Because actually having a failing test and then making it pass is relatively hard for the LLM to fake.

Obviously, if it's feeling malicious, then it can just kind of create a crap test and then make that crap test pass with a crap implementation.

But in my experience, if it's steered well, it just rarely does that.

And as it's going through this cycle, it's adding better and better tests to the repo, which are testing existing code, making the code base easier to change and easier to manipulate.

And I'm really, really excited to show you this as part of this course.

So nice work. I will see you in the next one.


### 057-AI Coding for Real Engineers p57 057 Red Green Refactor Day 4 Feedback Loops

Okay, let's go into our do work skill and change the implementation setup so that it uses red green refactor instead of just working through the plan step by step.

The way I recommend you do this is to go into a fresh Claude code instance here and use the writer skill here to add red green refactor into the implementation steps inside the do work skill.

We should encourage the agent to do one test at a time in a traceable it style, and we should encourage it to do this only for back end code, not for front end code.

The reason I'm adding that stipulation is that our test suite only really works for back end code.

We don't currently have a front end facing test setup.

We'll cover the front end later, don't you worry.

But for now, I'm just going to focus on red green refactor in the back end.

Then once you're happy with this skill and you're ready to test it out, we're going to immediately go and test it out.

We have a PRD here inside coupon redemption notifications for team admins.

When a team admin purchases seats and distributes coupon code to their team members, they have no way of knowing whether those coupons are actually redeemed.

So the solution is to extend the existing in-app notification system to alert all team admins when a coupon belonging to that team is redeemed.

This is a really small feature.

We're just extending what we had before.

And so it should be a good place to test out the TDD approach because there's some back end code that needs changing in here.

So once you finish writing your skill, then you should go in and do the do work setup that we had before, putting in both the PRD and the plan.

The plan itself only has one phase, so you can just say do phase one and you should be good to go.

Watch Claude code like a hawk and you should see it go through the red green refactor loop.

It is just tremendously satisfying to watch.

Good luck and I'll see you in the solution.


### 058-AI Coding for Real Engineers p58 058 Red Green Refactor Solution

Okay, let's start by modifying our do work skill.

The cool thing about TDD and Red Green Refactor

is that models kind of really know what it is.

You don't need to point them to external docs.

And so we can already see it has asked

to modify the setup here.

Okay, cool.

So it's given us quite a lot of text here.

I'm looking at the for front-end code section

immediately, this just looks really long to me.

I think we can say, just cut that down

and say, implement directly without PRD.

I think it knows what front-end code is

so we can just pair it down to that little sentence.

I do like this.

I think it already understands what back-end code is.

I don't need this extra pair of parentheses.

For back-end code, use Red Green Refactor.

I'm looking at this little list here

and I can see that it says,

refactor and then repeat from step one.

I'm actually gonna swap these two things here.

So I'm gonna get it to repeat from stage one

to continually do Red Green, Red Green,

and then do one refactor step at the end.

I'm also gonna return these parentheses.

I don't think these examples

are actually that helpful.

I think more vague guidance is better.

We're just trying to tickle the latent space

of the LLM really just to say,

do Red Green Refactor,

here's a list of things you should do.

But overall, this looks good to me.

I'm going to commit this,

say made changes to the do work skill

before I actually go and implement.

Okay, let's close this up

and I'm now going to run clear

inside my claw code instance

to make sure I've got a clean context for the next bit.

So I'm first gonna pull in the PRD,

then I'm gonna pull in the plan

and then I'm gonna go a couple of spaces down

and I'm going to say do work

and then I'll tell it just down here, do phase one.

And let's see how this goes.

It's nice that it starts off here with two explore agents.

It's exploring the notification system

and exploring the coupon system, very cool.

Before I forget, I'm gonna put it on shift tab

so I accept all that it's on.

And here we go, we've got our first TDD mention here.

Let me create tasks and start implementing with TDD.

Okay, it's continuing implementing

and it's starting to use TDD.

Let me write the first failing test first, yay.

It is, I have to say, writing more than one test here.

So it's actually written multiple tests inside here.

So I suppose it must be quite confident

about the implementation.

It's sort of rushing ahead a little bit.

We can see it's referencing the red phase

and indeed the tests do fail.

So it's now heading towards the green phase

where it's going to actually implement them.

We can see it's adding code to the coupon service

which is expected and now, yeah, all tests pass.

Now it's going to update the front end.

Okay, if we zoom down, we can see that it then,

finally, once it sort of did everything,

it's now validated with the type check and the tests.

So it's running the feedback loops as kind of a final check

before it actually goes and commits.

Then it's adding the code and it's asking me

for permission because it looks like

there's some dodgy stuff in there

or a command substitution.

The feedback loops ran just one more time

inside the pre-commit hook there as well.

And so we are looking good.

So I've logged in as Liam Thompson here

who's just a student.

And I can go into Introduction to TypeScript

and I can buy more seats.

I'm going to be a big spender

and I'm going to buy five seats here.

And I end up in my team management section

where I can distribute these tokens.

So I'm going to copy and paste the first code here

and just copy the link.

Then I go to the bottom left.

I'm going to log out of Liam Thompson.

I'm going to sign up as a new user.

So I'll go with Matthew Pocock as my name

and then I'll put in an example email.

When I sign up here,

then I should be able to go into the URL bar

and paste the link that I got from Liam Thompson

and redeem this course.

I can then click enroll now

and I should be able to start learning from here.

Now, if I go back into Liam Thompson,

then Liam Thompson, yes, has a notification.

Matthew Pocock redeemed a coupon

for Introduction to TypeScript

and there are four of five seats remaining.

And I can see that by clicking on the notification

and heading into here.

So I would say not too shabby.

Now, because this is a relatively simple feature,

we might have gotten the same quality here without TDD.

But what I definitely feel having done this

for a few months now is that TDD and RedGreen refactor

because AI is so patient at creating the tests,

because they create a huge network of feedback loops

that the AI can rely on,

they increase the likelihood

that AI is going to one shot the feature as it just did.

So I freaking love it, I'm a huge fan.

Now, one thing I did notice that does concern me a bit

is that it didn't follow our instruction

to do Tracer Bullet tests.

So what I would do if I was working on this

on a real application is I would go back into my skill

and try to really emphasize the Tracer Bullet approach.

And if you like, you can do that now.

So what did you notice that was different

from my outcomes to your outcomes?

How does your skill differ from the one that I produced?

All good questions that can be asked right now

on the Discord.

Nice work and I will see you in the next one.


### 059-AI Coding for Real Engineers p59 059 What Is An AFK Agent Day 5 AFK Agents

I want you to cast your mind back a little bit to this mental model that we had about multi-phase plans.

The idea of these plans, of course, is to basically break down large chunks of work

so that we can fit them into the smart zone of the agent so that we can get the best outputs.

This means that we need to prompt it with three inputs.

We need to prompt it with the destination, the PRD, the plan, which is the journey,

and then an instruction to do a phase, so do phase one or two or three, etc.

Now, there's a problem with this setup as I see it, which is this do phase n command.

This means that a human needs to sit with the agent telling it which phase to do,

which feels really wasteful.

In other words, this entire flow requires a human in the loop, or HITL as it's known.

And the truth is that that can be automated, do phase n,

instead of, you know, that's a for loop that we're looking at there.

And all of the stuff inside here is already automated.

You may have already felt this when you were monitoring the agent while you were doing the plan.

You might have felt, I don't really need to be here at all, do I?

You know, we've got the destination all mapped out.

We've already mapped out the journey for the LLM.

We can just be at the end and queue anything that comes out.

The do phase n can surely just be done with a for loop.

This is personally what I had been feeling for a while while I've been using Claude Code,

all the way up to December 2025.

But in December 2025, it seemed to be some kind of inflection point

that the models got good enough that you really could just send them off to do these very well defined tasks

and they would do a really good job.

Jeffrey Huntley's article on Ralph Wiggin really put me onto this.

He talks about using a simple for loop here just to run a prompt over and over again to complete tranches of work.

Initially, I adopted the Ralph approach, but I found myself slightly moving away from its original vision.

And so I like to refer to this pattern as AFK agents.

Agents you can run while you're away from the keyboard.

This allows you to delegate huge amounts of work to the agents and allow them to kick out a bunch of code

while you are busy planning future work or queueing some other agents run.

It really has been a game changer for me in terms of the amount of work I can get done.

And in this section, we're going to be taking these multiphase plans that we've been building

and we're going to be running them AFK.

And everything that we've been learning so far from feedback loops to planning to specifications to traceable,

it all leads back to this.

So good luck. I hope you're excited and I'll see you in the next one.


### 060-AI Coding for Real Engineers p60 060 Sandcastle Day 5 AFK Agents

You can think of there as being a kind of learning curve for ramping up to using AFK agents.

The reason you need a learning curve is so that you don't make mistakes with the AFK agent that you can't see.

You need some time interacting with the AFK agent and periodically checking in, seeing how it's doing,

so that you can ship updates to its prompt, so that you can monitor its progress and maybe make big changes to your workflow.

This means that we need two ways of running our AFK agent.

The first one is through this main.ts file, which we'll look at in a bit.

But the first one we're going to see is this interactive.ts file here.

And you'll notice that we're using a really interesting tool here.

This tool is called Sandcastle.

Sandcastle is a tool that I've built for working with agents inside repos, or rather inside sandboxes.

What it lets you do is in theory run any agent inside any sandbox provider.

So we can pass in an agent here, which in this case is claw code,

pass in a sandbox, which in this case is Docker,

and then we pass in either a prompt file or a prompt directly.

This means that throughout this course you can use Docker if you like, or you can use Podman if you prefer.

You can even use Versel as like a remote isolated sandbox provider, or you can figure out your own.

Sandcastle is my solution to what I see as a lack in the ecosystem of a kind of provider or sandbox agnostic setup for running agents.

The way this section is going to work is we're going to start with this interactive function,

which we import from Sandcastle up here.

And we're actually going to use no sandbox whatsoever until we're ready,

because setting up a sandbox is a little bit of a pain.

So what we'll do is we're just going to be using this prompt.md,

which is going to mimic what our later AFK agent is doing.

So by watching the agent carefully understanding how it works, we can optimize our setup around it.

So in the next few exercises, we're going to experiment with this and get it working.

Nice work, and I'll see you in the next one.


### 061-AI Coding for Real Engineers p61 061 Trying HITL Agents Day 5 AFK Agents

Alright, in this exercise we're going to be looking at the interactive.ts script

and we're going to be running it for the first time.

You'll see here that there are some very simple setups here.

We have an agent, we are in this case running Claude code.

You can run Codex if you want to, you can run OpenCode,

you can run a few different agents inside here,

but we'll stick with Claude code because that's the one I've been using throughout this course.

Then we'll say sandbox and for now we're just going to say no sandbox.

Later we can replace this with Docker when we actually do want sandboxing,

but for now this should be okay.

The main one that we're going to be looking at is the prompt.md file which we can open here.

And this should be fairly familiar to you because it's going to look quite a lot like your do work skill,

but with a couple of extra additions.

Sandcastle allows you to do this very clever little syntax here

where we basically have some code blocks inside here with just some backticks

and then before that we can prefix an exclamation mark to run this

and this piece of code will be placed into that position inside the prompt

when it's passed into Sandcastle.

So what we're doing is we're using cat which allows us to read a file's location

and then we have this argument syntax here.

This is another Sandcastle kind of local thing or Sandcastle native thing

where we can pass in an argument of a PRD location.

So this is going to read the PRD for us and put it in the prompt.

We then do the exact same thing with the plan down here

and we have a plan location prompt arg being passed in.

You'll see below here that there's an if there's no more tasks to complete output no more tasks.

I'll leave that a mystery until we look at the AFK version of this script.

We then tell it to explore the repo, very simple.

Tell it to complete the task just like our do work skill

and then run the feedback loops and then commit.

Simple enough.

And finally we say only work on a single task.

Now of course this is an extremely bare version of what a do work skill,

what a prompt for an AFK agent might look like.

You might tell it to do red green refactor inside the implementation.

You might tell it where to explore.

All of this is totally customizable and up to you.

Really the main thing here is that it only works on a single task down here.

If it continually burns through tasks or tries to do the entire multi-phase plan

in a single context window we're going to end up in a dumb zone and that's not good.

So like always we do have a new PRD to run through.

This is the Admin Analytics PRD.

Admins of the Cadence course platform currently have no way to view platform wide revenue

or performance rent tricks.

The existing Analytics dashboard is scoped to individual instructors.

So we are essentially making a read-only admin analytics page for our course platform.

We then have the plan which is going to be working here.

So we have three phases in this plan.

The summary and the route, the revenue over time and the course breakdown table.

And what we're going to do is we're going to use this interactive.ts file here

to initiate just phase one.

So we're just going to work on phase one in this exercise.

So what I'd like you to do is open up a new terminal and you're going to type in

npx.tsx.sancastle. interactive.ts.

npx allows you to run any arbitrary code from npm

and tsx is the library that we're grabbing here to run a TypeScript file for us.

A very handy little piece of code.

And so by running this we're then going to see an interactive little UI pop up

to add the values for the PRD location and the plan location.

I'm going to add in the PRD Admin Analytics here

and then I'm going to add in plans I think it is and the Admin Analytics plan.

Once that's done it's going to kick off the afk agent running without a sandbox

inside our repository.

And it should, if all goes well, execute only the first phase of the plan.

At this point it should be similar enough to your do work skill.

There might be a couple of permissions requests that you need to go through and answer.

But other than that I want you to just note down what happens and note down

what improvements you might make for next time.

And just remember we're only going to do phase one.

We'll save the later phases for later.

So see you in the solution.


### 062-AI Coding for Real Engineers p62 062 Trying HITL Agents Solution

Okay, let's run this and see what happens. We can see first of all that inside the prompt that it's

provided, it has all of the PRD and all of the plan just inlined into it, which is really,

really nice. We can also see that it's got the idea of its only implementing phase one. So only

the admin analytics summary plus the root here. So in theory, we should just get a bare bones

root without a huge amount of UI here. It's already gone about committing a bunch of,

sorry, not committing, but writing a bunch of code, which is a good sign at least. And we can see it's

not really configured with any of the feedback loop stuff we've done before because it's kind

of only now just getting to the tests. Okay, it's now requesting to run the feedback loop.

So we can see that it's still asking to do permissions requests here. This is not running

fully AFK yet. And it looks like it's now committed the code and it's reporting that

phase one is complete. Okay, let's go and see what it built. I've logged myself in as Alex Rivera,

who is the admin. And I should be able to go to his dashboard and then go into analytics here.

And we can see if I go to all time, some very basic summary cards at the top. I think I seeded

this data a little while ago because we have just 12 months showing here instead of 30 days

and seven days, but this is looking pretty good for a tracer bullet. So this is exciting.

If we just take away the permissions requests, we'll be able to have a little loop that we

can run again and again to just churn code, which is great. Let me know if you have any questions

or observations here, or if sandcastle did something you weren't expecting,

or if your agent did something you weren't expecting. But if everything is good,

nice work and I'll see you in the next one.


### 063-AI Coding for Real Engineers p63 063 Sandboxing Day 5 AFK Agents

In the previous exercise we marked this sandbox property of interactive as no sandbox

and you might have noticed that we had some permission requests that we needed to field.

This is not going to be any good for us if we need to run this completely AFK.

Now one thing we could do is to go into our agent and add YOLO mode.

In Claw Code that bypass permissions.

Don't allow it to make any permissions requests

and allow it to do damn near everything it wants to.

In the Claw Code docs they say only do this in isolated containers and VMs only.

But what does that mean? What is an isolated container or a VM?

Well if we let Claw Code do whatever it wants to on our system

then it will sometimes choose really really stupid things to do.

It will sometimes create a script that deletes our entire home directory.

It will sometimes take the code that might be company sensitive information

and exfiltrate it out into the world and send it to some strange API because it got prompt injected.

In other words without direct supervision Clawed may do stupid things

and so we need to restrict it to the smallest possible set of options.

Now Clawed does attempt to solve this itself.

It has a sandbox command here.

But this I found is not a perfect solution.

Clawed can actually break out of the sandbox if it wants to.

Which means it can't be trusted to run it with YOLO mode.

And so for me sandbox is a non-starter.

We simply can't use it if we want to run our script AFK.

So what can we use?

Well this is partly what I built Sandcastle for.

So if we go into main.ts here we can see that we have a run function here.

And the sandbox that we're using is a Docker sandbox.

This sandbox runs inside a Docker container and we can even see the Docker file for it in here.

We install node 22.

We install Clawed code right here.

We add Clawed to the path.

We add a working directory of home agent.

And this is now containerized inside a Docker container.

The cool thing about this is that it can still see our system.

It can still see the repo.

The repo is bind mounted into the container.

But it can only edit files that we choose.

So it can't see the rest of our computer.

It can only work in that directory.

And even any bash commands will run inside the container

focusing only on the stuff that's in that folder.

To get this working you will need to download and install Docker Desktop.

Or you may wish to use Podman which is a free and open source version of Docker Desktop.

Docker Desktop is free but there are some licensing constraints if you're a large organization.

So Podman is the one that's free everywhere.

I'll add links below for Docker Desktop and Podman.

Once you've got it downloaded you'll then need to go into the .sandcastle directory

and head to this .env.example here.

You'll see that we need to add some environment variables into a .env file just here.

And this is going to be piped into the Docker container.

These environment variables are the things that we're going to use

to authenticate the coding agent that we're using.

So in my case I'm going to be using Anthropic API Key.

Now if you want to use your Claude subscription then you should head to this open issue.

At the time of recording this issue is still not quite resolved

because it involves a small amount of legality from the Anthropic side.

A very frustrating situation for me personally.

So I maybe by the time that this is finished recording then, or by the time you see this,

then you might be able to use it and have a nice guide for it.

But let's see how that goes.

For now I recommend just using the Anthropic API Key.

There is also this GitHub token in .env.example but you don't have to worry about that yet.

Once that's done then you can open up the terminal and run pnpm sandcastle docker build-image.

I'll add a link to that below.

What this is going to do is build the docker image for this repo.

You can see that in the docker file here you can basically customize this to your heart's content

but this will work out in the box with Claude code.

And what we now have, now that we have our docker image built, is our sandbox is ready to go.

To finally test that this is working we're going to run this test.ts file which I've got here.

Which will just run an AFK agent with a prompt, hello, how are you?

This means that we can run npx tsex.sandcastletest.ts

and when we run this we can see a couple of logs show up.

So we have an agent log coming up here.

And if you command click or control click this link we can see some live logs as to what's happening here.

We can see the agent started and replied with, hello, I'm doing well, thanks for asking, how can I help you today?

We can even see that setting up the sandbox took this amount of time

and it tried to collect any commits that happened inside the sandbox but none were made.

And we even used 19k of context window, very cool.

So if you saw those logs, if you saw something similar to mine, the UI might have slightly changed

but if you saw a successful run, nice work and I'll see you in the next one.


### 064-AI Coding for Real Engineers p64 064 Setting Up And Trying AFK Agents Day 5 AFK Agents

All right now we're all sandboxed ready to go it's time to work on the afk script. This by

convention is in sandcastle main.ts here and we're doing something slightly different here.

Instead of asking for the prd location like interactively we are now passing it into prd

location and plan so we'll need to initiate the or call the script in a slightly different

way. We're going to do this by running this in our terminal. We're going to use npx tsx.

We are going to if I get my face out of the way run sandcastle main.ts so this main file here.

We're going to pass the prd admin analytics in the first positional argument and the plans in the

second positional argument so prd will end up being prd admin analytics.md and the plan variable

will end up being admin analytics plan.md very nice. Now just like the test.ts script that we ran

we're using Claude code and we're sandboxing it in docker and we're taking the prompt file

that we used which is exactly the same as the one in the interactive command we ran. In fact the

main things are different come down to three parts here. We're using run instead of interactive.

We're using max iterations and completion signal. Now max iterations what this will do is it will

run this in a loop for a maximum number of times. So we'll essentially just like we did a

single loop with our interactive function we are now running this prompt again and again and

until one of two things happen either we hit max iterations of three so it's run it three times

or we receive a completion signal of no more tasks and if we head into the prompt.md here

we can see that if it says if there are no more tasks to complete output promise no more

tasks so that means that if it sees this in the output it's going to stop or if it hits

the max number of iterations it's going to stop the loop as well. When I'm running this myself

I often have a lot of faith in the completion signal here so I'll often set max iterations to

something crazy like 10, 15, sometimes even 50 but for us let's just keep it nice and slim

to make sure we don't burn too many tokens and of course feel free to customize the agent and

the model that you're using here so this just gets passed straight into Claude code so whatever

model you prefer to use is up to you. At the time of filming 4.7 is the latest but I still

prefer 4.6 but I don't know sometimes I'm sometime I'm gonna have to migrate. As with

all of the exercises make sure you note down everything you see and if you have any questions

head to the discord so good luck and I'll see you in the solution.


### 065-AI Coding for Real Engineers p65 065 Setting Up And Trying AFK Agents Solution

Okay, let's run this and let's see what happens.

We should be getting our agent immediately.

We can control click to view the logs

and now we can see, okay, the agent has started.

Beautiful.

We can see that it sees that phase one is already done

and it's now going to work on phase two.

So it's now doing agent explore repo for phase two.

Really cool that we can see all of the tool calls here

and everything has just surfaced to us through the logs.

Crucially, we can also see the iteration number

that we're on here.

So iteration one out of three here.

Nice.

So I'm going to do something a little bit strange

which is I'm just going to step away for a minute

and let this cook.

I recommend you do the same.

Go get yourself a cup of tea and I'll see you in a second

to see what it actually did.

Okay, we have come back and we've come back

to what appears to be working code.

We now have a revenue over time chart.

I'm logged in as Alex Rivera

and we have a per course breakdown at the bottom.

We can see that we can filter by instructors.

So we can filter by Marcus Johnson

or filter by Sarah Chen

and all of this looks good.

The chart is sort of moving in slightly a funny way

but we could pick that up in QA probably.

This is looking pretty good, I think.

Let's now dive back through the logs

to see what happened here.

We can see that initially here it says

that phase one is already done.

That looks good.

Now this is working on phase two revenue over time chart.

So phase one, that was what we did

in the interactive exercise.

So this is the first piece of code here.

So it kicks off an agent explore.

It runs type checks.

It runs tests.

It's doing some syntax error stuff

and it's got, okay, running some more type checks.

All the tests are passing

and then it creates a commit here.

So it's saying git add this file

and then saying git commit two.

So it's adding a rechart, line chart

to the admin analytics dashboard.

Beautiful stuff.

So then if we zoom down all the way here

we can see we get to iteration two out of three.

So now it's starting the second iteration

because it didn't see the completion signal

in the previous one.

So it sets up the sandbox again.

It does phase one and phase two are already done

and now it's exploring the code base

and it's going to create the course breakdown table

with instructor filter.

Beautiful stuff.

So all the tests pass.

It's doing all the stuff it needs to.

It's created the commit.

And then we can see if we zoom all the way down

to the bottom, here we go.

We've got okay.

And we end up with no more tasks being emitted.

Beautiful.

We can see it's grabbed all of the commits.

We can see that it said that it signaled completion

after two iterations.

And then we get a printout of the context windows used.

I feel like these could go somewhere else in Soundcastle

but I'll list that as a bug report.

So we can see the first context window was 64K.

Second one was 80K, not bad.

So I was fully able to go and get myself a cup of tea

and come back and to working code.

Very, very cool.

We can see lots more tests were written.

We can see that all of our instincts about planning

are paying off here because we just get to align the agent

and then point it in a direction

and then we're good to go.

And we get working code at the end of it.

Now at this point, I've been doing this for months

and I fully see this as the future of development.

You're able to parallelize yourself with the agent.

And so having these two streams running at the same

time, you doing something else,

planning future work, let's say,

and the agent working on something,

it has been pretty cool.

So nice work.

We have glimped the future.

I will see you in the next one.


### 066-AI Coding for Real Engineers p66 066 Using Backlogs To Queue Tasks For AFK Agents Day 5 AFK Agents

I have a pretty big issue with the way that our AFK agent is currently set up.

An issue I have is that we are deliberately pointing it to a plan and a PRD.

Now we want to run this agent totally AFK, but we are still needed to specify the PRD and the plan.

Wouldn't it be great if we just had a queue that the agent could pull from as to what it should work on next?

If it had a queue at the end of the PRD and the plan, it wouldn't just kind of like fade out and go away.

It would go, okay, what's the next most important task to work on? Let me pick that.

In other words, we're going to get our AFK agent not only to do the task, but also pick which task it should do next.

Now, which task it chooses is going to be something that we'll need to prompt very, very carefully.

If we pass it a big list of tasks here, then it's going to need to decide which ones are more important.

And depending on what stage of project that you're at,

the way this task prioritization works is going to be very different.

So I've provided a prompt, but this is something you will want to look out for your project very, very carefully.

In the commit in this exercise, I have changed the prompt from instead of passing in a plan and a PRD to instead using this.

So now it's going to fetch a set of open GitHub issues.

In other words, we're going to be using GitHub as our issue tracker.

But of course, you could use anything that you want here.

Anything is open.

The next thing that's very important is we have a task selection prompt.

So it's picking the next task and it's going to prioritize tasks in this order.

The first one is going to be critical bug fixes.

Of course, those things have to come first because if everything else in your system

is like churning commits onto a broken CI or a broken app, that's not going to be good.

The next one is development infrastructure.

So getting tests and types and dev scripts ready.

And that's really important, of course, as we know, because feedback loops are so important for building features.

From then we go on to Tracer bullets.

In other words, Tracer bullets for building new features.

Then number four, we have polish and quick wins.

Then at the bottom we have refactors.

This is the task selection setup that I use for most tasks and it seems to work pretty well.

This means our agent is choosing between big tranches of tasks at once and choosing which one to work on next.

This ends up working pretty well up to around 20 to 30 tasks.

There's lots of different ways that you can winnow down the set that's actually open to the agent.

For instance, we can use GitHub labels.

That's something I've played with in the past.

We can use assignation labels so you can assign it to yourself, let's say, when it's ready to be worked on.

But all we would in theory need to do is just run main.ts, pointing it at this, and we're kind of good to go.

This means then that we end up in this virtuous loop where the agent produces code,

which is then reviewed by a human, which then goes through to GitHub or creates new issues or reviews the code,

which then goes through to the agent producing more code.

It is a wonderful, wonderful circle and it's very, very productive.

I've been using this setup to build Sandcastle itself.

So we can see that inside the closed issues, there are currently 403 of them.

And I also have a label in here called ready for agent for any task that's ready for an agent to pick up.

And so this setup where you point your agent at your issue tracker is what we're aiming for in the next few exercises.

Nice work and I will see you in the next one.


### 067-AI Coding for Real Engineers p67 067 Setting Up Our Repo For GitHub Issues Day 5 AFK Agents

Okay, let's hook up our issue tracker to our AFK agent.

In order to do this and in order to use GitHub as our setup,

we're gonna have to walk through a series of annoying steps.

If you were to simply fork the project repo,

then you would end up any issues you create

would go into a common pool, so it would go into my repo.

This would mean that every single student on the course

would be pushing to a single issue repository

and we'd all be pulling from the same one,

which would be total carnage.

So I'm gonna give you a series of bash commands

that you can run to essentially set up

a brand new repository on GitHub,

pointing to the cohort repo.

Below, you'll find a series of instructions to follow

so that you can go through this

and walk through each individual step.

The process is gonna kind of look like this.

The current setup is you have a local cohort 004 project

pointing to my GitHub repo,

the cohort 004 project repo.

The first step is we're gonna copy this over

into a new directory here

with cohort 004 project fork being the directory name.

We're then gonna delete all of the Git history

and then we're gonna create a new GitHub repo

with its own issue tracker owned by you,

which is the cohort 004 project fork.

So follow the instructions below,

make sure that at the end you have your own repo

that you can post your own issues to

that no one else can interact with

and we should be good to go.

And of course, if you hit any issues,

then come to the Discord.

Nice work and I will see you in the next one.


### 068-AI Coding for Real Engineers p68 068 Hooking Up Agents To Your Backlog Day 5 AFK Agents

Now that our repo is ready to receive GitHub issues, let's actually hook things up.

As you saw before, we are doing this via the GitHub CLI.

This is a really, really elegant way that LLMs can talk to GitHub.

They seem to know the GitHub CLI extremely well and rarely get it wrong.

And so it's very, very cool to watch them use it.

We're calling them inside this Sandcastle prompt expansion setup here.

So we have this exclamation mark which runs the code in this back ticks.

And it grabs all of the issues that are open, crucially, and returns them as JSON

with the number of the issue, the title, the body of the issue,

and any comments that have been added to.

That's going to be crucial in a minute.

We then run through our task selection prompt, which we looked at before.

And finally, just after the commit, we go down to the issue again here.

This says that if the task is complete, then you can close the original GitHub issue.

But if the task is not complete, then leave a comment on it with what was done.

This is really useful because the GitHub issue comments then become a running record

of everything that was done on that GitHub issue.

So if you want to put a multi-phase plan in a GitHub issue, you absolutely can.

And it will just comment each time.

And each of those comments will then be pulled back into the context of our AFK

agent by pulling in the comments here.

Our first step, though, is to go into .env.

And we are going to need to provide a GitHub personal access token.

This personal access token will allow the agent inside the sandbox to call the

GitHub CLI and go and ping things off to our GitHub repo.

We can also see that inside the Docker file, for instance, we have the GitHub CLI

already installed here.

So that's useful setup already.

But all we need to do is just find this personal access token and pass it into

the environment variable so that Sandcastle can use it.

I've given you some instructions down below on how you can acquire this personal

access token and the file that you need to save it under.

Once you've got this set up, then, of course, you will have this repo like this,

a cohort 004 project fork, where I'm going to add an issue.

This issue is a teeny tiny one, which pretty much everyone who's taken this

cohort has been annoyed about.

And it is that when you go to switch a user in the dev server here, then

you'll notice that if you choose a user such as Sarah Chen, this thing

doesn't close.

It just doesn't blooming close.

And so we are going to fix this finally.

And we are going to just add a little issue and run the AFK agent to fix

that bug.

I would like you to go into your fork, go into issues and then go new issue up

here.

And then we are going to add some text here.

Here is how I've chosen to write this issue.

User selector in the dev UI panel does not close after selecting a user.

It's blooming annoying.

Fix it.

I am going to create this issue in my fork repo.

Then inside the repo itself, I'm going to run PNPM Sandcastle Docker build

image.

Since we are working in a new repository, it will just need to build the image

again under this new name, but it shouldn't take very long.

Before this was Sandcastle cohort 004 project, but now it needs a new image for

cohort 004 project fork.

And after that, we can run npxtsx.sandcastle forward slash main.ts to

run our AFK agent.

When we run this, it should pick up the bug in our issue tracker.

It should fix the bug and then it should close the issue.

Very, very cool.

So good luck and I will see you in the next one.


### 069-AI Coding for Real Engineers p69 069 Hooking Up Agents To Your Backlog Solution

Okay, let's run our main.ts to see what happens. We of course get our agent up here. So let's watch

it and see how it's doing. So we can see crucially the GitHub issue list state open, Jason. It

returned just 37 tokens, which was our tiny little description there. And we can see it's

kicked off exploring the repo structure and understanding the code base before trying to

fix the issue. One question that people often have with this exercise is why would you take

your GitHub token and give it to an agent, right? And one thing you've got to understand here is

that you can offer really sharp tokens that only allow it to do certain things. For instance, here

we just really want it to read issues, to comment on issues, and to close issues. We don't really

even want it to be able to create its own issues. And so GitHub allows you to create a

really fine grained access token that only allows your agent to do certain things. So that's

how I would implement it. If we zoom down to the bottom, we can see that it's now found the correct

dev UI component looking at the exact code and it's looking at the API route. Okay, it seems to

be on the right track here. And it's also identified the bug when a user is selected,

the form submits via react route as client-side navigation, the open state says true,

and the dropdown never closes. We can even see that there is some code being changed. Oh,

it's actually already committed. Look at that. So there's a commit that's just being created

here and it's running GitHub issue close with a comment. So the commit has succeeded with all

pre-commit hooks passing. Beautiful. It has appended no more tasks here. And we use the

30K context window for the privilege. Lovely. If we go to our GitHub issues, we can see there's

zero open and one closed. We look at one closed and it is the one that we got here.

So it just added this piece of text to the end saying that, okay, it closes immediately when

a user was selected. Very cool. We get an element of observability here. We understand why the

issue was closed because the agent has told us. Okay. Now the moment of truth, we go to the dev

UI panel, we switch the user, we choose Alex Rivera and it closes. Incredible. Look at that,

the power of AI. And so there we go. We have hooked up our agent to our issue tracker,

and it's just able to churn through backlog items. If you want to extend this exercise

a bit, then you can go into all of the application, QA a bunch of stuff, find a bunch of issues,

report them as issues and just run the AFK agent again and see how it does. But overall,

we've proven that the concept works. Nice work. And I will see you in the next one.


### 070-AI Coding for Real Engineers p70 070 Updating Our PRD And Plan Skill To Use GitHub Day 5 AFK Agents

So we've seen now how you can take bug reports

and put them in an issue tracker.

But how does this work with new features?

How does this work with PRDs and issues?

Well, the way I tend to work with PRDs and GitHub

is I will put the PRD into GitHub

and put all of the, or put the plan into GitHub as well.

So instead of just having it as local files

as we've been doing so far,

I've updated the skills to put them into GitHub.

Nothing much has changed here

instead of just creating it as a local file

all we're doing is just creating a GitHub issue

containing the plan.

And it's using the exact same template.

So this means that our AFK agent

will look at the entire backlog,

look at new features, look at bug fixes,

and then use its task selection prompt

to figure out what it needs to do.

So whether that's critical bug fixes,

development infrastructure,

traceable it's for new features come down here.

And this means that we can be using

the PRD to plan skill and using our local setup

to create GitHub issues,

which are then being picked up

by another local running thing

but that's just looking at that backlog.

It means we get to do our entire planning loop

without actually touching the code base that much,

without creating any local files,

which can mess up an AFK agent

that's working in the code base.

I found that this loop is extremely cool

because it allows you to parallelize planning

with implementation.

So there we go, just a small commit

that just modifies our existing skills

to use the new backlog.

Nice work and I will see you in the next one.

Nothing much has changed here.

All we have is now we have a.


### 071-AI Coding for Real Engineers p71 071 HITL And AFK Tasks Day 6 Human In The Loop Patterns

Now that we've fairly successfully set up an autonomous agent to do our work for us,

you might be thinking, can it do all of my work?

Surely it can't do all of my work, right?

There are probably some things that I need to do human in the loop.

Now I would say your instinct is absolutely correct.

And I would say that when you're planning out work to complete a feature,

you should be thinking carefully about which bits are human in the loop.

In other words, you need to be there and which bits can be done autonomously.

Now obviously the dream is that we're just able to delegate all of our work AFK,

and we don't need to be there for any of it.

But the truth is that lots of work needs to be done human in the loop.

We already know one of the things that needs to be done human in the loop, which is planning.

An AI can assist with creating a plan, but without the human,

it doesn't have the source of truth to actually bounce off for what it's supposed to be creating.

Another one we've seen so far in the course is QA.

You need a human eventually to actually go in and test the thing that's being built.

They'll be able to surface things which aren't present in the AI's feedback loops.

Does it feel good to use? Is it fast enough?

Does it actually serve the purpose that I built this thing for?

You might be getting a sense for the things that you need to use humans in the loop for.

Anywhere that you need to apply taste to what you're doing.

Now what do I mean by taste?

What I mean is human judgment, human feel.

We need taste in planning because we need to work out together what we're building,

and I need to make design choices that I feel are sensible.

We need QA because I need to look at the artefact that's created and give feedback on it based on my own tastes.

And I feel that to create great products we need to let humans and AI do the things that they're best at.

The human should be there to give their taste, to give their opinion,

to give the feel to the application.

Not only to how it performs externally to users, but how it's built internally to its architecture.

And the AI should be there to pick up the grunt work,

to apply the human's taste to the canvas of the application code.

So throughout this section we're going to be looking at ways that we can bring the human back in the loop in a productive way.

Because if you delegate 100% to the AI you're going to end up with a tasteless application.

And often just something that plain doesn't work.

So let's get into it. I'll see you in the next one.


### 072-AI Coding for Real Engineers p72 072 Dont Plan Kanban Day 6 Human In The Loop Patterns

I've always had a little bit of discomfort when it comes to multi-phase plans with AI.

And this discomfort comes from the fact that human developers don't work like that.

When we understand the destination, we don't just plan everything out rigorously in a

single document to create a journey.

Instead, we create a Kanban board of different issues.

Some issues might be blocked by others.

In other words, this issue needs to be completed before either of these issues

can be completed.

And for this issue at the bottom to be completed, then this issue, this issue,

and this issue all need to be completed.

In other words, you have a kind of dependency graph of different issues and their interrelationships.

This means that two developers at the same time can grab both of these issues at the

top independently.

Then once those are done, maybe they both grab these issues independently.

And then one developer works on that one at the end.

What I'm talking about here is basically a Kanban board, where once you figure

out the destination, you then take all of the tickets, put them on a board, and

then developers grab them independently.

This is much less prescriptive than a multi-phase plan, and it's also much easier to

add new things onto.

For instance, if I want to grab another issue and just stick it inside here, then I can

very easily and just describe another blocking relationship.

I haven't needed to change any other part of the plan, I've just added something else

onto that.

In my experience, this is much easier than editing multi-phase plans.

It's also really, really easy to QA because you just say, okay, this issue is now done,

I'll just go and QA it and add all the QA feedback as a separate issue.

So the graph grows naturally instead of you having to squeeze it into a multi-phase

plan and figure out where to schedule it.

In the repo, I have gotten rid of the PRD to plan skill and I've added my own PRD

to issues skill.

This breaks a PRD, which is probably already in GitHub, into independently grabbable GitHub

issues using vertical slices, tracer bullets.

So the first thing is it locates the PRD wherever it is, then it might need to

explore the code base depending on what's in its context, or you might already have

explored it.

Then it drafts vertical slices, so it breaks the PRD into tracer bullets, and

these slices might be human in the loop or AFK.

It says human in the loop slices require human interaction such as an architectural

decision or a design review.

AFK slices can be implemented and merged without human interaction and prefer AFK over

human in the loop where possible.

Finally, and I found this is super nice, it says always create a final QA issue with

a detailed manual QA plan for all items that require human verification.

This absolutely rocks because it means I can step away for a long time and then

when I come back, I've got an issue in GitHub with a detailed QA plan with

everything that's been done and the stuff I need to verify.

It then quizzes the user.

It says, OK, we've got the numbered list here, present the proposed breakdown

and ask it does the granularity feel right, the dependency relationships correct,

should you split them or can we, are the correct slices marked as human in

the loop or AFK?

And finally, it creates the GitHub issues using this fairly simple template

here. The main thing is it references the parent PRD in the issue number and

it has a blocked by section below saying it's blocked by this issue number.

We're still going to be passing all of the issues into Ralph, so it should be

able to see all of the blocked by relationships just by looking at the

text inside the Ralph prompt.

I've also made a small adjustment, which is I've said you will work on the

AFK issues, only not the human in the loop ones.

And if all AFK tasks are complete output, no more tasks.

This should prevent Ralph from doing the human in the loop tasks.

But you may want to enforce this deterministically by hiding them with

labels or something like that. For now, this has worked fine for me.

So by using the Kanban approach instead of the plan approach, we get to

independently pick out issues from the AI.

In other words, we're parallelizing our work with the AI's work.

We get to extend the Kanban board infinitely by adding more QA issues.

And we should also get a really nice QA plan at the end.

In the next exercise, we're actually going to use this new setup and see

how it does. Nice work.

And I will see you in the next one.

Hello, Edit Matt here.

I wanted to flag a tiny bit of confusion that you may have noticed if

you've been using my skills and you have come to learn in this cohort or vice

versa, which is that in the cohort, this skill is called PRD to issues.

But in my repo, it's only called to issues.

This is really a teeny tiny change.

It is really just changing the skill from always requiring a PRD to being

able to take anything in and turn it into issues.

In my skills repo, it says work from whatever is already in the

conversation context.

If the user passes an issue reference as an argument, fetch it from the

issue tracker, read its full body and comments.

This just basically covers the idea that they can pass a PRD or they can

just pass anything and it will be turned into vertical slices.

It's such a tiny change that I didn't want to re-record the whole video, but

hopefully that's clear that in the cohort, it's PRD to issues and in the

skills repo, it's to issues.

So nice work. Edit Matt out.


### 073-AI Coding for Real Engineers p73 073 Using The Kanban Skill Day 6 Human In The Loop Patterns

Okay, now you've had a taste of what the Kanban skill actually looks like.

Let's go and use it.

I have a new PRD up here, which I will provide in a GitHub gist below.

The idea of this PRD is gamification.

We need XP, we need levels, we need streaks.

What course platform is complete without these useless doodads?

So we've got a whole bunch of user stories.

I want to see earn XP when I complete a lesson so that I feel rewarded for my effort.

Your job is to copy and paste what we get from the gist

and paste it into a new issue, like I've done here.

You're then going to note down the issue number of the PRD.

In my case, it's 57. I'll copy that.

Then I'm going to head into Claude here and I'm going to say PRD to issues.

I'm going to pass in number 57.

And I just press return very eagerly there,

but I will pause that until we get to the solution.

This is your first chance of seeing how it actually works with the Kanban board.

So write down whatever you notice about the approach and whether you like it or not.

Actually, creating the issues shouldn't take that long.

I would like you to run a Ralph loop on the resulting issues afterwards.

It should only pick up the AFK tasks.

And once that's done, you should be left with a bunch of Human the Loop QA to review.

So best of luck and I will see you in the solution.


### 074-AI Coding for Real Engineers p74 074 Using The Kanban Skill Solution

Alrighty, let's rock and roll. It's asking to review the GitHub issue, which of course I don't

mind, and it's heading off exploring the repo. Okay, pretty swiftly it has returned with the

potential list of issues. Whenever I'm checking these, I always check the first one just to make

sure it's like a proper tracer bullet and not some horizontal splurge. This one looks really

good because it's got XP on lesson completion plus sidebar level display. So it's doing the

XP events table and migration, doing the test for the XP service and showing the UI,

which is great. That's exactly what we want. Then it goes on to do streak tracking. That's good,

like it's like an extension of the tracer bullet originally. Then quiz XP, again, another extension.

Four and five look like really small pieces, so I'm tempted to merge those together. And then

number six, we've got the full gamification verification, so a proper QA plan. So okay,

I'm going to go down and I'm going to say merge four and five together. They look too small

on their own. Then I'll submit this and it should just plunk those two together. It's now

saying, shall I go ahead and create these as GitHub issues? Yes, they look good. I'm not going

to read through these manually because they're kind of just derived from our conversation.

Anyway, we can just sort of see them all on the issues template once they're done. And

in fact, it's asking me for permission for each individual one. So I'm actually going to go

up into settings.json, which doesn't appear to exist. I think it's just settings.local.json.

And I'm going to add bash and this is going to be GitHub issue create or gh issue create

this. I'm just going to allow it. So that should hopefully speed things up a little bit.

Now, of course, I'm using GitHub here, but you could definitely feel free to use any kind of

task tracker that has a CLI or has an MCP server. Alrighty, it has created all five issues.

And if we head to the UI here, we can see that they're all here. We've got the PRD of

57 and 58, 59, 60, 61, 62. Let's just take a look at one of them just for an example. Yeah,

this is the one we grouped together, which is the dashboard summary card and the module

completion toast. It really is pretty thin. It's just a couple of lines here on what we need

to build as part of this plan. And it says go and see the original PRD for full details

and a bunch of acceptance criteria. Good. Now let's go and take a look at the QA one,

which is the last one here. Nice. It's basically got a big list of checkboxes for

us to check all of the work that was completed. I really like adding the QA plan in actually

and showing it to the LLM too, because it just shows it what the user is going to do at the

end provides another source of like, you must do this. You must follow these criteria.

Okay. So we're all set up. I think we're ready to run the AFK loop. I'm going to run

it 10 max iterations. I've actually gone recently to running it one 100 as my default,

which I know is slightly mad, but honestly, I've just haven't had any issues with it yet.

So I'm actually going to go full AFK for this one. I will be back once it's done its iterations,

unless I hit any weird issues on the way, which hopefully I should not.

Okay. I've come back some time later and I now have only two open issues,

which is the original PRD here and the human in the loop QA task. We can see that it did

complete after four iterations and we're up to nearly 400 tests and it completed each issue

in order. So I'm now going to walk through this QA plan and just see if everything works.

I'm going to first log in as a student here. I'm going to go to the dashboard.

Well, that's an early fix. I think it hasn't run the migration. So I'll just run those locally.

I'm going to run PNPM DB migrate. And now I should just be able to refresh the page.

And yes, here we go. Okay. We can see lots of UI has been added here.

At this point during the QA process, what I would do is I would start looking at things

that I don't like. For instance, I don't like the fact that these stars and flames

and et cetera seem to be displaying in light mode. I want them to look like the ones on the

sidebar over to the left here. And I don't like that there's weird kind of padding at the top of

this board here. So I would start putting these into GitHub issues, but let's go ahead with QA.

I'm going to go into this course here. I'm going to go continue learning and I'm going

to complete a lesson by pressing up next and I should get 10 XP. Yes, I do. Very cool.

So I'm going to check this off here. That looks nice. Then complete the same lesson again,

verify no duplicate XP. So I'll go back to pagination and filtering. I can then press

up next again and I don't get duplicate XP. Now I've got to go and find a quiz to pass for

the first time and verify that five XP is awarded. So to do that, I had to log in as

James Park here and I found one on the API fundamentals HTTP methods quiz. See if I can

get this one right. Okay. Which HTTP method blah, blah, blah. A 404 status code. You know

that's wrong. Which stays coding decades successful resource creation. I think that's correct.

Submit and I get five XP. Beautiful. Now there's nothing duller in the world than watching

someone just follow a QA script. So I recommend you do as much as you feel comfortable doing

that you feel that you've got the picture and then finish up to save your sanity because

this is a toy project after all. Now the important thing about this Kanban skill and

the thing that I really like about this process is that AFK and human loop tasks are first

class. We can plan huge tranches of work while not quite knowing how all of our taste is going

to be applied yet. You can even modify this skill to break the QA stages up into sections.

So you're only QAing certain bits instead of large chunks. And of course you can delegate

this to different members of your team. If you have a testing specialist, I think that the

AFK versus human in the loop designation allows you to build in humans into your dev loop

in a really intuitive way. And I hope that this exercise has taught you the same too. Nice

work and I'll see you in the next one.


### 075-AI Coding for Real Engineers p75 075 Research Day 6 Human In The Loop Patterns

There's a certain type of work that you need to do with agents that sometimes can result in really expensive explore phases.

For instance, you might need to integrate with an external service that you don't have the documentation for locally,

or maybe a service where the documentation doesn't exist or isn't public.

And in those phases, because the explore phase is so expensive, then you might need to think about caching it.

Now, what do I mean by this?

Well, I've shown you this diagram a bunch of different times in different ways.

It's kind of like a context window with an explore phase, with an implementation phase and with a testing phase.

Now, if we imagine that this is a kind of Ralph loop where it's split out over multiple context windows,

the longer and more expensive this explore phase is, the more you benefit from reducing it.

In other words, this might be long because it needs to go to an external documentation site and fetch all the docs.

And maybe it can't quite find the thing it's looking for, and so it needs to just continually search.

And over multiple runs, let's say we run this 10 times over a massive Ralph loop,

then this is just going to get really, really expensive.

And so wouldn't it be great if we could reduce the size of these somewhat?

Because if we reduce the size of these explore phases down,

then we're going to end up with a more efficient loop, less token spend.

And it's just going to be faster and better overall because we're going to spend more time in the smart zone.

One of the best ways to do that is to start off before you actually go into a Ralph loop with a research phase.

In other words, you look at everything you need to do for the PRD,

you take all of the external documentation and you cache it into an asset locally.

In other words, this is a research.md file.

It might be research about a specific external library or service that you need to integrate with.

It might be research into a specific approach you want to take, like, I don't know, SSE versus WebSockets or something.

Either way, you do a bit of upfront work and then all of the Ralph loops afterwards get to benefit from that.

Now, I consider this research to be a human in the loop task,

because especially if you're, let's say, trying to choose an external library to do a piece of work,

then your taste is going to be really, really important to influence the direction of the LLM's research.

If the external service has multiple ways of doing the same thing,

for instance, maybe it has some streams and maybe it has some webhooks,

then your taste is going to be really important for guiding which one goes into the research.md.

Now, this approach won't be necessary for all tasks because not all tasks need a long complicated explore phase.

However, I would say that as your code base grows and maybe gets harder to find the right things to actually pull into the context,

then a research phase at that point would be really, really handy, too.

A crucial part of this is that this research should have a life cycle that's really closely monitored.

We don't want this to stick around in the repo forever because we might end up choosing a different implementation or refactoring away to a different service.

Or if this research is about our own code, then our code might change.

So it's really important to audit these research files in the same way that you audit your steering files,

the same way that you audit your Claw.nd or your skills,

because a bunch of stale markdown files in your repo are going to really hurt your LLM's performance.

So that's what research is.

It's a way of caching explore phases to make sure that you don't do expensive explore phases at the start of a bunch of Ralph loops.

You've got to very carefully manage the files that it creates.

But if you do, then you're going to get really, really nice results.

Nice work and I will see you in the next one.


### 076-AI Coding for Real Engineers p76 076 Trying Out Research Day 6 Human In The Loop Patterns

So now we know what research is, let's actually try out doing some research.

In the application I want to build a live presence indicator on lessons,

where you can basically see all of the little icons of people who are also taking the course at the same time.

To make this work, we'll probably need to figure out the external service, right,

or figure out how we handle this in the back end.

There are many, many, many different approaches we could take.

We could take a simple polling approach or do web sockets or use an external service,

because we need to know when someone quits out of the lesson so that we can remove them from the UI

or when someone comes in so we can add them back.

So what I'm going to ask you to do is go into Claude Code inside the project,

and you're going to say something like this.

I want to research several different approaches to create a live presence indicator.

This live presence indicator is going to show up for students who are intrigued

who else is looking at the lesson at the same time.

I want you to iterate with me towards a solid approach

and ask me some good questions about where we should go.

And then I want you to look on the web to back things up and kind of validate our assumptions.

At the end, I want you to create a research document inside the plans directory.

This document should be focused on the implementation

and focused on providing research on the approach and how we intend to use it.

So I don't have a skill prepared for this one.

I don't tend to use a skill.

I prefer to just rely on Claude Code and to get it done.

The important thing in this prompt is that I'm asking it for several different approaches

so that we can compare them.

And I'm then going to use my human judgment to figure out the right one

and then create a markdown document about it.

All we're going to do in this lesson is just create the markdown documents.

We're not actually going to go and implement it,

although you're very welcome to turn that into a PRD,

turn that into a Kanban board and then go.

But since we've already done that, I don't want to be too repetitive.

As you do this, really work with the agent, ask it questions.

We are just kind of co-researching together.

Write down anything you notice and any questions, ping the Discord.

Nice work and I will see you in the solution.


### 077-AI Coding for Real Engineers p77 077 Trying Out Research Solution

All right, let's give this a go and see how it does.

We have our traditional explore phase as it goes and explores the project tech stack.

Okay, it's done its exploration.

It's now found that we have a React router V7.

We have a full stack SSR.

And crucially, we have no existing real-time infrastructure.

Now, here is where we get to apply our taste.

You notice these questions like scale expectations and fidelity versus simplicity.

What should the UI show?

We're really in kind of writing PRD territory and kind of, you know,

it grilling me about my expectations.

In terms of scale expectations, I'm imagining something like 20 students

viewing the same lesson is probably realistic.

I'm going to say that I do want true real-time.

The UI should show Matt, Sarah and two others are here.

As you say, the cursor scroll position is overkill.

I'm definitely open to adding a third party service

and I would probably prefer that to self-hosting it.

Presence data doesn't need to persist.

It can be ephemeral.

We don't need to worry about unauthenticated users

counting towards presence.

Okay, let's ping this off and see what it does now.

So for the first time during this course,

it has gone and launched some background agents.

Those agents are researching party kit, pusher, ably and liveblocks

and it's going to share its initial thinking on the trade-offs of those.

I know about some of these, but I've never actually used any of them.

In fact, while I've been waiting, it looks like the agents have completed.

So super base real-time and liveblocks don't look right.

Then we've got pusher and ably and party kit.

So it looks like it thinks ably is the best.

It also has a super generous free tier,

which is what I suppose I care about most in this really a toy application.

I'm just going to answer its last few questions here.

I agree that ably looks really nice.

I think I would prefer a managed API key service.

I'm comfortable with that API.pusherauth.ts idea

and this is probably the most important one.

Let's make ably the recommended approach for the research document.

So with that, I feel comfortable running it and we can get it to work.

This is nice.

It's now kicking off the agent again to research ably again.

This is a really nice in-depth exploration

that we're able to do without using skills actually.

Okay, it's come back from its final explore phase

and it's written a markdown file for us.

This is that live presence indicator in the plans.

And let's just take a quick look at the length here.

What are we talking?

We're talking a decent hefty, you know, nearly 200, 300 line file.

Let's take just a quick look at the top

and see what the top level items are.

We've got some requirements here.

We've got the recommended approach, the implementation design,

integration points in the existing code base.

That's really nice.

The alternatives considered, we might not need,

but then it might be useful as a kind of architectural decision record.

And I suppose it's useful context for us to decide why we picked ably.

So this then is the asset that would go into the PRD

and go into any planning that we then go on to do from here.

We've even still got, you know, just 18% context used here.

So we could just go and write a PRD from this point too,

directly from the research.

That way the research, all of the issues in the Kanban board,

and everything would rely on this research.

And I hope you can see now from having done it

that the human in the loop part is really important.

What I would do for a production application

is I would go into each service,

kind of investigate in depth and verify what the AI was saying to me too.

Because as part of a research, you often need to winnow down

and figure out exactly what approach you want to take,

or at least which one you want to prioritize now

and maybe test out and prototype.

I'd love to hear if you noticed anything different from that,

or if you have any great ideas

for how you want to use research in the future.

It's a really, really great tool.

I don't use it every single time,

but when I do, it feels really effective.

I suppose the last thing I should mention

is why we're including it in the local file system

instead of on like a GitHub issue.

The reason is that I want this to be really easily discoverable

by the AI that's doing the implementing.

We can certainly reference this file directly in the PRD

and in the issues so it knows to go and read it.

But if we later come back

and we need to fix some bugs with the approach,

then having the original research in the repo

is going to be really useful.

However, as I said before, beware of doc rot.

If we eventually move away from Ably

or Ably changes their underlying SDK,

then this research is going to go totally out of date.

And it's actively going to harm the agent

working on this code base instead of help it.

I tend to be really aggressive in deleting the stuff

because you can always just check in the Git history

and pull it out if you need it.

So I would say once you've finished the Ralph loop

that's working on this feature,

and once you finish the QA,

then you can just delete it from the repo.

Very nice work and I will see you in the next one.


### 078-AI Coding for Real Engineers p78 078 Prototyping Day 6 Human In The Loop Patterns

Whenever you're embarking out on a big build of something,

especially something that doesn't have a precedent

in the code base, it's often extremely useful

to get in an early prototype.

This is a technique that software developers

have been following for decades.

You're not quite sure what the client meant,

so you provide them with a prototype they can play with,

they can mess about with, and give you feedback on.

If you think of the plan mode as you and the AI

trying to work out in text what you're trying to build,

then prototyping allows you to actually make it concrete.

And along with research,

I tend to think of prototyping as a really key part

of building good applications.

Because you as the human get to impose your taste on the AI

before it then goes into the Ralph loop.

I tend to use prototyping a lot for front-end design.

I tend to get it to create multiple options for me

on a throwaway route.

And this also means that when the Ralph loop goes

and actually implements this AFK,

it's got this prototype to reference.

This is also really great for testing new tools.

For instance, I might want to just spin up

a new library or something,

maybe even in a throwaway repo.

I want the LLM to really put the new library

through its paces and maybe test something out.

And then having that janky little prototype

that I can then feed into the actual implementation again

is really great.

And of course, it's also really great

for testing new services.

This is where research and prototype

can work really well together.

You research a bunch of possible options

and then maybe you create prototypes

for all of those options.

Then you as the human can QA the prototypes,

offer feedback, maybe iterate on them a little bit.

And then you end up with the best possible solution

that can feed into a PRD

and then break down into issues for the Ralph loop.

What we're trying to do here is try to flush out

the unknown unknowns really early on in the process.

And there are lots of places

where prototyping is not useful.

For instance, bug fixing is the obvious one.

We know what the desired behavior is,

we just aren't meeting that behavior.

Extending existing features usually also means

you don't need a prototype

because you're usually just composing

existing functionality together to build something new.

If we've got 100 models in the application,

we don't need to prototype what a new model might look like.

We can just throw it together

from all of our bits we've got already.

However, if you do want to redesign a entire system,

then a prototype can be an amazing way to do it.

Now for me, I don't tend to use a prototyping skill

to create this prototype.

I'll probably just invoke my do work skill

and do a normal kind of human in the loop run with this.

The reason is I want to be close to the prototype.

I want to be offering advice and applying my taste.

And once that's done, I'll create the PRD

leaning on information in the prototype

and then create the Kanban board too,

again, referencing the prototype locally.

So this is really like a form of research,

but instead of researching external stuff

and saving explore phases,

you're actually making the implementation step simpler.

And I cannot recommend it enough as an approach.

So prototyping even before the PRD

or as part of building the PRD

is essential to applying your taste to products.

It's great for design.

It's great for testing out services,

even great for software architecture.

Nice work and I'll see you in the next one.


### 079-AI Coding for Real Engineers p79 079 Trying Out UI Prototyping Day 6 Human In The Loop Patterns

Okay, let's try out prototyping by taking the research that we did before and trying it out.

Our research is currently all theoretical. Before we were to actually implement this AFK,

I would definitely want to do a prototype. Because first of all, I want to know whether

the time I'm going to be waiting for the AFK is going to be worth it. I need to see this thing

working and fix any weird bugs with the implementation before we actually go and implement

it. So to get this going, I'm going to go into my Claude instance and I'm going to kick

off a prompt. The first thing I'm going to do is specify the do work skill. Then I'm going to

add in the plans live presence indicator. So I'm going to add in the research. Then I'm going to

say, I want to build a prototype of the research here. I want this on a throwaway route that is

only visible to developers. I want to create a local asset that the agent that ends up

implementing this in the real app can actually use. I think that's probably enough. I imagine

it's going to ask me some more questions as we go. The important point is that I've

specified I want it on a throwaway route that's only visible to devs. And I'm kind of explaining

the purpose of why I'm creating the prototype. If I was doing or interested in design here,

I would also say, okay, maybe give me lots of different options. You know, give me five

options for how we could actually design this on the front end. But I've already got a pretty

solid idea of how I want it to look. And that's kind of reflected in the design. So I

don't really need to do see multiple of these. I just need to see it working. So I'll

give you this prompt as something you can copy and paste below. Actually seeing this working

will mean you will need to go and sign up to ably and actually check it out. Or if you

just want to watch me do it, then I'll be there in the solution. If you do do it yourself,

then write down anything you see. And if you have any questions, then head to the

discord. Nice work, and I'll see you in the solution.


### 080-AI Coding for Real Engineers p80 080 Trying Out UI Prototyping Solution

Okay, let's run this and see what we get to.

It is exploring, of course it is.

A little side note while it's exploring,

I do still like having a do-work skill,

just because it allows you to do

these kind of human-in-the-loop mini sprints.

Just encoding the very simple stuff I want

out of a do-work skill, like the feedback loops,

like any TDD stuff I'm doing,

I still want to apply my rigorous code standards

even to these prototypes,

because it means that when the implementation

goes to actually copy them,

they'll be copying genuinely production-ready code.

Okay, it feels like it's ready to go

without me needing to do any planning,

so it says PMPM add ably, okay.

It now feels confident enough to start adding files.

I'm just gonna let it do its thing.

It's already at the point where it feels like

it's confident enough to run the types and the tests,

and it's now committing.

It's actually done something really nice here,

which is it's actually made the prototype components

reusable and exported from the prototype components.

In other words, it looks like it's designed

to be pulled out of the prototype

and dropped immediately into the real app.

This again means that the AFK implementation of this

is gonna be so simple.

It's also given me a how-to-test-it thing,

which is nice.

I'm gonna go and grab myself an ably API key,

and I'm gonna come back and see

if this does what it says it's gonna do.

I actually found this pretty confusing,

so I'm actually gonna ask it,

give me a detailed step-by-step guide

on how to acquire an ably API key

with exactly the scopes that you need.

So a nice way of just making my life

a little bit easier.

Okay, that's what I need.

Getting an ably API key for presence,

get the API key, set the right capabilities, beautiful.

Having some actual research here

means that we don't need to actually go out

and explore this.

It's just basically churning stuff out

from the research, beautiful.

So I've now followed these steps,

and I've got an ably API key in my .env.

That's lovely.

Okay, and I have logged in,

and I'm on dev presence,

and I've logged in as Emma Wilson, a student.

It's telling me open this page

and open multiple browser tabs as different users

via the dev UI to see presence updates in real time.

So on the tab on the right,

I have logged in on an incognito tab,

so hopefully they won't share the same session,

and then I go in,

and I'm gonna go in as Olivia Martinez,

and now going to log onto dev slash presence,

I connect, and we see on the left-hand side

that we have Olivia Martinez too.

If I then come out of here and go back,

then the presence disappears instantly.

So there we go.

Our presence setup is genuinely working.

At this point, I might want to iterate on the prototype

a little bit more.

I might want to make it a bit more

like what I imagine it's going to look like in the lesson,

but to be honest,

all of the unknown unknowns

are flushed out at this point.

We know that the service works okay,

and we know that we can connect to it easily.

All of the rest of the stuff I'm confident

can be worked out AFK.

So there we go.

That's the power of prototyping,

putting a little bit of human-in-the-loop work in early

in order to validate your assumptions

about an unknown unknown.

Anyone who's an experienced developer

will know the value of this already,

but I think it's important to categorize it

as human-in-the-loop work.

We could have potentially said,

okay, just go off AFK and make this happen.

Then I'll review it later.

But the idea that you can sit and iterate

with a prototype and just get into a tight feedback loop

with the AI is so beneficial,

and then pays dividends

when you go to actually implement it.

Nice work, and I'll see you in the next one.


### 081-AI Coding for Real Engineers p81 081 The Prototype Skill Day 6 Human In The Loop Patterns

Since working on this course for the first time, I've been doing a lot more prototyping

and I'm even more convinced that it's a fantastic way to just flush out unknown unknowns during

the planning process.

To that end, I've built a prototype skill here which is in my skills repo.

It's a little bit churny at the moment, you know it's undergoing quite a lot of changes

so it's not quite ready to go into the course but I wanted to point it out to you

as a pretty cool thing that you can use when you want to do prototyping during

a grilling session or during any stage in the process.

You can find it and download it at the link below.

In its current state, the prototype skill has two branches.

So you essentially have one branch for pure logic testing and one branch for UI testing.

For UI testing, it generates several radically different UI variations on a single route,

either switchable via a URL, search param, and a floating bottom bar.

This means that you end up with this little bottom bar on the bottom of the screen

that you can click left and right and it will show you the possible prototypes in the UI that you're building.

This is incredibly cool for UI design, for just trying to figure out what it should look like

and the radically different UI variations is something that you can iterate on.

So you can go, okay we've got A, B, and C to decide between.

I like the look of A but let's take a little bit from C. It's just really cool.

The thing I tend to use more often though is the logic variant.

The logic variant allows you to build a tiny interactive terminal app

that pushes the machine through cases that are hard to reason about on paper.

What this means is if you have a sort of complicated data model

or you have something that's changing over time like most apps do,

then you can see it in the terminal and it will give you actually interactive key presses to press

in order to move it through time.

This is great for testing out any kind of interaction on a piece of data

and that's basically what most apps are.

So now you know what prototyping is, I urge you to go and check out the actual prototype skill

which when you want to prototype will give you really nice options.

I may also add future branches to this as well so you know there are probably

variants of prototypes that don't fit into these two branches.

And so watch this space as the skill develops.

Thanks for watching and I'll see you in the next one.


### 082-AI Coding for Real Engineers p82 082 Designing Codebases Ai Loves Day 6 Human In The Loop Patterns

There's one extremely important place where human in the loop can make a crucial difference to the success of your codebase.

And that is in defining software architecture.

The current generation of agents are not good at thinking about software architecture,

and they generally design systems that are hard for themselves to use.

So organising codebases for AI is going to be an essential skill

and probably one of the highest impact things you could do to your codebase.

Let's look at what AI sees when it looks at a bad codebase.

A bad codebase looks like this, where there are dozens and dozens of modules here,

each with maybe some exported functions, some functionality inside them.

And to find the correct code to actually explore this codebase,

the AI has to go through, understand which modules are imported by which other modules,

as to go through the entire chain, or at least large chunks of the import-export chain.

What this basically means is that AI can't at a glance understand where to find specific functionality.

And these tiny chunks here are really hard to get good tests out of.

We know the importance of good feedback loops to AI,

and the way you'd have to test a module like this is really just to sort of test,

OK, maybe just write some tests for this module on its own, then this module on its own,

then this module on its own.

It means we don't get a good sense for how all of the pieces of the codebase work together.

And if one of these individual modules change, then we need to change the test as well,

because it's too coupled to the shape of that tiny little module.

Now, you as a human will probably be able to navigate this codebase OK,

because you can kind of understand and start to develop an instinct for the purpose of these chunks of code.

You'll know that, OK, these groups of files over here, these relate to authentication.

These groups of files over here relate to just the API layer.

These front-end components pertain to a certain feature.

These ones pertain to a certain feature as well.

But the AI doesn't have the same advantage as you.

It can't develop memories about the codebase in the same way that you can.

So what it sees when it goes into a bad codebase is this.

It has to recreate all of the relationships from scratch.

So then how do we make this codebase better?

How do we make it so that AI can detect and understand what the purpose of the code is

without needing to develop a memory or without needing to traverse the entire graph?

Well, we can restructure the code into larger chunks

and we can bake in the intention of the code into the structure of it.

This is a concept that John Osterhout from the philosophy of software design calls deep modules.

Deep modules have two parts.

They have an interface, which is this little thin barrier up there,

and then the implementation.

The interface is a thin little layer between this massive module and the rest of the world.

On an interface, you might define functions or methods.

You might say, OK, this is how you're going to call this function.

This is how you're going to call this function.

Only these properties, etc, are available and you call them in this way.

And then behind the interface, you then stack a bunch of implementation.

In fact, the more implementation you can fit behind a simple interface, the better,

because that means that different parts of your system are just relying on this simple interface,

which should rarely change.

And so you can test or write tests for these huge units individually.

These tests will test the public interface of this module.

And because the public interface won't change that much, these tests also won't change that much.

And you can really experiment inside the tests and write really detailed implementations.

So when you have a code base structured like this,

where you have a bunch of deep modules with simple interfaces,

then the AI can actually just read the interface and understand very quickly what the module is supposed to do.

And from a high level, it can get a very fast sense of what the entire code base's purpose is

and where it might need to change things to adjust an implementation.

There's another massive bonus to this approach, too,

which is it decreases the cognitive load on the developer.

If you're a developer maintaining this system, then you have to keep the internal map in your head.

And because AI is changing this code all the time,

moving these boxes in and out and around and doing weird things with them,

then that cognitive load is really, really hard to maintain.

And it often leads to devs just feeling really knackered when they use AI.

This, by the way, is something that's really important to mention,

that cognitive load is something that I think everyone is experiencing more of having used AI.

You want to move so much faster and you want to continually push with AI

to just maximally parallelise yourself to do as much work as possible.

So any strategy that's out there that can decrease cognitive load can just make your life a lot easier.

So organising your code base into deep modules not only allows the AI to navigate it better,

it also means that the map that you have to keep in your head is simpler.

Not only that, but you as the developer get to just focus on the interfaces,

focus on how these modules are designed.

And you can largely let AI take care of the implementations.

I find myself doing much less code review on these stuff inside these boxes

because I know that it's tested.

I usually find myself reading the tests more than I do the implementation.

So I think of these as grey boxes.

I can look inside them, you know, they're not fully black boxes,

but they're grey boxes because by default I want the AI to handle what's in the implementation

and I can help design the interfaces.

Let me give you an example to make it a bit more concrete.

For those who don't know, I record all of my content on a custom video editor that I've built.

And as you can imagine, it is really, really complicated.

There is the entire front end for the video editor, which has a bunch of modules associated with it,

many of which I had automated tests for individually,

like a reducer that did some state in the front end

and some of the very simple selectors which pull down state from that, you know, sort of front end stuff.

Then I had maybe an even more complex back end API,

which was spread out over several API endpoints.

There were maybe actually about 20 files here, sort of focused on the back end API,

and all of them were really interrelated.

The back end API then contacted a CLI that I use to monitor files that are being created from OBS

that I need to sort of detect the silence on, blah, blah, blah.

There's basically a CLI that handles that stuff.

And then there's a couple of related modules for saving stuff in the local database I have.

So I was getting a lot of bugs in my video editor,

and it was a lot about how these pieces interacted together.

In other words, I would try to fix the bug on the back end,

but then it turned out it was actually the way that the front end was calling the back end API.

And then maybe it was the fact that the back end API wasn't calling this CLI properly,

rather than the CLI had a bug in it.

So what I needed to do was find some way to turn all of this into a single testable unit,

because then instead of breaking my brain trying to figure out where the bug was

between all of these four possible places,

I could just wrap the whole thing in an integration test and test the whole thing end to end.

And then all of the stuff inside here,

I wouldn't necessarily need to care about its internal structure so much.

So that's what I did. I wrapped the entire thing in a service.

I essentially built two parts of this, an SDK that could be called from the front end,

and then a sort of API handler on the back end that took messages from that SDK.

This basically turned the entire thing into a single deep module.

And now whenever anything goes wrong with my video editor,

I'm able to do TDD on the entire editor flow.

Now identifying that this was a problem and identifying that wrapping it in an entire service

and deepening the module was the solution,

I don't think AI is capable of that right now.

Certainly not without a human prompting it.

So that means that you as a developer need to develop the language

in order to talk about these deep modules with AI.

Designing your code base to work this way needs to be embedded in your planning process.

Nice work, and I'll see you in the next one.


### 083-AI Coding for Real Engineers p83 083 The Improve Codebase Architecture Skill Day 6 Human In The Loop Patterns

So now we know that codebase architecture is important and we should have a good idea that deep modules increase the quality of your codebase and make it easier for AI to navigate.

But how do we actually make that concrete? How do we take a bad codebase and turn it into a good codebase?

Well, I have provided for you an improve codebase architecture skill.

This skill walks you through your codebase and looks for opportunities to improve it.

It starts by defining what a deep module is.

It has a small interface hiding a large implementation.

It then just tells the AI to explore the codebase, use the agent tool with sub-agent type explore to navigate the codebase naturally.

It says to explore organically a note where you experience friction.

Where does understanding one concept require bouncing between multiple small files?

Where are modules so shallow that the interface is nearly as complex as the implementation?

That's really nice. This is such a common one.

Where have pure functions been extracted just for testability, but the real bugs hide in how they're called?

This is something that LLMs do all the time.

They say, OK, let's make this testable by just pulling out this one small bit.

But actually, you still get bugs in the real implementation.

Where do tightly coupled modules create integration risk in the seams between them?

I use the writer skill as skill to put this together.

And it honestly is on a tear here. This is just perfect.

So once the exploration is done, it's going to present some candidates.

It doesn't propose any interface designs yet.

It just basically says, OK, so there's this cluster of shared concepts.

They're coupled together. We should probably group them into a deep module.

Then the user picks a candidate. That's step number three.

Then step number four is to design multiple interfaces.

So this one spawns multiple subagents in parallel and each are going to produce a radically different interface.

I found that this gives you the best opportunity for getting lots of diversity,

lots of diverse options that can then be pulled together into the right design.

Then it should just below here give you a recommendation.

Which design you think is strongest and why,

and if elements from different designs will combine well, propose a hybrid.

Finally, the user picks an interface or accepts your recommendation.

And then you create a refactor RFC as a GitHub issue.

You can then turn that RFC directly into a Kanban board, breaking it down into issues if you're happy with it.

Now, the way I usually run this is I usually identify myself something that might be a problem.

And so you can, say, improve your code base architecture looking at this specific area.

But for this one, I'm just going to run it clean.

I would like you to do the same as me.

And let's compare our notes in the solution.

Good luck. And I'll see you there.


### 084-AI Coding for Real Engineers p84 084 The Improve Codebase Architecture Skill Solution

Okay, I'm going to run this. It is probably going to do its exploration and I'll see you once this exploration is complete.

Okay, it has come back with a bunch of options.

The first one is a quiz subsystem. So merge scoring, CRUD and XP awarding into one deep module.

This is the one I was kind of hoping it would pick.

When I put this code base together, I decided to leave one service that had been badly coded.

In other words, this quiz scoring service uses a raw database instead of using the actual DB from elsewhere.

It has like NEs all over it, quiz data, answers, etc.

And it actually has no tests accompanying it.

So it's literally just as if it's been written by a contractor, someone just foreign to the code base.

And so I do think it's a good idea to wrap this in a deeper module in order to test it all.

Honestly, there are lots of decent candidates here.

The student progress system, like consolidating a bunch of stuff into a single module.

This stuff can be pretty hard to read if you're not used to some of this language,

like side effects and transactional domain operations and monoliths.

But if you have any questions about the language, I recommend you ask the LLM directly what it means when it uses certain phrases.

Learning these phrases will actually benefit you in the long run because then you can prompt the LLM with those phrases.

I'm actually going to zoom to the bottom and ask the LLM, which of these would you recommend?

This is like asking the waiter which meal he would most prefer.

OK, and it's recommending number one, where we can see it because it's the only place in the code base mixing raw, better SQLite 3 SQL with drizzle ORM.

I like that. That's freaking hilarious.

You're already looking at it because the quiz scoring service is open in your editor.

OK, I guess so. Cool.

So at this point, I'll just say, yes, let's explore number one and let's see what it comes back with.

So it's going to pull in all of the current quiz files to understand the exact interfaces.

And it's now spawning some several different design agents, one with a minimal interface, one with a flexible interface and then a third with a caller optimized interface.

Now, interface design is like a really, really deep topic.

And it's something that you will get better at as you design more of these systems.

But seeing multiple options from the AI is really, really useful just for developing taste.

And you don't necessarily need to get it perfectly right, because the next time that you run improve my code base architecture, you could target the thing that you've done already and make improvements to it.

So I'll wait for a minute until these three come back.

OK, we have some designs to look at.

Before I actually look at them, I'm going to zoom all the way to the bottom and I'm going to see, OK, it recommends design B.

So before I read this stuff, let's actually go and look at design B.

So this is essentially a function called create quiz module where you pass in the database, you pass in the scoring strategy.

So that's dynamic.

And then you pass in the quiz pass XP.

And then this has a few methods on it.

So get quiz for lesson, get best attempt, get latest attempt, attempt history, get stats, submit attempt, save quiz and delete quiz.

I see. And the XP amount is completely configurable outside of it.

So it doesn't own the XP amount.

This means that whether you're an instructor creating a quiz or updating a quiz or whether you are a student taking the quiz, you're essentially calling the same module, which I really like.

That means all of the quiz stuff is in one place and I needing to fix anything to do with the quiz will put it inside the quiz module.

So I dig this. I think this is great.

I can see that the recommendation at the bottom, too, it says to take design B's factory and injection, but borrow one thing from design A,

use an XP awarded Boolean rather than an XP awarded number or null.

The XP amount is an implementation detail that the caller doesn't need.

I agree with that. It's now asking if I want to create a GitHub issue.

And I do. And just like that, we have an issue ready to go.

The quiz subsystem is split across three shallow, tightly coupled services that callers must manually orchestrate.

And it's in that manual orchestration that the bugs come up.

If we zoom down below, we can see that there is a proposed interface.

This absorbs all quiz concerns behind around eight methods.

This looks super duper good to me.

I really like that it gives you a before and after of how the caller actually calls these functions before it would have to grab the quiz by the lesson ID,

then grab the quiz with the questions, then get the best attempt.

And to figure out the result, it would have to compute the result and then award XP.

But afterwards, it now just has one or two calls on the loader where it gets the quiz.

And if there is a quiz, then we get the best attempt.

And in the action, it's now just one call instead of two.

So overall, this is a relatively small change.

We're just combining more functionality together into a larger testable unit.

And over time, as you do this more and more to your code base and as you bake this thinking into your planning,

you'll end up with a code base that's more testable, where the feedback loops are stronger and that's more easily navigable.

And in theory, we could take this quiz module and just turn it into a gray box.

You as the user can now just completely test from outside of it.

And you don't need to worry about what's inside.

As long as the XP is awarded and as long as the quiz gets passed and as long as all those functions work and test correctly, then you're good.

So hopefully that makes the idea of what a good code base looks like more concrete.

And feel free to grab that skill so that you can turn it on your own code bases and see what comes out.

Nice work. And I will see you in the next one.


### 085-AI Coding for Real Engineers p85 085 Adding Module Awareness To Our Planprd Skill Day 6 Human In The Loop Pattern

Now we should understand a little bit more about what the cure for a bad codebase is.

It's a human working with improved codebase architecture, iteratively improving it over time,

applying their judgment and finding opportunities for deepening modules within that codebase.

But there's kind of a prevention and cure thing happening here, right? Because we know the cure,

but how do we prevent these bad modules from being created in the first place?

Well, I would say that whenever you're building new features, whenever you're constructing

anything, and especially something that takes multiple sessions to work on via an AFK agent,

you need to build in module awareness into your planning. So that's what I've done to the two

PRD skill here. Instead of being a two-step process like we had before, it's now a

three-step process, where just before we write the template it says to sketch out the major

modules you will need to build or modify to complete the implementation, actively look for

opportunities to extract deep modules that can be tested in isolation. A deep module is one that

encapsulates a lot of functionality in a simple testable interface that rarely changes, and check

with the user that these modules match their expectations. So this brings module awareness

into the most important moment, which is when you're designing the new implementation,

you're thinking about and sketching the major modules that are going to be built

and where they're going to be tested. This means that the right seams are going to be

tested, that the TDD loops that you're using are going to be properly enforced. You're going to get

higher quality tests and so a higher quality implementation. This is prevention. We are preventing

bad shallow modules from invading our code base at source. If you fancy it then feel free

to take this updated 2PRD skill, try something out in the code base and see how it works. Or

feel free to jump in the discord and see how you might improve the skill even further

and bring some of your own architectural expertise into the planning phase.

Nice work and I will see you in the next one.


### 086-AI Coding for Real Engineers p86 086 The Final Workflow Day 6 Human In The Loop Patterns

Well done. You have come to the end of AI coding for real engineers. You've worked your way through

all the material. Very, very nice work. And I wanted to jump in here and just give a summary

of where we've got to and what the whole process looks like. I think of that right now as being

seven phases to AI development. And we have worked through each of these in turn in a kind

of weird, secuitous order that has brought us back to these seven steps. The first step then

is the grill, is the interview where you get interviewed for some sort of idea and just to

harden the idea before you eventually turn it into a PRD. This grilling may result in a little

bit of research that's required, for instance, to explore third party APIs, to explore tooling,

to maybe even explore options or just see what's out there. Research may also involve prototyping

where you actually maybe stop the grilling session for a bit. You build something and then you go

back to grilling all the while figuring out where you're going. All of these steps then result

in a product requirements document or some kind of spec, some file that sits in your set of

issues that can be reviewed by your team. That is the destination documents, the document

of where you're going. Once you figured out where you're going, i.e. the PRD, you've got

to figure out how to get there. You turn that PRD into issues with individual tickets,

with blocking relationships. You then implement it either human in the loop with you watching

or totally AFK where the agent just goes through, picks up all the issues and gets to your

destination. And finally you review its work. You check that we reach the destination correctly,

that all of the stuff from the PRD was implemented. You check it against your

coding standards and you also review the entire process to make sure that any prompt

updates that need updating are there. You update any skills that needed changing along the way and

you write down your process and you compound and get better and better and better at the

whole thing. And this right now is just my tech by the way. You are totally free to do these in

a different order if you like, to find your own way through these maze, to call these whatever

you like. But this is how I see AI coding right now in terms of the best way to do it. I hope

you enjoy bringing these techniques to your organization or just integrating them into your

personal development and building cool stuff with them because that's the whole point of

all of this. AI coding allows you permission to build stuff that you wouldn't have thought

possible before. And crucially I hope you enjoy it as much as I do. Nice work and I will see you very soon.


### 087-AI Coding for Real Engineers p87 087 Appendix Greenfield Projects Day 6 Human In The Loop Patterns

There's a common question that comes up again and again when I do these courses.

And so I wanted to add a little appendix here to talk about Greenfield projects

specifically. If you've never heard this term before,

Greenfield is when you're starting in a new project where there is nothing

there before you. The field is green. It has not been built on yet.

Brownfield means that the field has maybe something on it. You know,

you're building in an existing setup.

This might be a legacy code base that you already have,

or it might need to integrate with stuff that's already there.

In other words, there's stuff on the ground already that's impacting what you're

doing and where you're going.

Most of the work we've been doing in this cohort has been Brownfield.

I've given you an existing application and we are working within the

constraints of that application using pre-existing patterns in the code base,

kind of working on stuff that's already there from a pretty solid base.

But how do you start when there's nothing to start from?

How do you start from a blank page? Well,

the first thing I start with is a grilling session.

I have some kind of vague idea that I need to start hammering out and I chat

with the agent about it. From there,

I would then take this and save this into research files.

So anything that I capture during those grilling sessions would be saved,

usually in the early phases as markdown documents in the repo itself.

The idea is I would have multiple grilling sessions continually refining my

idea for what we're trying to build and save the output of those into

markdown documents so that we build up this kind of almost like a code base,

but of markdown documents with decisions that we've made. From there,

I would start to look at prototyping.

So I would take some of the research questions I had,

I would turn them into prototypes. Maybe those prototypes would get reused.

Maybe they would just get sort of saved in the code base as prototypes.

And then I would continue to iterate on those.

So I would start to get a clearer picture of the thing that I actually

wanted to build. Once I would have that clear picture,

then it's time to start writing the product requirements documents.

And this will look a little different in a Greenfield code base to a

Brownfield code base. To understand why we need to talk about these two pieces

of terminology, we have UX and AX here.

UX here means user experience.

So the experience of the end user. And in a Brownfield code base,

we've usually got all of the fundamentals nailed down and we can start

focusing on the user. But in a Greenfield code base,

we are really starting like the first thing we need to think about is the AX,

the agent experience, the experience of the agent working in the code base.

So that means our first product requirements document not only needs to specify

some UX stuff, some kind of end facing user experience goals,

but also we need to focus on the agent experience,

focusing on the feedback loops,

focusing on the languages that we're using on the technologies that we're

using. Let's actually list these out so we understand more what we mean.

We need to first look at the feedback loops,

the types and the tests and the pre-commit hooks that will,

and the formatting as well,

that will make sure that the agent is producing high quality code.

We need to talk about technology choices.

These are often really difficult decisions that are difficult to swap

out of later. We need to figure out what language we're going to use,

what front end framework we're going to use if we're building a front end

app. And that's really important to grill on with the agents.

We may need to think about the module shape, the initial shape of the modules,

the deep modules that we're going to create,

because we know how important code base architecture is to agent experience.

And finally, we need to look at the testing strategies as well.

So which ties into the module shape really,

what things are we going to mock? Are we going to use a test database?

All of this stuff will mean that we're producing higher quality code from

the get-go. So that means that your first PRD is really crucial because

you will probably need a PRD for the AX before you even look at the UX.

Now, of course, what you're building will influence your technology choice,

will influence your testing strategy,

and will definitely influence your module shape.

So you can't sacrifice AX for the sake of UX.

They need to be tied together.

The thing that you're building needs to feed into the way that you build

it. But once you've got your AX sorted, often via its own PRD,

then you can start going through implementing issues, grabbing all this,

doing reviews, and we're back into essentially a brownfield code base.

So really I think of the difficulty of setting up a greenfield code base is

really just setting up the agent experience. Once that's done,

then you can just immediately start going through the loop that we've talked

about throughout this entire course. Hopefully that makes sense.

If you have any more questions, then do ask them in the Discord.

I think this is a particularly juicy topic to grill on together.

How about that? Nice work. And I will see you in the next one.


### 088-AI Coding for Real Engineers p88 088 Appendix grill-with-docs Day 6 Human In The Loop Patterns

Hello, I'm back with another appendix.

And this one, I think solves a problem

that I started to have with GrillMe

as I started to use it more and more,

especially in the same project again and again and again.

And to understand the problem I was having,

we need to understand the sources of information

that the agent has when it's working in your code base.

The first source of information, obviously, is the code,

the current commit of the code

that's currently accessible to the agent.

The second one is the commit history.

It can look here to access historical things about the code,

look at how things used to be,

bisect it to find bugs, et cetera.

Then we've got GitHub.

In other words, things that people have said

about the code accessible via the GitHub CLI

or whatever issue tracker you plug in here.

This is really good if you have issue numbers

in your commit history,

then the agent can go into GitHub

and try to find the reason why a change was made

or things like this.

And then you have user messages,

what you yourself say about your code.

Now this all looks good until you realise

that there are two questions

that it's really hard for the agent to answer

just by looking at these four sources.

And the first question is, why did you do it this way?

In other words, if there's a weird trade-off

visible in the code, like why was it done this way?

Why was this slightly strange-looking choice made?

Why was this technology chosen instead of this technology?

Why did you do it this way?

The agent might have access to this information

if it has access to everything it needs to.

It might be able to look in the commit history

where the change was made,

link to the GitHub to look in the issues,

pass through everything to understand it.

But it's really hard for the agent

to access this information.

And it's really crucial that it does

so that it doesn't recommend

that you do it the same way again.

The way that many engineering teams document this

is via ADRs, architectural decision records.

These are records of important decisions

that were made during the design of the system.

They're usually just little markdown files

that explain why a decision was made,

what alternatives were considered.

And it means that the ADRs are in the code base themselves

so they're easily accessible

to any agent that's running in there.

So I have found that an ADR is a really nice way

to help the agent quickly answer this question

because it's a very important question.

However, there's one question that ADRs cannot answer,

which is, what on earth is an XXX?

In other words, you're using some kind of jargon

that the agent just doesn't understand

because it's jargon that you use in your business,

but the agent doesn't know it.

For instance, in my course Video Manager,

the thing that I am recording all of these videos on,

which is an app that I've built,

I have various bits of jargon

that are really hard for the agent to understand.

I make videos for my lessons,

but I also have videos for YouTube.

I have pitches that are then,

videos are attached to those pitches

or they can be standalone videos

or the videos can be as part of lessons.

I have a feature where I'm able to plan lessons

within the scope of a real course.

And so you have lessons next to ghost lessons.

You can have ghost sections,

which might be added in future.

And when you turn a lesson into a real lesson,

then that turns the ghost section into a real section,

which is called the materialization cascade.

You see what I mean?

There's just layers of jargon,

layers of jargon that is really convenient for me to use

because I understand it,

but the agent doesn't understand it.

So I have found that a shared glossary

is incredibly useful for the agent

when it's working in your code base.

I keep mine at a context.md file

at the root of the repository.

And we have things in here like the course,

the course repo, the section, the lesson, course versions.

Let's see if I can go and find a ghost lesson,

ghost section.

Do I have the materialization cascade here?

The chain reaction when materializing

a lesson inside a ghost course.

But there's a really tight little definition here.

And if there is a problem with the materialization cascade,

I can just say that instead of having to say

this whole verbose extra definition.

By the way, a ton of these ideas

come from domain-driven design,

which talks about a ubiquitous language,

a language that's shared between domain experts,

the people you're building the thing for,

and you as the developer,

and also all the way into the code itself.

This means that the glossary not only helps you talk

to the agent better about the thing that you're building,

but also means it's easier to name variables,

easier to find stuff in the code base

because it's all conforming to the same language.

So you can start to see the benefits

of why a shared glossary would be useful.

And I think it makes sense for why ADRs are useful too.

So the question then becomes what phase

in our development cycle should we create these docs?

My immediate instinct is we need to create them

before we create the product requirements documents,

before we describe where we're going.

Because if we do that after the PRD,

then all of the issues won't have the documentation

they need to correctly create the issues, right?

Like they'll be using old domain language.

It doesn't make sense to me.

So for me, I think we need to create them

at the earliest possible moment

during the grilling session.

When we're grilling, when we're initially talking

about the thing that we're trying to build,

we need to be using that shared language.

So we need the glossary.

If any decisions are created inside that grilling session,

then we need to turn them into ADRs.

So the way this will often work

is I will grill with the agent.

We'll talk about the glossary.

We'll hammer out any new terms that need to be added.

And then we'll add any ADRs.

And then I'll turn that into a commit

that I commit to the repo.

And then we'll create the product requirements documents

on top of that.

But you might be thinking that sounds pretty annoying

if you're having to remember yourself to create ADRs

or to like hammer out this glossary every single time.

Surely the skill could handle that for me.

Well, guess what?

There is a skill for that.

This is my grill with docs skill

that essentially runs a grilling session

but has a little bit of extra stuff here

for creating a context.md here,

which is the glossary and also for creating ADRs.

This is essentially a drop-in replacement.

And this is now what I'm using

for every single code base that I have.

Every time I'm working in code,

I will tend to use grill with docs.

And every time I'm working in

just like doing non-code stuff,

I will use grill me instead.

You can see that in the instructions for the skill,

we have instructions for updating context.md,

our glossary, and also offering ADRs

and only creating ADRs

when the decision is hard to reverse,

surprising without context,

or the result of a real trade-off.

It also has some context pointers in here

to a context format that sort of ties down the format

and also the ADR format too.

So the template for the ADR.

Overall, I found that grill with docs

is just an extremely useful skill

and adds that extra layer that's needed

to answer the most confusing questions

for the agent easily in the code base.

I encourage you to use it

as a drop-in replacement for grill me

and let me know how you get on with it.

Nice work, folks.

I will see you in the next one.


### 089-AI Coding for Real Engineers p89 089 Office Hours - Day 6 Morning

Morning, morning, morning or afternoon, whatever it is where you are. Hello, folks. I'm here

a little bit early. I was just sort of waiting around, so I thought I would rock up and

say hello. And also make sure that I'm on the right thing because last time I went on

the wrong stream and was chatting to myself for like two minutes. So hopefully I'm on

the right one. Hello, folks. Welcome, welcome, welcome. Welcome to week two. It's extremely

exciting to, I don't know, be halfway through the cohort, I suppose. Seeing all the material

leak out to you guys, seeing all your nice things you're saying about it, the great

enormous amount of questions we've had over the weekend in the Discord. Good morning,

folks. We're doing Slido again and I'll leave this up just so I can, you guys

can join. What's up, what's up, what's up? I'm just going to open my window

two seconds. We've got a little interesting little journey to go on today. We're going to do 15

minutes of Q&A, then I'm going to show you something for 15 minutes and then we're going

to do 15 minutes more Q&A just to mix up the format a little bit. I've also over the

weekend been learning how to do a Rubik's Cube and that will feed into what we're learning

about today too in the little middle section. Your boss said he'll buy me more courses if I

can get one answer to his question from you. I think this office hours will answer your

question. I think I saw your question in the thread since you posted it in a few places.

Where are we calling from, folks? What's the latest? Here we go. 54 of us so far. I mean,

that makes sense since we're only a couple of minutes ahead. I went to a tractor show with

my son, Stockholm, Sweden, from India, Austria, Raphael, what's up, New Zealand. The purpose of

life is to play and experiment within this strange world where we are. Devon, UK. I went

to university in Exeter so I know Devon very, very well. Where are you from in Devon? I need

to know. Halfnáidur, Iceland. I have no idea how to pronounce Icelandic. 69 of us. What's up,

Ben? How are we doing? Ben's very local to me actually. Rajkot, India. You'll never miss an office

hour. Very good. I mean, if you're in hospital or something, please don't come. What's up,

Palestine, Stafford, Kilmington. Kilmington? I know Axemanster. I don't know Kilmington.

What's up, folks? Okay. Chiang Mai. How are we doing? What time is it in Chiang Mai?

What's up, Craig? For those who don't know, I'm also in Oxford, UK.

Okay. All right. I think we're basically ready to go. We've got some good questions already.

Let's get cracking. We're going to do this for 15 minutes until quarter two. Then I'm going to

show you something cool for 15 minutes. And then we're going to do more Q&A in 15 minutes.

Yeah, this office setup. How nice. It's so much grubbier in here than it looks. It looks quite

neat. And actually, it doesn't even look that neat. I have a little marker to myself to make

sure all the books are standing up on the bookshelf, but they're not currently.

All right. So let's go for question number one. Feel free to join the slido. You can

vote on questions. Voting on questions is how it decides to show me the question. And so,

the top voted question will be the one that comes through. So if you see something interesting,

then make sure you vote on it to surface it. How do you efficiently explore a code

base for the first time to create documentation both for devs and for agents? So this,

immediately I want to do something I don't have, which is to open a TL draw.

What we've basically got here, innate in that question is something really interesting,

which is that there's a difference between documentation for devs and for agents.

Now, something that has occurred to me kind of since building the course is that these two need

two proper terms. We need a term for DX, developer experience, and AX, in other words,

agent experience. And these two, like the Venn diagram between these two terms,

is really interesting because for developers, if you give developer lots and lots of documentation,

are they going to read the docs? Are they going to skim the docs? Are they going to

make sure that they get every line correct and they memorize it? Probably not. If you give

an agent a bunch of documentation and tell it to explore the code base and use that

documentation to inform an agent's behavior, the agent will probably behave a lot better.

And so, the differences between DX and AX, obviously there's things that they both need.

They both need a well-designed code base that's easy to change. They both need automated checks

and feedback loops. They probably both need human review to certain extents as well,

or they certainly both benefit from them. But the question here is how do you explore a code

base to create documentation for devs and for agents? I would say that DX is getting a lot

less important now and AX is the thing you need to be thinking about. So when I'm thinking

about is my code base easy to explore and how do you explore it for the first time,

I think I do want to... I will answer this question more fully in the middle section

because we're going to be talking about the teach skill. And I would say the teach skill,

which is an in-progress skill that I've got kind of cooking at the moment,

which I think is nearly ready for prime time. If I zoom over to my skills repo, go into skills,

in progress and teach here, this essentially teaches you anything. It taught me to do a

Rubik's Cube over the weekend. And I think that teach, if you personally want to learn about a

code base and learn everything there is to know about the code base, or rather all of the

useful stuff that's going to help you work in it, then I think teach me about this code base

is probably going to be the way to go. But for me, if I'm wanting to explore a repo for

the first time, create good agent documentation about it, then just letting the agent do its

thing naturally, not steering it too much is how I prefer to do it. Because if the agent unsteered

is going through the code base and running into certain issues, that tells me something about

that code base. Hopefully that makes sense. What do I think of tools like GraphiFy? Is it

better to let the agent discover the code base by itself despite the token cost? Let's have a

look at GraphiFy. So GraphiFy is one of a bunch of tools which essentially try to create

a knowledge graph out of your code base. And it turns your code base or rather

creates a bunch of summaries of your code base and puts them in a graph. So in theory,

that graph is easier for the AI to navigate rather than looking directly at your code base.

I think I'm suspicious about tools like this. Not suspicious in their motives. I'm suspicious

as to whether they work and rather I'm skeptical is the right phrase. And I'm skeptical because

teams like Claude Code have basically come out and said this approach is expensive and it

doesn't work that well. The thing that really works well is giving the AI access to the file

system, giving access to powerful tools like grep and letting it search through files. That's

what works. That's what's actually efficient. Whereas GraphiFy is not very efficient or rather

the approach that GraphiFy takes of creating this layer on top is just not very efficient.

So that is why I'm skeptical about tools like this and why I don't recommend. I haven't

personally explored them, done an A-B test or anything. You can try it but I just don't think

it's that good really or rather I don't see it as an avenue worth going down.

I'd be interested to hear what your experience is.

AI is moving fast. I'm feeling overwhelmed by everything I feel I need to learn. How do I

prioritize and manage my learning without burning out? So the approach that I've taken here

is that and the thing that I'm currently thinking is that AI is moving fast, right? But what are

we talking about when we talk about AI? Are we talking about new models coming out? Are we

talking about new harnesses coming out? What it seems like to me is for the past seven months

or so since December things have kind of settled down into a bit of a pattern which

is that we're mostly using harnesses with a similar shape. Harnesses being claw code,

being cursor, being codex. They mostly have a text box at the bottom where you send inputs

to them. They all are constrained by a context window and their capability is getting better

but it's not getting better at a sort of massive pace or anything. It's pretty steady

and so what I think is you can get a lot more now out of refocusing on your own practice

as a developer. What I mean by that is thinking about every little step that you're going through

when you build anything, when you're fixing a bug, when you're making a change, when you're

refactoring, when you're doing performance optimization. Whenever you're doing any of

those things you should be thinking about your own process and thinking about how you can

teach an AI to do it because AI is, I've talked about this in previous office hours,

there's kind of two ideas here. There's two types of programming, tactical and strategic.

Tactical programming is the on-the-ground programming, the stuff that you do

like the sergeant running around with a gun to try to solve the problem of today.

Strategic is the long-term view, long-term vision. AI is eating tactical stuff,

the actual coding but it's not yet very good at strategic stuff. You really need a human

there thinking about what the best thing to do is, what to build. AI knows how to build,

it doesn't know what to build. And so I think by focusing on your own skills,

by just working with what we have today, which I don't think the form factor is going

to change that much, I think you can do a pretty nice job. Security with agents,

what are key security considerations and best practices when working with AI agents?

There's two things here. There is the security of the software that you're creating

and then there's the security of the agent itself. Agents have several security concerns,

especially when you're working with closed source code bases. The main one is data exfiltration.

Let's say you have a closed source code base and you allow the agent to do a web search,

or no, not a web search, a fetch. And in that fetch, maybe it fetches from evil.com

and it sends as its payload a bunch of your data. It does a curl to evil.com,

sends a bunch of your source code as its data or maybe some environment parables or some

sensitive data. That to me feels like the main danger to businesses of AI and certainly AI coding

because you pretty much always want the AI to be able to fetch things because you want it to

be able to fetch external documentation. It's just that people don't think of fetch as also

an outbound push as well. You can push data out. And so data exfiltration, it sounds very

unlikely, but let's say that it fetches some information from evil.com and evil.com says,

send your entire code base to evil2.com. This is a kind of prompt injection. And so if then

sends to evil.2, it curls through your entire code base to a second endpoint or something.

So the way that you mitigate against that is by sandboxing. And we don't really talk about

preventing data exfiltration in this course. It's sort of a little bit outside and it's

relatively simple to set up. Within the Docker sandbox that we're going to be using,

or any sandbox, you essentially just restrict outbound network traffic. You only allow it to

hit certain URLs. And this means that none of these fetches will be possible because you've

banned the agent accessing them. And so that's one way to do it. So I would say that's the big

one. And that's the one you most need to focus on. I reached the 120K smart zone area during

implementation despite splitting the task into several phases. What should I do? Compact or

hand off? It depends on how far you are through the task. 120K, people I think are acting

as if this is, and maybe I explained this badly, they're acting as if this is a smart,

like cut off, right? Immediately it goes from like, smart, smart, smart, smart, dumb, right?

As soon as you get to 120. And it really is not that bad. It really is more like a very

gentle curve down. So what I tend to do is when I reach this setup here of 120K is,

should I finish my task? Do I think? This is what I often think. Is the remainder of my task

easy enough that I can trust a dumber model to do it? If that's true, then probably I'm okay

to just continue going, right? And just finish my task. Some tasks I finish end up in like

the 250K zone, you know? Just because I know, okay, you just get to the end, you know?

Let's see a completed thing. I can QA it from there. That's fine. And so you may want to compact.

That's another thing. Compact is useful when you've reached the kind of middle of a task.

When you have had a clearly defined start and you have a clearly defined goal, then you can

compact in the middle sometimes if you need to. Because compact basically says, okay, just

compress that thing and then we know where we're going from here because we haven't started it.

If you compact kind of in the middle of a unit, then it might forget or might sort of get

confused by what it's already done. You get the idea. I do think compact is getting better,

though. I think like that's one thing I've kind of underestimated over the last.

Or rather one thing that I want to watch going forward is if compact gets better and

we can compact in more places and start to like not worry about compacting,

that's I think the dream. And that's where I think most AI coding labs want to push you towards.

Is if compact just becomes essentially lossless, then, you know, we don't really need to worry

about smart zone, dumb zone. We can just put the auto compact buffer lower, give ourselves

just like 180K to work inside and then just compact compact. So that's something to think

about too. How do you envision the future of agentic coding given that its costs seem

to be rising rapidly? I'm a teacher, not a pundit. I have no clue. I don't tend to answer

questions like this because I just don't think about them. I don't, you know, I don't have a

take. I don't watch the market. I don't do anything silly. I like, you know, I just try to

do what I'm doing and make it the best I can. I'm not interested really in the future

agentic coding. If it stays the same, then it will still be extremely useful.

What's the best way to work with poly repos when work spans across them? Yeah,

what I'm doing right now is creating a wrapper directory over work trees of the poly repos.

Yes. So what you describe there, let me kind of explain that to folks. Let's say we've got,

um, so we've got two repos, repo one and repo two. Now let's say that one is a front end

and one is a backend. It doesn't matter which. Now, if you want to add a new feature

to this code base or these code bases, then you will probably need to touch both repositories.

This is true if they're, um, you know, different languages or anything like that.

To add a new user facing feature, you'll need to touch both. Now, how do you do it? What I

recommend doing is not something I've got a ton of experience myself, but seems to make sense

to me, is you add another kind of wrapper repo. Let's call it W. So this is the wrapper.

Wrapper. What am I doing? There we go. So this is the wrapper repo. And in the

wrapper repo, you basically have references to the two other repos, to repo one and repo two.

And you run it in either a parent directory or you can just give it kind of permissions

to access those directories. And in this wrapper repo, you have all the information to

understand the directory. So you have your Claude.md, you have your skills.

This is the repo where you actually run Claude or run your agent. So that is probably how

I would do it. Though I do recommend where you can consolidating these into monorepos,

consolidating them into a single repository that contains both of the code or both of the

code bases. The difficulty with a monorepo is that every time a piece of code changes,

it's going to trigger a deploy in both because usually your deploys are watching the

commits in your repos. And so you just need to be careful with that. So yeah,

that is what I would like. What you're describing is I would say the second best option,

monorepo is the best option. Okay, so we've hit 15 minutes. Let's look at a cool new skill.

I have been learning how to do a Rubik's Cube. And the thing that's been helping me

is a teach skill. So I'm going to say Claude, I have a teach skill available now in my skills

repo. It's still in the in progress, but I think after this, I might make it live.

And teach me Rubik's Cube. Now over the course of the weekend, I've had maybe six or seven

different sessions here, and it's built up a line and designs lessons around it. So

the main thing that it does, and I think this is a really interesting exercise in learning how to

build skills, because I feel really happy with this skill, I think it's doing something very

cool. The first thing it does is it basically asks you, okay, what's your mission? Why do

you want to be able to do this? Or what do you want to be able to learn? And it says

it basically in the first session, it recorded this map wants to be able to take a scramble

three by three Rubik's Cube and solve it unaided at least once. The goal is the

achievement itself, not speed, not theory. So it adds a little bit of extra documentation here.

And this is then the thing that everything else is built around. It then creates these

HTML lessons. So let's open this in file explorer. Let's open it up. And this is

what they look like. Apologies for light mode. And so it's basically going through lesson by

lesson and giving me a just enough little bit or kind of taking my teaching style,

which is focused on, you know, various nerdy teaching stuff, zone of proximal development

stuff, and giving me information. So it gives me little quizzes to so a friend says I feel

the two stickers swap them to fix stickers belong to physical pieces. Yeah, and that's

correct. Teach me the notation, etc. And now I can actually solve a Rubik's Cube. So I'm

not going to do it now because I'm very, very slow. And it's kind of dull. But I'm

going to show you that I can move a piece, this little white piece onto the bottom.

Wait, I'm freaking myself out now.

Oh, it's different when you're on stage, isn't it? There we go. So that white piece is now

on the bottom. So yeah, that's this is generated from that skill. Very, very cool.

I've done this for a couple of things. Now I've only got this, this one on my work computer,

but I've got the others on on a personal laptop. And I've been learning vocal harmonies

for folk music. That's something I'm interested in. And one is and the other one is sorry,

where's my brain? I just I get very excited when I learn something new. And so I'm quite

pleased that I managed to do that. The other one is I've been trying to learn how to teach my

get my son to eat different food. And so it's given me some strategies there.

So this is really, really cool. And we can look at the skill itself and the design.

I'll just show you a couple more here because they do look they just look really nice.

So spin the top and counts the algorithm that it's teaching me. So I now understand

what these letters are. It's just so cool. And we can I think, what would be cool is let's actually

open out the CD into my repose AI directory. Let's make a new directory for learning codebase.

One thing I've not tried yet, and I'd like to try on stream is let's code inside here.

And I'm going to get it to I'll just show you what it looks like when we sort of

start off. So I'll say Claude, I'll say teach me about this repo. So repos cohort for project.

I'm a new starter and I want to get productive on this code base.

I think that if this works, and if I can tune it properly,

then it should be a really amazing way to onboard new people onto a code base.

First, it's checking the state of the teaching workspace and taking a look at the target

code base. While it's doing this, let's actually have a look at the skill. This is inside skills.

And what I'll just show you, I had a long bus journey to go on just to London,

and I needed something to do. And so I wrote this by hand. This is a by hand skill.

And what it's essentially doing is I think of skills as some skills are stateful and some

skills are stateless. And this is a stateful skill. What that means is it has some state

that it saves inside the workspace that it's in. If you think of grill me, grill me doesn't

have any state saved inside the code base. But grill with docs does because it has a context.md

and it has some ADRs in there. So this is stateful. So inside the teaching workspace,

it has a bunch of stuff. So it has a mission.md, the document capturing the reason the user

interest in the topic. We saw that in the Rubik's cube. It has a bunch of reference

documents. These are really cool. They're basically, if we look inside the reference

here, I'll open this up. We've got a glossary inside here and a single card that sort of

condenses all the information, a cheat sheet essentially. So it's not just producing lessons,

it's also producing really high quality reference material. Really good for review

and that kind of stuff. Resources.md, it bases everything it's looking at on high

trust resources. So one of the first things it does is it goes and looks up proper

resources about this. But it's not just basing on parametric knowledge and it saves it inside

a resources.md here. So all of this stuff is stuff that it can then reference later on when

it's building future lessons. It's not only focused on knowledge, but also focused on wisdom

and skills. But I'll get to that in a minute. It also keeps track of what you've learned

inside learning records. So inside the Rubik's cube here, we have these are kind of like

architectural decision records. And so we've got this, like this was the first thing that

it recorded that I learned. I can do the right white cross, shaky, but working.

Can solve the second layer, can make the yellow cross, can align the cross.

And I did my first full solve yesterday. It's super nice. And what else is there?

Then there's just a set of lessons and then a set of notes. And so this also encodes my teaching

philosophy as well, which is something that I take to my courses too. So I think the user

needs knowledge, which is information, skills, actual time practicing the thing, and then wisdom,

which is them applying it in the real world. That's sort of what I've stole that from

someone. But I can't quite remember who tells you how to do the lessons, tells you about the

mission. A really important one is the zone of proximal development, which is absolutely so key.

It's first full solve took about, I don't know from beginning to end, but like,

it took like two days, I think, just because I wanted to get every bit nailed.

Then the zone of proximal development should always feel like they're being challenged

just enough, essentially. So what I love about these skills is that you're able to

not only explain what the user should do and what or rather how the agent should behave,

but explain why, explain the philosophy behind it. So this is definitely one of

the more detailed skills I've ever written, because it's just goes into all of that

information. Let's see what it said about the learning the code base here. Okay, so

okay, it's done a lot. A clean well structured code base. Let me read a representative vertical

slice so I can ground your first lesson in real code from this repo. Very cool.

Let me read one full route, understand the architectural spine.

Cadence is a course platform with a very clean, consistent architecture.

Thank you. Whole code base runs on one repeating pattern, root service database.

Once you see that pattern, you can read any file in the repo. Cool.

Okey dokey. Let's open it for me.

So you can see what it's created here. We can see it's created some starting points.

Very cool. Some lessons. So it's got the spine, architecture map,

mission notes, etc. And it's created our first lesson.

So let's see if this actually sort of wait, can I not zoom in here?

Okay, something something very strange is happening.

Okay, very odd. Well, I'll just open it manually.

Wow, it also does dark mode. That's quite cool.

So cadence is a course platform and it's showing us route service and database.

The rule that makes it work, don't put business logic directly and routes call into services

instead. So cool. The route reacts to the click.

Look at this. I love that it's got syntax highlighting as well.

I don't know how it's done that.

Turns out agents are pretty cool. And there you go. And it gives you an exercise.

And it also emphasizes that I'm your teacher. Ask me anything that was unclear.

Ask me to trace a different feature. You get the idea. It's so freaking cool.

So cool. And so that I think is one thing that you can do with skills is I definitely

see skills as like we are able to a higher level. Engineering right now is currently,

I think, one of the most productive things you can do with AI. AI is much better at

writing code than it is at doing creative writing currently or painting pictures or building

bridges or things like this or even doing video game design or things like this.

It's just much better at writing code than it is at doing almost anything else.

And because we're in a position now, we're the first people to really see AI doing cool

stuff. We're able to be the first to actually have production experience working with AI and

getting it to do interesting stuff. And because we're the first, that means we're

going to develop skills quicker than the rest of the world. And so engineers really,

I think, are in an incredibly privileged position when it comes to adopting AI.

The skills that we develop working with Claude code and working with

codecs and cursor, etc. We can then take into non-engineering domains and take into places

that like we're the earliest AI adopters, so we have the first mover advantage. It's a

very cool place to be. And that's how I feel when I look at the output of this teach skill

is like I would not have been able to do this if I hadn't had experience working with

Claude code before. It's an exciting time. So that's my teach skill. I'll make it live

probably today and make a video about it at some point. It just came too late for the

main stuff, but I'm happy to be able to show you it now. So let's go back to Q&A.

We'll have 15 minutes more Q&A and then we'll finish up.

Suboptimal context gathering strategies by the agent. Broad unfiltered file system suites

that caused a context avalanche. Steering or code-based problem both.

So great question. What do you do when the agent fails to explore? Basically,

we'll look at this actually in week two. In week two, we have a section on research,

which is where if you have a multi-session

kind of plan that needs executing, then if that plan needs a very expensive explore phase

in order to work, then you can cache that explore phase in some research.

It's not only like context gathering inside the repo that's a problem. It's also let's say

you're using a new library that isn't represented in the code base anywhere,

or a library that has a new major version that's come out since the knowledge cut off of the

model. That's an expensive explore phase to do on every single phase in your 12-phase plan,

let's say. So what do you do? You essentially run the explore phase once you cache it in a

local markdown file and you say, right, that's the research that we're then going to depend

on for this plan, which is very useful. You can also do that not only for third-party

libraries, but also for your own code base. If it's a massive code base and you want to run

some hardcore, like a long multi-phase plan on it, you probably need to do some research

there and cache it in a markdown file so that you can ameliorate this issue that you're

having of bad context gathering. Now, you probably also just need to look at your repo too, because

if your agent is failing to find stuff, then that is probably an architecture issue as well

as a steering issue. If you have like a very important file, extremely important,

let's say it's a root manifest or some sort of manifest that touches a bunch of different

files. First of all, you may want to consider just sort of refactoring that away if you can,

or redesigning it so that it's not needed. But if it is needed in almost every change,

or needed to be considered, then you should probably have a context pointer to it from

your root claw.md or have some kind of documentation that points there. And so

it could be a steering issue and it could be a code base problem.

And probably there are solutions to be found in both. And also research is handy.

Great question. You should be designing loops that prompt your agents. What's your thoughts

and approach? I don't understand. I actually don't understand the question. That's sort of what

we're doing, right? Like in week two, we're going to be looking at AFK agents, and we're

essentially going to be building a loop that just re prompts the agent again and again and again.

That sounds so what I'm seeing there is it sounds familiar to me,

and it sounds like something that we're going to be doing as part of the course.

What's my experience with Clawed Opus 4.8? Am I reaching dumb zone more quickly,

getting better results? I don't know. I mean, I'm only one dude. I,

everything I do, I use AI a lot obviously, but I don't consider my own experience to be representative

at all. I would look at bigger organisations who are tracking performance across their employees

and probably tracking pass or success and failure rates. So if you have an org or if your

org is big enough to do that, I would definitely recommend hooking up your coding

agents to some kind of observability tool so that you can see which sessions are good and

which sessions are bad, and then you can make more informed decisions about 4.7 versus 4.8,

or Codex versus Clawed Code, or things like this. So I don't consider that my opinion here

is relevant. Again, I'm a teacher, not a pundit. What I use these skills for small tasks to,

is there a point where grill me becomes overkill for small tasks? Yeah.

Yeah. I mean, if the task is well known, if you know exactly where the change needs to be made,

and you just need AI to, like if you fully understand the task that needs to be done

and don't need to align with the AI, if you can fully describe it out front,

then you don't need grill me. Grill me is essentially for cases where you need to align

with the AI, where you're not sure you share a design concept before you get going. Good question.

Excellent course so far. I can imagine it's challenging to teach people across different

levels. What are you feeling to make an advanced course? I am planning to,

I don't know how much I can announce yet, but I am planning to extend the material upwards.

Yes. In terms of more advanced stuff, definitely. That's where I think the headroom

is. I think there's a bit more space of stuff I can teach kind of below the material,

and, but there's lots more space above it actually.

How would I handle multiple Claude sessions on the same code base?

Git WorkTree, we're going to see Sandcastle and Sandcastle is great at this.

It does all the Git WorkTree stuff for you and it helps you handle that.

Let's see. Coding standards in a new project. What universal standards do you recommend for a new

project? Any good resources to learn what to define in here? Yeah, I mean,

I think probably. It's such a hard question to answer because no coding standard I think is

truly universal. That's the difficult thing about reading some of these books actually, is that

some of these books will give you a hammer and you will try to use that hammer on every

single nail you see. You will try to take the deep modules idea and even though it's a very

good idea, you try to apply it in places where it doesn't make sense. You will try to

make everything into an adapter, make every little thing into a seam and try to just,

you know, it's very easy to take these ideas too far because they're subtle

and they take some time to bed in. Now, that means that every standard that you create

is probably going to be relatively specific to that project or to a certain style of project.

I'm not sure there are universal standards. I think the best you can do is probably

because you personally or your company has a style of creating applications. You probably pick

relatively similar libraries and frameworks and front-end stuff again and you probably do that,

you know, repeat that over several projects. And so you should probably just be building up

a set of coding standards that are universal within your company and maybe those should not

live within the repo. Maybe those should live somewhere else and maybe fetched in, let's say.

So I do think they should live, they should be somewhere that what I hate the idea of is

having everybody in a company building their own set of coding standards. I think that's crazy,

their own set of skills, their own set of like userclaw.md. I think probably that is

just so unhelpful in a company because you're missing out on, like imagine if everybody in a

company, a 100 person company is contributing to the same coding standards, right? You know,

modifying things, editing them, you know, let's say they go through an RFC process,

you're going to end up with an absolutely sick, incredibly comprehensive set of coding

standards which the AI can then apply. So you're making the AI better. If you're just

working on your own set of coding standards, your own skills, your own code.md, then you're

just making yourself better, you know, and I think that's not that suboptimal. I think

you should probably have a set of company coding standards which I'm sure you probably do

but you should be making them really great for AI.

Should I translate the teach skill to Norwegian for the kids or should I let them use

Norwegian as it is, let the agent handle the translation on the fly? I've no idea. I don't

know how, yeah, I don't know. I do know that lots of people all around the world use my coding

skills even though they're written in English and the agent doesn't seem to mind. So I think

it should be okay. Which books do I consider essential? I mentioned a philosophy of software

design and the pragmatic program. Do I have a reading list? I should have a reading list.

Those two are the big ones, definitely. They're relatively cheap, they're easy to pick up,

and they're freaking great. Yeah, so you're right. Those two are my big ones.

Is the cohort sample app a good representation of how I would set up a web app today?

Do I have any go-tos that reflect what I think is best practice? I think so, yeah. I

like React Router. It's pretty great. I'm not too precious about frameworks. I'll happily

use Next. I'll happily use whatever, to be honest. But yeah, I think it's pretty good

representation. I've got a better representation at GitHub MapoCorp course video manager. This

is my work repo. Essentially, it's where I do most of my work. It's the thing that I record

all my videos in. And as you can see, it's also a React Router app. So we've got

Router Dev here. It's more complicated because it's a lot more mature. But yeah,

I'm using Vtest, I'm using Router Dev, I'm using TypeScript, I'm using Drizzle.

This is about what I would do for setting up a production application.

Do I see a Teach and Grill me amalgamation? I don't think so. I think they're different

things. I think you can use them. You don't necessarily need to think about mashing every

skill together into a single skill. You can just have different skills that do different things.

And so Grill me is good at the thing that Grill me is good at. You can probably use Teach

and Grill me within the same session, and it would probably make sense. Grill me about the

thing that I'm learning. So yeah, I think keep skills relatively separate, keep them

good at the one thing that they do. You know, a kind of Linux philosophy.

I noticed from an agent implementing a feature via Grill me to PRD to issues,

Ralph writes unacceptable code. How do I get it to write to my standards?

So one thing you can do, and one thing I haven't really touched on in this course,

and I think I might add an appendix for this week, is add a review stage. I found that

automated review is really, really good for getting it to write to your coding standards

because implementation is quite a costly thing to do in terms of tokens. You

will often during implementation run up against the dumb zone.

And what that means is that the AI is kind of constrained. It's sort of like,

how do I say this? It's like the AI is working at the maximum capacity. If you try to tell an

implementation agent to also apply these coding standards, it sort of intuitively makes sense

because that's what we do as humans. But to AI, it's sort of overloading it in terms of

the task that it needs to do, and it will tend to perform worse. I tend to find just getting

it to write a basic implementation first that passes the tests, and then clearing the context,

showing a new agent the diff, and then getting it to apply the coding standards

is the way to go. Because then it's kind of like you're doing a red-green refactor loop

where you write the failing tests and then get them to pass within the implementation agent,

clear the context, get a review agent to take a look at it, and fix it right there. I've

tends to find that produces much higher quality code. What are my thoughts on cognitive debt or

the gradual loss of understanding of your code base? With AI writing and testing code autonomously,

is it inevitable? This is something that we cover in week two, which is I think that

code-based design can mitigate cognitive debt. If you have a code base that's easy for

AI to understand, it's probably also going to be easy for you to understand.

Hiding implementation inside deep modules is an amazing life hack for just reducing your cognitive

debt. If you have this incredibly well-tested engine inside your code base, like I have a

video editor in my code base. I talk about this in the course, but I'll say it again.

I have a video editor in my code base, which is very complicated. It's got a front-end

component that's very complicated, all the back-end components are really complicated.

It's like live reading a video as it's being produced.

Doing silence detection on it, transcribing it, it's complicated. I've managed to,

with a really nice little code base hack, essentially hide all of that complexity behind

a perfectly testable interface where I can test 100% of the functionality,

let's say, or rather most of the functionality behind that interface.

So when I need to add a new feature, I don't need to look at the code inside.

I just say, AI, okay, just give me this new feature, test against the existing interface,

and then I don't need to see what's in the black box. That's very good for my brain,

because I can just delegate it. If there's a problem, then I'll dive in, but if there's

not a problem and it seems to work and it's QA-ing, fine, then I've not needed to look

inside that black box, and that's great. So just hiding information from yourself,

delegating stuff to the AI is incredibly useful for reducing cognitive debt. I definitely think

it's an important thing. Understand the flow from GRU with docs to PRD to issues,

but how do you pre-organize a raw pile of loose features ideas before picking one to grill?

CB There was a question about this in the Discord earlier, and I think I answered it in an unsatisfactory

way, which is that I tend to find I do this automatically. For most of my career, that's

what I was doing. I was building, I was working in startups, trying to make people's weird

ideas into reality. And so I've got this very long history of being able to take a

raw random pile of features and then picking out the one that's essential to grill on.

What you're often doing in those situations is trying to find the core of the idea,

the actual value proposition, the thing that will most impress the person that you're building,

and not only most impress them, but you need to show them something, show the user something,

show the client something that is going to invite feedback in a rich way and make sure

that you're aligned on what you're building. And so that's often what I'm thinking about,

and I'm often the one steering GRU with docs in order to get it the right way,

or rather get it to build that thing which is going to allow me to give richer feedback.

But I've not encoded that into a skill yet, so you're right to pick it up.

If you're looking for advice on this, then Shape Up is where I learned most of this stuff.

It's really a fantastic book. It's pretty old now and it's totally free. So it's just,

you know, like you just read it online basically. And that's at basecamp.com forward slash Shape Up.

Ryan is an expert on this stuff and he was really influential back in 2020.

I don't know, 2020 was when I read that one, maybe 2019.

Okay, we're at 10.15. My time. Thank you so much for joining. I hope you enjoyed the

little sojourn into Rubik's cubing. I'm just going to solve this one because it's been

annoying me the whole thing. Thank you so much for joining along. I'll be in the discord again,

as usual. And there we go, complete the white side. And I hope you enjoy the week two material.

It's going to be focusing on AFK agents, focusing on code based design, and kind of

putting the whole thing together in terms of flow where you end up with an agent that you

can delegate to, which is very, very exciting. And it's so far we've sort of talked about

getting better code and seeing things come to life with AI. But now we really get to parallelize.

We get to focus on just stepping away from the computer, going away from keyboard while

the agent implements our stuff. Very, very cool. Thanks so much for joining.


### 090-AI Coding for Real Engineers p90 090 Office Hours - Day 6 Afternoon

Hello pals, we are live again. Office hours on day six. I've come like a little bit in

a rush. I've just come back from dropping my son off at my parents, but I'm here and

ready for another barrage of wonderful questions. Excited for week two, good to hear. Greetings

from Uberlandia, Brazil. I never heard of Uberlandia. It's like a German flavor bit of Brazil.

Very glad to have you. Thank you so much for joining along. Let me get properly set up. Let

me get the Slido set up and we're gonna have a bit of fun. The plan for today is to do about

15 minutes of questions to, I'm going to do a little 15 minute demo in the middle as well.

I've got something cool to show you, which will hopefully answer some questions folks have

been having around how you apply this knowledge we've been doing into a team. How is life after

the baby's born? Wonderful. Wonderful. I am about a thousand times more productive than I was

before because your time gets so compressed and you have this physical entity, physical reminder

in your environment all the time about what is important and how important it is. Work becomes

obviously a lot more time compressed, but so much more important because you just, you know,

this little life that you have needs to be cared for. And so yeah, I love it.

So many Dutchies. Yeah. Hello from Ternopil, Ukraine. Glad you're enjoying the course.

Uberlandia meets fertile soil in Latin or land of Uber, probably the land of Uber. So I'm

going to bump my sound up on my mic. You should be able to hear a little bit better now. Apologies

for the big jump. Make sure you guys head onto the Slido and the Slido is where we're going

to be doing the questions. Make sure you vote on questions as well. Cause if you don't vote,

then you're not, we're not going to get the best questions coming in. So make sure

you're looking at people's questions, voting and whatever is the top question I will answer.

Hello from Rye Gate. Had a friend in Rye Gate. I've been to Rye Gate.

Belarus. Great job with everything. Thank you so much. In the morning session,

we talked about my new teach skill and I showed you that I can now look, solve a Rubik's cube.

Look at that. Get it back to where it was. Look at that. It's fun. Very fun.

Middle of nowhere, Argentina's countryside. Wonderful. That sounds great. Okay. I'll let

this Q and A warm up a little bit. Nice. We've got about 13 questions.

Newport beach. Sorry. Adjust volume. Sorry, Raphael. I do. Yes. Two Rubik's cubes,

one sold and one not. I've got a very, I recorded a video just before this where I held

it up and it was unsolved and then in the next frame it was solved. I was very pleased with that.

Okay. Let's get started. I'd love to hear a bit more about how our plans on Anthropic

can be used in the AFK mode. So Anthropic recently made a change or announced a change.

They've not made the change yet to the way that plans work, which is your Anthropic

subscription can only, you get this sort of bonus budget of API credits that can be used

every month for the stuff we do in the course. So the stuff we do in the course,

like the AFK sandcastle stuff, that will now instead of eating out of your main sort of budget,

it will come out of this little extra bonus budget that you get.

And before it seemed that you could do the whole thing, right? You could use your entire

subscription to do AFK work. And that's certainly how I've been using Claude Code so far,

but it seems like in this new mode, you can only use this tiny little bit,

which is a bonus to your subscription. So it's technically a bonus, but it's also a big cut

in the way that you can actually use it. So what I'm going to do is I'm going to switch

from Claude Code to Codex. That's what I'm going to do, because in Codex,

you get a big generous subscription, but you can use it for these AFK use cases. You can use it

in sandcastle, whereas Claude Code, you can a bit, but not very much. So I don't know quite

what the mechanism is for using that tiny little Claude Code budget is. Once I do know,

once it's very clear, then I will ship it into sandcastle and it should just work.

But before that, we won't know.

How do you know when something is good enough? Grilling, splitting it up into issues,

code review cycles, etc. So there's two questions here. If you think about the,

let's open up some diagrams. If you think about the seven phases of development,

which is something I talk about really in the appendix. Where are my seven phases? Here they

are. The seven phases of development are here. Now, it's very possible. I'll just introduce this

doc. We've got grilling, first of all, which is the initial ideation, the grilling grill with

docs. You've then got research too, if you want to do any kind of exploration where you

explore some third party documentation. Essentially any kind of difficult exploration phases

are cached by saving them in a research document before you start implementing.

Then there's prototyping too. So hashing out ideas, hashing out the design before you

eventually create a product requirements document, some kind of spec. You then turn that spec into

issues. You then implement those issues and then you do a QA, maybe going back,

adding more issues, going back through the implementation loop. That's the flow.

Now, the original question was, how do you know when something is good enough?

Now that can mean a few things. What does a good enough PRD look like? A good enough PRD

sort of defines where you're going. And sometimes you won't know if a PRD is good

enough before you've actually implemented it. How do you know when something's good enough

before you get to it? Often I find the secret weapon here is prototyping. Good prototypes

are essential for judging the value of something, judging the value of the approach

that you're taking, whether that's a technical approach or a product approach.

Judging the trade-offs in what you're doing, you can create two contrasting prototypes and

say, does this one feel better? Does this one feel better? Does it feel better if we

use WebSockets? Does it feel better if we use SSE? Does it feel better if we use a

third-party service? You get the idea. So prototypes can do a lot there in answering

questions that you might have because that good enough, what does good enough mean?

Good enough means are the most relevant questions that will define the success of the

thing we're building. Have they been answered? Usually that's when I know something is good

enough. And yeah, I hope that gives you some insight. How do you envision your workflow

being adopted and used in large teams and large codebases? Well, first of all, large team.

Large team sort of feels like a bit of a smell to me. I feel like the right size of

team should be around six to 10, or maybe smaller. Probably the right size of team is

like three, let's say. But you know, three to 10, let's say is a good size of team.

I'm going to talk about this in the demo in the middle, because what we've not really covered

in this course is human review, and I want to add a bit more flavour of that.

Yeah, I'm going to save this question until the middle section.

After an implementation, what's the best way to get a list of manual tests to check the

implementation? I'm fairly sure in the course itself, we talk about a QA plan.

When you do the two issues phase here, at this point, you can actually add an issue to say,

create a QA plan. In the list of issues that you create, or in the plan that you create,

in the end, you're going to have an issue which is assigned to the user to QA the work

that's been done. This means that your review phase just ends up being click through the

thing. That's pretty useful. The best way to do it is to tell the AI to do it as part of

two issues. That's something we cover in the course. How does your workflow modify for a larger

team? We did Scrum, regular shared understanding meetings. Let's talk about that a bit more.

I personally think that all of this stuff leading up to the PRD should absolutely be

collaborative. You should be having collaborative grilling sessions where, let's say, you're all

on a call working with a single AI. There are also things like GitHub's ace, which I'm really

intrigued by. GitHub ace, whereas it here, agentic context engineering? No, that's not it.

GitHub ace, GitHub next, projects. Where is this thing?

Ace, ace, ace, animating the traffic lights in ace. Excuse me.

So where is ace? I'm trying to find ace, but I don't know where it is. Projects,

auto loop, agentic workflows. Essentially, it's an agent coding environment.

Where is this thing?

Collaborative works, but well, okay. I can't find it.

It's called an agentic coding environment and or possibly something, agent collaboration

environment. It's multiple people all collaborating on the same grilling session with an agent

that's hosted in the cloud. So you get a kind of Slack interface for multiple people to chat

with the agent. Now, I can't seem to find it, but I did watch a talk about it, so I

know it exists. Prototyping should also be, you know, you can delegate creating a prototype

to someone, you know. Prototypes can be shared in the team. You can chat about them and those

comment threads or let's say it's a Google meet call, you can take the transcript of that,

feed it to the agent, use it to grill on that and create the PRD. So all of this stuff

before the PRD should definitely be collaborative because you don't want the bus factor. You don't

want just one person knowing all of this stuff, all the design decisions. And often you will hit

stuff in the grilling that you need someone else to solve, right? You need someone to,

a third party to interact with. Once you've figured out the PRD and everyone agrees on it,

then you need to bring it to life. And that can really be the job of a single person,

you know, just going through the issues, implementing them. Because you all know where

you're going, how you get there is really just the concern of one person.

From there you implement it and then you can do review as a group. You know, you will dive in,

human review the code and human review the implementation as well, make sure it's okay.

So yeah, that's how I see sort of collaboration in a general sense.

How are you able to quickly map out the overall workflow, help us to see everything

fits together? Hopefully this gives you a sense of it. This is also in the appendix

at the end or one of the last lessons in the final day.

Interesting how to use the practices we're learning across agents, codecs, co-pilots,

et cetera, some links from .clauda.agents or something else. Yeah, that's how to do it.

This is really most of what I'm teaching here is skills and skills are cross-agent, you know.

Agent agnostic is the right word. How does running Sandcastle on your local machine

compare to running it on GitHub actions? This is exactly what I'm going to talk about

in about two minutes. How can we ensure that Claude is actively handing off work to less

expensive models for sub-agents or even less expensive alternate LLMs? So

I think the answer here is that Claude has the ability to

choose the model that's used when it does exploration pages or does sub-agents.

So I think the way to do this would be in a steering file. So in Claude.md,

you would basically say whenever you use explore, use Haiku or something. There was a phase in

Opus 4.5 maybe where it used Haiku for all its explorations and that was great because

and that was great because Haiku is like two orders of magnitude cheaper. It's incredibly rapid.

It can burn through tokens like very, very quickly read a ton of files, summarize them

and you get a pretty decent output. For some reason, they moved away from that. Maybe that

went out of their system prompt. Maybe they found that it didn't perform that well. I

found it performed great. I loved it and I'm thinking of getting it back,

but that would be how I would do it if I did it. Less expensive alternate LLMs. I'm not sure

if Claude allows you to do sub-agents in different LLMs. I don't think that's a thing.

What are my thoughts on using Claude dynamic workflows as a better implementation of Ralph

loops? I've not tried them. It certainly seems like it's a good idea, right? It seems to

make sense that you could take a product requirements document, take a bunch of issues

which are all designed to be built in parallel and then just say forward slash workflow,

do this for me. That would replace the implement step here. We wouldn't need

if we were using let's say auto mode or something. I don't know. I feel a bit

uncomfortable not sandboxing that. You want your agents to be sandboxed.

For those who don't know Claude workflows is a way of creating a script that allows you to

spawn a bunch of agents to complete a ton of work all in parallel. It's very cool.

That's how I would see it fitting in. I don't know if it's good yet because I've not really

tried it. Should you learn TypeScript? Yes. On a more meta level, the quality of the

agent's output is gated by your understanding of what you're building. In other words,

your ceiling is the agent's ceiling. If you have a deep understanding of a language,

then you're able to steer the agent very effectively to avoid the pitfalls of that language.

If you're not, then you and the agent are going to hit the same pitfalls and

you might not even be aware that the agent is even doing something wrong.

This means that your knowledge is now more valuable than ever because it compounds. It

means that you can take this knowledge and encode it into working practices that you

can feed into these agents that will then never make the same mistakes that they would

make if you didn't have the knowledge. I think that learning anything specific to coding

is way more valuable now because before you were only able to teach yourself and improve

your own output. Now you have this fleet of agents through which everything you learn

goes into them as well. Yes, you should learn TypeScript because agents love TypeScript.

It's way better than JavaScript. Let's take Dave's question later. I'm going to show you

something. The thing I'm going to show you is inside a repository of mine. It's inside

github.com. This is something I've been working with for a little while now. It's

really since I built the course. If we take a look at some of these issues here,

let's take a look at this one. This is a little QA issue that I left on my own repo.

Course Video Manager here is essentially the thing that I'm using to record all my

videos. It's where I organise all my content. It's a huge app that I've built myself.

I reported this here and I said in the actions menu for sections add a move up

and move down button which will reorder the sections. It's essentially a small feature

request. What I did was I added a label to this. This label here added agent implements

and then this triggered something. It triggered github actions, added agent in progress and

removed the label. An agent picked this up and then we can see just here, let me open

that in a new tab, an action ran and opened a PR. Wow, that sounds good. Let me open that up

and see if I can find the original action that kicked this off before I go to the PR.

What issue was this? This was move up and move down. Can I say move up and move down?

Move up. What name?

Like that? No. Workflow, workflow name. It's basically one of these. We could go and find

it but maybe I can just show you a different one. Yeah, agent implements. Let's just show

you this one. What this does is if I open out this implement tab here, let me just delete

my face for a second, is it does a few different things. Firstly, it sets up the job

with Node.js and stuff. It prepares a GitHub action environment. This is running in GitHub.

Then it checks out the main branch. It sets up some dependencies and it runs a file here.

It runs a sandcastle file, implement.ts and basically goes through and implements the issue.

This is sandcastle running inside a GitHub action. It goes and creates some commits.

It commits this run and pushes the branch. Was it right below this one? Of course it was.

It writes a PR title and a description and it creates a PR. The PR that it created was here.

But it's not done, you see. At this point, then, we add the agent review label.

The agent review label is a different action which runs a different agent which then

reviews the PR, does automated checks on it. You can see the review summary. The core feature is

solid, clean, well tested. What I changed was I memoised something, added some edge case tests.

There's a little bit of scope concern, some drive-by deletions. That's funny.

We can see it even added actual comments to the GitHub action here. This is all my stuff.

I've not added any third party stuff here. This is just GitHub actions and sandcastle.

That's all. Very cool. Again, it seems to actually duplicate this comment for some reason.

You can see it removed the agent in progress. I've even got an automated action here for merge

conflict resolution. I can just sort of conflict against main. I can even, if I want to,

add comments on here. All section IDs, blah, blah, blah. I don't like this name.

Like this. I can comment here and then if I add an agent implement label here,

then it will go through, fix all my comments and reply to them.

So yes, I'm adding these labels manually. So sorry, some of them I'm adding manually,

some of them I'm not. The agent review one, this gets added every time an agent

implement finishes. So the flow is like this. You create an issue. You add an agent

implement label to it. That then goes and creates a draft PR with the agent review label.

That fires off another action which goes and reviews it and then marks it ready for review.

It's very, very cool. Let's have a look at the actual code that's driving this because

I think that will make more sense. So it's code, repose AI, or sorry,

repose Matt, course video manager. Now the code for this is all open source so you can just go

and have a look at it. It's pretty simple to look at really. It is just in, if I bump this

up a lot more, it is in .github workflows. You see all of the workflows here. There's a few

different ones. The main one we talked about is agent implement which if the, we can see it's

on issues type labeled. If it's of type agent implement then it goes and does its thing.

So this does not, it skips the entire thing of running Sandcastle locally. You don't need

Docker for this. All you do is you just run these on GitHub actions. It's incredibly cool.

Now we do, there's a sort of some little finicky things here. We need to pass in like

a custom GitHub token for various bits. There's some like nasty code here that I really do need

to sort out. So this is rough right now but it does work extremely consistently.

So again there's some preflight checks here, preflight refusals. We're transitioning the

labels here. We're checking out name, can you see the branch name, blah, blah, blah, blah,

and then, and we run implement.ts. So let's go and see that. Implement.ts

and okay for some reason it's, oh no, there we go. Types went funny for a second.

What we're doing is we're running Sandcastle.run with no sandbox here. So we don't need to run

it with a sandbox. We're logging things directly to standard out and we're grabbing a prompt

file which is just here which is very similar to the Ralph prompt that we've had.

There's no loop here because we're not, we don't need to loop again and again and again.

We're just literally implementing the issue and that's it. This file is what 54 lines long.

The prompt is very similar to what we've had before. There's a bit of sort of red green

refactor stuff in there and then we commit. The review one looks quite similar. It's a

little bit more in here but the prompt for instance just looks like this. We read from

some sort of built-in coding standards which are here and which are fairly long because I

add to these sort of from PRs and stuff and it's pretty great. I am, yes, using Sandcastle

to build Sandcastle. Absolutely. Why would I not dogfood it? So if we look in

map-hocot-forward-slash-sandcastle we can see it's got exactly the same setup where

we've got github workflows. This one is a little less developed. I just copied over some

core stuff. Is it secure without docker container? I'm not so concerned about data exfiltration here

because the only thing that's in the github actions is open source code really.

I suppose it could grab things from the process but I'm not even sure it can.

Maybe it can. I don't know. The worst thing that would happen is it would get a github

token and I only allow it to have a read-only github token within its sort of run.

So it's not too bad in terms of security. You would need to nail it down a bit more if

you wanted to run this with closed source code but for me this is working fine with open

source code. For open source repos I'm pretty sure you get unlimited minutes on github actions.

I've certainly not hit any limits here in terms of the amount of actions that you need to run.

So I think you can just like go crazy with it and of course you don't need to run these on

github actions as well. You can have a different system that picks up the labelling events because

github allows you to send web hooks out to third-party services. So what this does is I

think it makes it clear how flexible the whole strategy I'm using here. You can also, yeah,

self-host runners in github for instance. This means that so much of this stuff can be done afk

now. I want to show you a couple of the other workflows because they're really nice.

Update branch is so nice. How many times have you fixed merge conflicts in your career?

How many times? I might have done it you know 100 to 1000 times. This one it just makes them a

thing of the past because what you do is you take a PR that's got an out of date with its

target and you just add a label to it and what that label does is it just goes through

this setup. So it's just, let's see, prepping the branch. It goes and attempts to do a

rebase and does it rebase or does it merge? I can't remember but it does one of those

and if it fails then it gets an agent to fix it passing all the information that it might need

to understand the reason for the changes. It's great. I've had some people tell me this is

quite similar to symphony and I did investigate how similar it is to symphony. This is way more

way more complicated than symphony actually. Symphony if you don't know is symphony.

It's a bittersweet symphony this life. It's over here. It turns project works into isolated

autonomous implementation runs which sounds like what I'm doing. Symphony really has only one

move. It's do this thing. So you create a ticket in linear let's say and that then gets

picked up by symphony and it does that thing in your repo which is very flexible

but also just not very opinionated. With this it's more like we have a set of workflows which

we can just reusably do again and again and again. So implement PR. I've even got it working

with PRDs. So what you can do is you can create a PRD and you can, oh god I could

talk about this for hours, you create a PRD. You can give it the two issues label which

will automatically just attempt to create issues for it. These are created as subissues underneath

the PRD and then you can just press agent implement and it will just iterate over the

issues like a Ralph loop and complete them and you end up with a PR that then gets reviewed.

One of the coolest ones is architecture review. This is not on a label it's on a cron job

and this cron job, you guys are going to get nuts for this, it's so good.

This cron job creates at 9am every weekday an issue suggesting how you might improve the

architecture of the application. Look at this, hopefully it's got a mermaid down here.

So here we go. Before each route re-implements the video posting shell, yes that's true actually,

I've not seen this one before. So each one has like a post page, social post panel. Instead

it's saying there should be a shared layout, roots only, unique page plus loader. I sort of

understand that. But essentially I can take this, I can just label it. So let's just do it

now for fun, why not. Let's do agent to issues. We should see that this immediately gets picked

up and it's going to immediately start creating issues based on this PRD. This is kind of like

a PRD what's been created here. So you can start to see how much this can automate.

Like oh there you go, it's gone to in progress now so it's being picked up by an action

and it will do something. Thoughts on local PRD versus hosted as a GitHub issue,

you've got to put PRDs somewhere that multiple people can review them. I think local

stuff is a bad idea in general, I just needed to start with that in the course because I

wanted to sort of give you an easy starting place. But GitHub issues or JIRA tickets or

linear issues, that's the place for them. So if you're interested in this stuff,

then you should definitely check out inside GitHub workflows inside my course video manager

repo. These are going to be sticking around here and I will definitely make more content

about these. This Cronjob uses the skill to run a version of improved code-based architecture.

It's not actually running the skill, I just took a prompt from it or turned the skill

into a prompt and it runs that prompt. But yeah, it's the same core idea. So

right, that was the demo and that's something I'm so excited about.

I freaking love it. It's the fastest I've felt in terms of being able to get stuff done.

One thing to mention is if we look at the seven phases, is this is really just focused

on implement here, right? And a little bit of issues. All of the grill research prototype

and often the review stuff as well is still all human in the loop. I'm really just focused

on implementing here. I still do grill and research and all of this stuff with a repo in front of me.

Does it display in a GitHub project Kanban? It probably could, yeah.

Yeah, certainly could, right? Because that's just, is that milestones? I think that's

milestones. And there's definitely a GitHub API to modify milestones. Hang on, I just need to

fix something, sorry. Oh no.

I've got a thing that turns it off at 5pm for some reason.

Does this mean we can use your new teach skill and paste the URL to your course

video manager so it answers all questions? Yes, absolutely. Yeah, you should do that.

That sounds great. Okay. What are, would you say, the optimal tests that need to be

run before shipping? I think this is the wrong mindset. I think that every team should be in

a posture of continuous shipping. If you feel that, oh, today's the day we ship, you know,

like today's the day we get our work out there. Let's all make sure it's all good.

Let's get it absolutely nailed. Then that release is probably not going to go well.

You should be releasing every five minutes or something. Every time your CI runs, it should

be a new release. And that takes the pressure off those big releases, because if you have those

big releases, what you're doing is you're often just sending lots of code out into the world

at once. And if you do that, some of that code is going to be bad. Whereas if you have

a trickle of code coming out every day, or every, you know, every hour, then you're going

to be getting feedback on that code immediately. And it means that bugs are a lot easier to

fix because you can see the exact diff that caused it. If you have to roll back an entire

release of unrelated features that are not even related to the bug fix, you're in a really bad

spot. So the optimal tests to run before shipping are the tests that you run every single day,

are your continuous integration tests, are the ones that you run on every change. Your

tests need to be high quality. There's something else here though, which is how much QA should

you do on a feature? And I think you, the sort of QA phase has not really changed, like pre-AI

and post-AI. You still need to be pulling the thing down, pulling the GitHub PR down locally,

testing it to within an inch of its life, giving detailed feedback. And yeah, that's what

you need to be doing. So I don't know, I don't think there's a set of optimal tests you should

do. You need to be releasing every minute or every hour and that will help. Best way to

extract implicit coding standards in existing projects. I find telling the agent to do so

creates quite some noise similar to init. Okay. So your team probably has some kind of review

cycle and in that review cycle, it may be accessible via API. If you think about it,

every GitHub comments that you leave can be retrieved via an API call. So something I've

been thinking about recently is taking all of the comments that I've left on PRs and turning

them into some kind of data set. That data set will grow over time naturally as I leave

comments. And every so often I can use that, feed that into an agent to update my coding

standards based on things that I've actually given feedback on. So that's the way to do it,

is to take the data set that you already have, which is your review comments and

bam, you're good to go. I find, yeah, to touch on that more, I think what you might

be saying is like, and I think this is a mistake that lots of people fall into, is that

it's very tempting to tell an agent, look at my code base and create some coding standards based

on my code base. Guess what? That is information the agent can already see in the code base,

can already see it. So why would you need a secondary document when the code already

explains itself? You don't need coding standards that represent what you already have in the

code because the code, it's self-describing. So yeah, I don't know. I think as long as you're

really carefully reading that stuff and cutting out anything that feels extraneous,

then you will get good results that way. But yeah, hopefully I've answered your question.

Is the AI SDK still relevant to learn? Absolutely. There's still,

I still do a lot of pulling out features of Claude code and customizing them to my own liking.

So for instance, I have a whole AI writing setup, which is totally custom to me and it's

within my course video manager app. So that is all driven by the AI SDK. And I'm done,

I'm going to move off the AI SDK because similar to Sandcastle, it just allows you to use any AI

vendor that you want, any model provider that you want. So yeah, it's fantastic. It's still

an absolutely brilliant tool. And it's, however, it's more useful in building AI powered apps,

than you being an AI powered developer. So I don't mention it in this course,

because it's not really relevant. Not really relevant to AI coding. You get the idea.

GrilleMe aligns me and the agent on the what to build. When I run that, I tend to end up with

an architecture I don't like. Second grill on architecture. Yeah, I think so. I think it's

very, what's the right way to say this? I think that you should be driving the,

the, grill me is a tiny skill, right? It's not opinionated at all. It really just lets you do

whatever you want to do. And so you as a developer need to be having both tracks in mind.

You need to be thinking about the user experience, right? The end user. But you also need to be

thinking about the agent experience working in this code base. That's definitely a challenge

that a lot of people have when they start with a greenfield code base, because neither

exists yet. Like the agent hasn't done anything in the code base. It's an empty state.

The user can't see anything because it's an empty app, right? And so you need to build both at the

same time. So I think you would have both in the same grilling session. You just need to be

mindful of both at the same time. Opus 4.8 for exercises consumes about 2x more tokens,

comparing your lectures when it Opus 4.6 was used. Do you have similar observations? How

do I handle it? A lot depends on the effort level. You want to be really careful with the

effort level. I used Opus 4.6 medium, I think, which is pretty low effort. Now these days,

Opus 4.8 defaults to extra high effort, which is really spendy. I'm still on medium.

So yeah, I would just watch that. You've said in public videos that for coding,

we should use grill with docs, but we've been using grill me during the course. Why is

that? There's an appendix where I talk about grill with docs, basically. It's sort of,

I debated putting grill with docs earlier in the course, but it didn't quite fit anywhere.

And so I've decided just to put it in as an appendix because it really is just a small

addition onto grill me. And it doesn't really affect much else in the skills. It just sort

of benefits everything. So it is in the course. It's just not quite as early as you might

expect. Let's see, can we not see the course content in cohort OO3, the Ralph loop part?

It seems not in the cohort OO4. Yeah, it's been replaced with sandcastle. Sandcastle is by far

the better solution. And I mean, if you want to see it, I could probably make that happen,

but I don't know why you would because it doesn't work as well.

A new skill to start a new project makes sense. There's an appendix I've added on

Greenfield projects on how you should be thinking about Greenfield projects. And

I don't think you need a new skill. What you do need to do is just use the existing skills in a

different way. Again, thinking about kind of touching what I touched on before, the UX and

the AX at the same time, the agent experience too. So you thinking about both of those

things during grilling, thinking about both those things in the PRD.

How do I stay up to date with so many new AI developments? How should I start if I want to

become a software engineer? I would be really intrigued by how you get on with my teach skill,

which is you can watch a 15 minute demo on in the previous office hours, the one I did this

morning. So yeah, I'd love to know how you get on with it. And feel free to ask for support

in the Discord. I think those two things are different. Staying up to date with AI is I

think kind of optional. Like you don't need to stay that up to date. I think most of the

working practices have kind of settled down since around December last year. We've all decided,

okay, we found the right form factor for these agents. It's always a text box with some,

you know, that we're running in some directory that has the ability to write and edit files

and run bash scripts. That's kind of what we're all doing now. And the stuff on top

is just kind of layered on top and doesn't change that much. So people are getting better at it

and sort of starting to develop best practices around it. But those things are moving quite

slowly and certainly more slowly than, you know, Opus 4.7 to 4.8. What I find is there's

a ton of noise out there. So much noise. The best thing you can do is just to be exploring

every day, to be trying to optimise what you're doing and you will find new insights,

which will put you ahead of most people in the field. So yeah, hopefully that answers your question.

Do I always aim to have tests in all my implementations using TDD as default?

If not, what is your approach? Yes, in the feedback loops section, I hope I explain

why feedback loops are so important. For certainly backend code, because it's quite easy to write

good tests for it, I have almost everything tested. I make sure I test at a sort of pre-agreed

seam. So I'm not sort of writing shit tests that just crap tests that just kind of like,

um, just test like tiny units. So yeah, I always need to have tests for certainly backend code.

For front-end code, it's harder to write tests for because front-end has a very visual component

to it. And if you get the positioning of something wrong, then it can have a ripple

effect and affect loads of other stuff on the screen. So having visual testing for

UI is very tricky. I've not quite figured that out yet. I do have some ideas, but

they don't always involve unit tests. So, um, yes, I suppose is the answer, certainly for

backend code. Is Sandcastle not ready for the codec subscription yet? Should we expect it soon

because you plan to make the jump? It is ready. It's just there's a documentation issue where

I've not documented how to do it. You essentially just copy over or bind mount the .codex folder

into the sandbox and then it reads from the auth.json file in there. I just haven't found

the time to document it yet. I should get an agent to do it for me.

Do I have a list of recommended books to read? Um, no, but I should. At the top two are the

Pragmatic Programmer and Philosophy of Software Design. I almost always have to run a refactor

loop to simplify the architecture as the implementation run tends to go too far with

the OOD abstraction Java issue. Yeah, I don't know. I don't do a ton of Java,

but this sounds right to me. This sounds, I think that implementation plus review is

so much better than implementation. I cannot like it. And it's very easy to hook this up

with Sandcastle as well. You just write a slightly different prompt to say, you know,

just radically simplify the code and you get it to run on each commit. You just commit

directly to the branch and you end up with much, much better code.

Based on the new subscription limits for AFK, are you saying that I will mix Claw Code and

Codex? Probably, yes. It's awkward because then you're kind of mixing two rate limits,

you know, which is fine, I suppose. But I do want to optimize that a little bit. I

don't want to be too token burning. I don't want to max out on both subscriptions. I will probably

bump Claw Code down, I imagine, since Codex is what I use for or AFK is what I use from

most things now. All right, let's do one more question. Has code review changed in the AI era?

Is it still fundamentally the same? What are we reviewing for with mostly AI generated code?

So let's finish there by talking about AX, DX and UX. I think I've got this already in

a thing, but maybe just create another one. So AX, DX and UX. When we think about software

quality, we're basically trying to think about these three groups. We've got the

user experience, which is, I suppose, the most important one, right? If we don't have a good

user experience, then users are not going to use our product. They're going to run away.

We're not going to have happy people and we'll probably get fired. DX, developer experience

was for a long time the most important thing you could have at a company other than UX. If

your developers are happy, if the developers are able to make changes quickly, if they're happy

with the tools they're using, if they like the code they're writing, then you're going to have

a good time. You're going to ship more code and have high velocity. And before agents came

along, these were the two important things that you were reviewing for when you did any kind

of review. We need to make sure it works and we need to make sure that future maintainers

won't try to tear their hair out, if that's possible. AX, we're now reviewing on a third

axis, which is developer experience is a little less important. Still important, but a little

less important. The thing that is really important, though, is AX. Probably, this is

now sort of swapped into this kind of tier list. AX being agent experience. And agent

experience is critical because if your agents are having a bad time inside your code base,

if they're not able to find the files that they need to edit, if they get concepts wrong

about the code base, or if the automated tests are low quality, giving them bad

feedback, then they're going to produce crap code. So AX, very, very important. And those

are the three axes that you're really reviewing for whenever you do any kind of review.

Okay. Nice work, folks. And yeah, I won't answer that question because we're over time.

Thank you so much. Always, always wonderful questions to answer. Really fun. I hope you

enjoyed the kind of middle section where we did a little demo. I really like doing those.

I might do another one of those as we go. Make sure you do head to that repo and

use your clanker, point it at it, ask any questions on what you can learn,

what you can bring to it. Yeah, let me know. Overall, thank you so much for joining along,

and I hope you enjoy week two. This is the end of my day. So I'm going to go and

make some dinner. I've got a little folk night that I'm going to take my guitar to and do some

singing. Loop engineering, I've never heard of that. God, everyone's always claiming

a new version of engineering. It's just rubbish, isn't it? Just hype. All right, pals,

I'll see you in the Discord and I will see you all the way up until the final office

hours on Friday. So the same time as this. See you.


### 091-AI Coding for Real Engineers p91 091 Final Office Hours - Morning

Pals, morning, morning, morning.

We're here a couple of minutes early.

Just gonna get warmed up.

Going to make sure everyone's got access to the Slido.

And, well, I guess, I mean, for many of you,

this will be goodbye, this session.

This will be the last session that you'll attend.

You will no longer see my face or, I mean,

I'll still be around in the Discord, of course,

but this will be officially our video goodbye.

So, in that case, goodbye.

Good morning.

Hello, hello, hello.

I'm expecting usually the way these go

is that we end up with fewer people

attending each office hour,

so this should be a nice, intimate session.

I know it's sad, isn't it?

Isn't it sad?

It's been great to see you guys

work through the material, it really has.

Rajkot India, what's up?

Morning, Adrian.

Encouraged following your way of working?

Glad to hear it.

Well, we've got a few questions pouring in already,

so make sure you not only ask your questions,

but vote on other people's questions,

because these little votes in the top right,

I'm sorting by most popular here, not the newest,

so whatever is the top, I will answer,

and we'll start this in a second.

Morning from Denmark.

Oh, turn on the mic.

Yes, you're right, I'm on recording volume, aren't I?

Let me bump this up.

Okay, we are now at proper volume.

What am I gonna release in future cohort?

Any upcoming plans?

I do have some plans.

I think I will probably take some of the material

in the cohort and turn it into a small course,

which will be a relatively cheap course,

and I think, yeah, I think that's what I'm thinking,

sort of an intro, sorry.

I do this every stream.

This is why I do this little setup thing,

so the people who come in at half past

don't get this weird kind of janky in volume.

So again, make sure you're voting, folks.

Make sure you're voting.

It's so much more relaxing watching all the training

material, knowing that Fable 5 is just running

through the backlog in the background, nice.

Oh, will this cohort get future updates?

Sadly not.

This is the idea of a cohort.

You pay for the material as it is right now.

I gave cohort three a free update to cohort four

because it was just a small tweak, really,

in the material, just dropping in,

dropping Docker sandbox and pulling in Sandcastle, basically.

Good morning, pals.

Good morning, pals.

Space changes so quickly.

I have to make sure you stay up to date.

Yeah!

I mean, it does change quickly.

I'm changing my approaches like a lot, I suppose,

and I have new ideas cooking all the time.

I'm sort of not...

I don't know, maybe I feel like everyone's talking

about MDD in the chat now, like Mat Driven Development,

but I should name my approach, really,

because then at least I would have...

Like, having a name for the approach

and having like a spec for the approach

might be really useful to sort of not only teach people,

but also show changes to it over time,

because I am planning to make changes to it,

just not in big ways,

most because like the core loop

of essentially grilling PRD and to issues

is not gonna be...

That's not gonna change, right?

Because you need a way of specing out work

that's gonna last over multiple sessions,

and I really like grilling.

It's like an approach for fleshing out...

Like, conversation is fantastic for figuring out stuff,

so that's not gonna change.

I think some names might change.

I think that PRD is not the right word.

I might change it to spec instead,

and it's not gonna turn into Spectrum Development,

because Spectrum Development is fundamentally different,

which we'll talk about in a sec.

PPP, Pocock's Pragmatic Prompting.

Ha ha.

Yeah, I don't know.

I mean, like, I feel like everything's got a name

these days, you know?

H-I-L-D-D,

K-A-M-D-D.

Environmental impact of using AI as we do.

Yeah, I mean, the world has an energy problem, right?

It has an energy problem.

That's above my pay grade to fix and know how to fix.

But essentially, if we can produce more energy,

then in a clean way,

then we'll be able to support all this new AI stuff.

Yeah, I'm thinking instead of PRD and issues,

I think it should be spec and tickets.

Spec and tickets, because that just maps onto,

like, a few more things.

It's not quite so opinionated.

PRD is its own specific thing,

whereas spec is more general,

and issues is kind of GitHub specific,

whereas tickets is more, you know, anything's a ticket.

Human in the Loop DD.

Pokeable skills.

Yes, it is easier.

I mean, it's good to have a shorthand.

I basically need to tokenize the approach into just one token

and say this is the name of the approach that I take.

I don't know, maybe we can figure that out.

MDD is fine for now as a shorthand.

But it's ridiculous.

Tasks.

I didn't want it to be tasked

because I didn't want it to interact

with Claude's own concept of tasks.

So Claude has its own inbuilt idea of tasks,

whereas a ticket manager is kind of clear

to everyone what that means.

Graphify.

I've not used Graphify yet.

All right, let's go to the Slido.

So the plan is we're gonna do the Slido

for about 15 minutes.

I'm then gonna demo you something for 15 minutes,

and then we'll go back to the Slido again.

I'm excited by today's demo.

I would like, if we can,

I mean, you guys can talk about anything,

ask Q&A about anything,

but what I'm gonna demo for you today

is something about skills.

I'm debating making a change in my skills,

which would change how they operate

without actually changing how you use them.

I'll explain more what I mean in a minute.

I found myself wanting the abilities of a skill

without necessarily wanting to invoke the command

inside the skill.

I'll explain.

All right, so let's do it.

So if we can direct our questions towards skills,

I think that would be an interesting way to frame this.

So this can be the skills office hours.

Okay.

How would you explain the differences

between MDD, Mat Driven Development,

the approach I'm teaching in this course,

and other AI workflows like superpowers or STD?

So superpowers, what I tend to notice

is that superpowers,

let's take a look at it,

because it's really interesting

the way that they've designed it.

It's at Obra, superpowers,

it's at, I mean, 225K stars.

It's maybe the fifth or sixth

most starred project of all time.

This is an incredibly influential set of skills.

What you can notice here is that

the skills themselves aren't written like commands.

They're written like abilities.

So for instance, here we've got a writing plans skill

that the agent is supposed to invoke,

use whenever you have a spec or requirements

for multi-step tasks before touching code, right?

So it's essentially an ability here.

Whereas my skills are supposed to be more like commands,

or procedures, let's say, where the user invokes them.

So superpowers is designed to empower the agent

to make smarter decisions and kind of respond to you

based on what it thinks you need to do.

So for instance,

brainstorming is its own version of grill me.

It's sort of got a,

you must use this before any creative work,

creating features, building components,

adding functionality, modifying behavior.

So essentially there's a lot of work

or a lot of reliance on these little descriptions

in order for them to be pulled in to the agent.

Now, I think it's more...

What superpowers does is it means that it feels like

you have superpowers when it all clicks and when it works.

And the agent is sort of like just,

you say to the agent, this is what I want to do.

And the agent goes,

yes, I have a skill for that.

So let's get started.

But what you're doing is you're imposing

a lot of non-determinism, a lot of probabilism.

It's not always gonna pick up the skill.

That's what I'm saying.

Whereas if you have them like I do,

like in procedures where you say grill me, do this,

then it's always guaranteed to pick up the skill.

And you have a little bit more thinking to do

as the user because you have to think

about your own process and you have to sort of walk

through this fairly rigid process, but you are in control.

You have the steering wheel.

Whereas in superpowers, the agent has the steering wheel.

That's the big difference.

And that's what I find people noticing

as they use my skills instead is,

wow, this imposes a bit more work on me.

Do I like it?

Most people do like it and I really like it.

So that is the difference.

SDD, SDD is a whole different thing.

Like I don't know how I can describe SDD in a short way.

This is spectrum and development.

Spectrum and development, there's lots of flavours of it.

And the flavours are very, very different.

This is a problem with a name actually

with naming anything is that you name something

and then that name, the container,

like the things that it contains just gets bigger

and bigger and bigger and bigger.

So spectrum development actually contains multiple

different approaches.

You can have approaches that totally ignore the code

that just treat the spec as the source of truth.

If you have a bug in your application,

you go back, rewrite the spec,

and then you just recompile and then it takes the diff

and basically computes what needs to be done from there.

So the spec is the source of truth.

So almost at any time, you can just recompile the app

from the spec, which doesn't work.

But anyway, there's other approaches where the spec

is just one part of the process

where you use a spec as part of something else,

but you still really care about the code.

Yeah, so I don't know if I can answer

like how good my approach is versus spectrum development

because spectrum development has

so many different approaches within it.

All right, next question.

What do you do when the skill goes off course?

Example, improve code base architecture,

did implementation, no interfaces, no GitHub issue.

It's hard to balance improving AI tooling

and doing actual work, yes.

On the second one,

it's hard to balance improving AI tooling.

There's always been a tension in programming

between improving the DX and shipping the feature, right?

Always, whenever you're shipping something,

you're thinking, oh, I wish this was better.

I wish that piece of code was better.

I wish the tests ran a bit faster.

I wish that the CI wasn't so flaky,

and otherwise, the PMs are thinking,

God, I wish these guys would go and do some actual work

instead of improving their working conditions.

So yeah, it's always been hard balancing plumbing

versus fixing.

So if you're experiencing issues like this,

then you should probably first of all report them to me.

I need to know about them.

And then you should check out anything else that might be...

The issue here is that if you think about

the probability distribution of things

you're gonna get back from the agent,

then improved code-based architecture,

doing weird stuff, jumping straight into implementation,

is probably somewhere on that bell curve, right,

of weird responses from really good over here

to really, really, really bad over here.

It will be somewhere on there,

and some random Tuesday,

even if you're using Fable, it will do something strange.

That's just how models work.

That's how non-determinism works.

So yeah, I mean, what you need to do is just,

if it keeps happening consistently,

look at something in your setup

that might be imposing constraints on the model.

So I would tend to look at the harness

that you have the model inside.

So I would look at your agents.md file.

I would look at your skills.

I would make sure that I'm not overloading it

with information, pushing too much stuff to the agent,

that it sort of does weird things.

You might find there's something in your cloud.md

that's saying, always, when you do implementation, do X.

And the model interprets that as,

oh, I probably need to do implementation

in every single session.

So it's hard.

It's hard to balance improving AI tooling

and do an actual work.

I find that improving AI tooling

generally gives you extremely good results,

so it's always worth investing in.

In day four, you said the red-green refactor

is mainly for the backend.

What's the recommended feedback loop for the frontend?

Great question.

It's really hard.

Testing frontend code has always been hard,

mainly because there are two components

with frontend code, which is,

one, does it work?

Does clicking the button take me to the URL?

Does clicking the button open the modal?

Does this timer add up correctly as it goes through?

Are these dates formatted correctly?

Number two, does it look good?

And there's a whole suite of kind of frontend testing tools

that will test number one,

but cannot touch number two.

They will test whether it works,

but they can't test whether it looks good.

And often, actually, those tests,

you can run frontend tests inside Vtest.

You can use a library, let's say JS DOM, for instance,

to emulate the browser inside JavaScript

and just basically click around the application,

just literally physically going inside a virtual environment.

The tricky thing is those tests are really hard to debug.

I've spent many, many hours, pre-AI, in my career,

debugging those tests and figuring out what's going wrong,

because there's no browser to look at.

You can't physically see what's going wrong.

And then, if you do put those tests inside the browser,

the browser is an incredibly expensive thing to run,

so your tests run really slow and they often become very flaky.

So it's hard. It's just very hard.

One feedback loop I think would be useful

is essentially giving the agent browser access while it's developing.

So it has access to your dev server.

So using agent browser or using Playwright, MCP,

or using any of those tools that do this.

This means the agent is able to click around,

and it can do one.

So it can figure out if it works for the most part.

It can offer some feedback on how it looks,

because mostly it's going to be clicking around,

still a virtual representation that happens to be driving the real DOM.

So it's clicking through the, what they call it,

Accessibility AST or something.

So essentially it can see all the buttons,

but it sees them in text.

And then, if it wants to, it can take a screenshot of the front end

and sort of feed that in as an image and make observations.

So it's basically a hard problem.

You can help by doing these things.

You can do a little bit of front-end testing.

You can do a little bit of browser use

to get it to walk around and check stuff.

But yeah, it's hard.

The AFK agent says,

seems to be optimized for monorepos.

How best to adapt it for a poly repo?

Yeah.

So this is a sort of weakness in Sandcastle,

which is you can only add one repo to the sandbox at any one time.

That's difficult.

Making changes in a poly repo is really hard.

There is a proposal out there to add multi-repo support,

which is you would essentially mount a bunch of repositories into the sandbox

and then you would take out all the commits from each

and pull them back to their original repos,

which seems possible, but also fraught with difficulty.

How do you manage the state in those individual repos?

What happens if there's unstaged changes in one of them?

It's just quite tricky.

So, I mean, I always recommend monorepos.

I think monorepos are great.

They come with a tooling cost.

They come with an overhead cost.

But the gain that you get is you don't have to worry about this stuff anymore.

It's just in one place.

There's a single commit that just can touch multiple places.

The history is really easy to rewind.

It's a single source of truth for your company stuff.

Yeah, I dislike poly repos a lot.

And let's see, how do I answer this question?

Well, I don't know how best to adapt it to a poly repo.

Maybe you should open an issue or join in the original issue

and we can figure out some hacky way to do it

while I'm sort of building this

or thinking about building the poly repo setup.

Token cost is steadily increasing.

How best to minimize token usage?

So I get asked this a lot these days.

My response is that I think you should be optimizing for quality,

not optimizing for cost right now.

If you're optimizing for cost, then your quality is going to go down.

And if you imagine there's a sort of tipping point with AI,

which is that, let's say quality sort of goes up like this,

and at some point there's a line.

As the quality is bad, you're going to be spending time fixing the agent's issues.

Right?

And if we imagine that to the line, as it gets better quality, better quality,

you're going to spend less time, less time fixing the agent's problems

until you're not fixing agent's problems.

You're just merging work.

And that, at that point there, with sort of AI is almost self-sufficient, right?

You just do a little bit of review and then you're good to go.

The issue is that as you optimize token cost, you're going to reduce quality.

Right? That's the game you're playing.

So you get up to quality here, you realize, oh, we're spending a lot.

Let's just go down a little bit.

And suddenly you start getting into the issue where you're having to review code again

and review the AI's work and check it.

So I think you should be doing everything you can to stay above that line,

because sure, tokens are, they cost money, but also developers cost money.

And if you can take hours that were being done by developers and turn them into tokens,

then you've had a massive reduction in cost.

Right? That's just economics.

So I think minimizing tokens is the wrong game to be playing.

I think I'd need to understand what it is exactly that you're missing,

because things like preventing data exfiltration,

you can just encode that into the sandbox itself via IP tables

or any way that you would make a Linux box secure usually,

you can do that in a Docker sandbox.

Or sorry, in a Docker container.

So you can just do it.

So yes, I think it can be reconciled.

Let me know in Discord if you have any specific questions.

Let's do one more.

I tried the AFK agent on a backlog.

But why is this better than a cloud agent?

Cloud agents seem even cleaner with PR creation.

Yeah.

So I've sort of moved to, I still do a little bit of stuff locally,

but yeah, you can totally just change your setup so that it creates PRs instead.

So yesterday, a couple of folks, let me look at some merged PRs,

a couple of folks had some issues that they spotted,

which is for instance, the codec's default model was too small.

I explored their issue with an AFK agent.

I implemented it with an AFK agent,

and then I reviewed it with an AFK agent.

And this is basically all code that was produced by AI on GitHub actions.

So I've talked about this in the previous office hours,

which you can go and check.

Yeah, so I think cloud agents are fantastic.

And I use Sandcastle to do this basically.

So Sandcastle is working within that GitHub action with no sandbox inside it

because the GitHub action is already sandboxed.

And yeah, it does great.

So Sandcastle is really just a tool for running an agent in a sandbox.

And you can do anything you want with that.

You can do this PR workflow.

You can commit to main as the sort of main setup we have here does.

And yeah, so Sandcastle is just a tool really.

Alrighty.

So let me show you what I've been thinking about.

And to do this, let's open up a TL Draw.

The thing that I've been thinking about is that skills really have two different types.

You have procedure skills, and then you have ability skills.

Now, what do I mean by this?

So let's say you have a procedure skill.

Procedure is essentially meant to be kicked off by a human.

It does a series of steps or it makes the agent behave in a certain way.

And then you have abilities.

So abilities are things the agent now knows how to do as a result of the skill.

So for instance, a procedure might be improve code base architecture.

And let me just sort of zoom this like this.

So that's an example of a procedure.

What improved code base architecture does is it looks at your repo,

looks for improvement opportunities, and presents them to you,

and creates a GitHub issue with the one that you want.

That is a procedure.

But inside there, it also knows how to understand deep modules.

So it understands what a good code base looks like.

So it sort of has inside it a code base design skill,

or rather the ability to produce a good code base.

And what I found was I would often want the ability, but not the procedure.

So I sometimes wanted to take the abilities inside improved code base architecture

and just say, just find me opportunities in this little section of code

to improve the design here.

Or how does this change match up with what we know to be good code base design?

You see what I mean?

So I was thinking then that this means I can potentially split my skills

and have some skills that are abilities and some skills that are procedures.

And the procedures would then reference the abilities.

So inside improved code base architecture, you would say, here's the procedure,

and reference this skill if you want to know about good code base design.

So this is what I've been doing with my skills.

This is not on the main branch. This is on a PR.

And you can check out my...actually let's go to the skills.

GitHub, my Perkoz skills.

There is a single PR open.

And this is the PR.

Split skills into commands versus skills.

And you can check this out too.

I've just updated it to main, so it should be a nice diff.

So let's have a look inside the skills.

We've still got the same folders, but now we have engineering.

We have a few different things inside here.

We have code base design, which is...

This is the theory that I was literally just talking about.

That description is way too long. I need to cut that down.

But we have diagnosing bugs.

And let's have a look at grill with docs as an example.

So grill with docs under this new model would look like this.

Run a grilling session using the domain modeling skill.

Interesting.

So that means we would have domain modeling.

This is basically taking the domain modeling stuff from grill with docs.

Again, this description is way too long.

And sticking it in its own skill, its own ability,

because I wanted often to do domain modeling,

but I didn't want to necessarily put it inside a context.md.

And then we've got...I think grilling is inside productivity here.

Yes, here it is.

There we go. And this is essentially the grill me skill.

So grilling is actually used in a bunch of places.

Grilling was used in...

This means that improved code base architecture

can reference the grilling skill.

Run the code base design skill for the architecture vocabulary.

That's what I'm talking about.

Does it do grilling? Yeah, here we go.

Once the user picks a candidate, run the grilling skill

to walk the design tree with them, constraints, dependencies, etc.

Pretty neat. Pretty neat.

And I've been running this for a while, and it works super well.

So this means you get a little bit of what you get from superpowers here,

which is we're extracting out the ability into...

What am I talking about?

I just saw something interesting, so I'll answer that.

Looks like you were overloading skill,

which Claude also means to use all skills. Yes.

That's why I'm talking about abilities versus commands, essentially.

And Claude also has an idea about commands.

So Claude code command.

Here they are.

So commands are essentially skills that only the user can invoke.

And commands are kind of deprecated in favour of skills.

This is why I'm sort of talking...

The language is confused here,

because I'm basically using ability to be a skill that the model invokes,

and procedure to be a skill that the user invokes.

So, yeah.

So grilling, for instance.

This one here.

This is...

Essentially the difference between the two is whether you put

DisableModelInvocationTrue.

So if you put DisableModelInvocationTrue,

this means the model cannot itself invoke the skill.

Whereas if we look at GrillMe,

GrillMe now has DisableModelInvocationTrue,

and it's literally just run a grilling session.

And then grilling here,

this one, the model is allowed to invoke it,

and it invokes it basically based on the skill,

or it can invoke it itself.

That is a skill that acts like a command that runs a skill as a skill.

Don't be silly. Don't be silly.

Yeah, so a skill with DisableModelInvocationTrue is a command.

I mean, I think we should probably use

ProcedureSkill versus AbilitySkill.

And Superpowers, for instance, is all AbilitySkills,

whereas I tend to prefer ProcedureSkills,

and this is kind of mixing the two a little bit.

This means that you can design your own skills,

which use a grilling session,

or let's say have a single source of truth

for what a good codebase looks like,

which is in this codebase design skill.

Or you might have a DiagnosingBugs skill.

So this is a sort of setup that you can use for diagnosing bugs

that the agent is now able to invoke itself.

Let's see, ResolvingMergeConflicts, another nice little skill.

Use when you need to resolve an in-progress merge conflict.

This is a nice little one here.

But most of these two, let's say two issues,

these are all procedures.

The main idea here is that it allows me to turn on

DisableModelInvocation on more skills.

I actually should turn it on for most of the skills in the repo.

I didn't because of some cool code bug, which is now fixed.

Yeah, the benefit here is that I'm now able to...

Let's see.

How many places are referencing codebase design?

Let's see.

Yeah, so for instance, in TDD,

TDD also sort of had a bit of blending over to...

Yeah, here we go.

It had a bit of blending into codebase design.

But now TDD can just take all that codebase design stuff

and just have a single source of truth for it.

So it's basically making the skills a bit more modular.

Yes, I'm sort of using language tense

to describe an ability, sort of.

Atoms are agent-invoked molecules and compounds are user-invoked.

Everyone always goes for those.

I remember atomic components being popular in React for a while.

Atomic components, compound components.

Everyone always wants chemistry to work,

but it never quite works as a metaphor.

Pleasantly surprised if Claude invoked GrillMe itself.

Yeah. But this is the idea.

I think if I was designing this from scratch,

this is how I would do it,

and I probably wouldn't have so many procedure skills, actually.

Like, the procedure skills are really...

Like, technically, you could just write yourself.

If I go into... Let me demo this.

Let me just link the skills.

And I just go, Claude, instead of running like Grill with Docs,

you could just run...

Do a grilling session, and let's domain model it.

You know what I mean? You can just do that,

and it should pick up both skills...

Or both abilities, rather, and pull them into the context.

So, yeah, I don't know.

But then just having Grill with Docs as the shorthand is pretty useful.

Procedure, I don't think, can call a procedure,

because it doesn't have the...

It doesn't have the description in its context window.

Do I feel my approach could work for mobile app development? Absolutely.

Absolutely. There's nothing really different about mobile app development.

All right.

So, friends, let's go back to the slider.

Feel free to ask any sort of questions about the skills,

or let's just sort of roll through.

This is your time, really. I mean, this is...

For many of you, this may be the last in-person session

that we have together if you're not tuning in for the afternoon,

or if that doesn't make sense for your time zone.

So, this is your moment. Ask your questions.

Vote on the ones that you want to be answered.

And let's make these 15 minutes count.

So, I have two questions.

Have you tried compound engineering skills and Shad C and Improve?

Differences between MDD and these.

MDD is catching on, man. Well, I'd test them like thermonuclear.

So, Shad C and Improve looks okay.

It looks like pretty meaty single skill.

I prefer smaller skills that you can split up

and sort of prune, basically.

I think it does need a little bit of pruning

and a bit more progressive disclosure.

It's quite a fat single skill.

I've not tried compound engineering skills.

I've just not tried them, not investigated them.

I've heard they're pretty good, but not tried them.

Differences between MDD and these.

Differences between MDD and these.

I can't really talk about compound engineering

since I don't know it that well.

Shad C and Improve seems quite narrow.

It's like just improve the thing.

And I think Shad C and Use is my skills

for his daily development anyway.

So, I think it's just an addition onto them, basically.

Will I test them like thermonuclear?

EVALing skills, I think, is not very sensible.

I think it makes sense for situations

where your skills are mostly abilities,

because you want to make sure that the agent picks them up

at the right moments using the right prompts.

But, I don't know.

I don't see much value in EVALing them.

I think what EVALs do is they just push a bunch of data

through a system.

And what I have is hundreds of thousands of users

across the world all using my skills, giving me feedback.

So, that's another way of pushing data through.

And as long as I'm responding to the feedback,

then it's sort of the same thing.

And that's what a lot of people are doing now

with EVAL encoding agents.

They're just looking at user data

and reading them and making changes.

Is it a good idea to always apply Caveman and Claw.md?

Oh, I don't know.

Caveman, like, I was experimenting with Caveman

in my skill set, because Caveman is not something

that I came up with.

Caveman is based on a different project.

I just pulled it into my skill set,

and it's hung around ever since.

And I will be removing it at some point,

because I just don't use it.

The idea about Caveman is that you get the agent

to speak in a really truncated, non-grammatical way

in order to save on tokens

and also, crucially, save on your reading, too.

However, I've just not played with it enough

to know whether it's a good idea or not.

I don't know whether it degrades performance.

I don't feel like it would,

but I just haven't tried it enough, basically.

I don't know if Caveman affects the generated code.

It feels like it could,

but again, I don't know.

How can you best prepare for larger projects

to minimise issues running AFK

and structure human loop tasks

to avoid holding up other things?

So...

minimise issues running AFK...

I actually don't understand the question.

I don't understand the question.

Best prepare for larger projects.

Minimise issues running AFK and structure human loop...

I don't understand the question.

Apologies.

Is this about how do you increase throughput?

You increase throughput by essentially having

multiple parallel threads by...

Let's say you...

No, I'm not sure how to answer this question.

I'm so sorry.

You frequently say to avoid summary files

for repo overview, code standards, etc.

But what about really large repos

or working across multiple repos?

Well...

In the research section...

So, okay, the problem here is that

the codebase is the source of truth.

And the code itself, rather,

is the source of truth on how it behaves.

The tests that test the code are the source of truth

because they are runnable snippets

that actually exercise the code itself

and check that it's working.

So you can...

If you want to understand how a codebase works

or how a piece of code in the codebase works,

look at the code.

That's the thing that will tell you.

However, that can be expensive, very expensive,

if you need to explore multiple files

and just to check how a simple function works.

So it makes sense to think,

what if we just created a summary of this piece of code

and let's say we updated the summary

every time that the code changed.

You know, we got an AI to write some docs about it

to understand how it works.

And those summaries are useful

because they save on tokens,

but they can go out of date very quickly.

And it's essentially you're caching

a part of the explore phase.

Now, that makes a ton of sense

for things that don't change very much.

So it makes a ton of sense for third-party libraries,

let's say, that have a contract with you

that cannot be broken or they shouldn't break it

until there's a major version bump.

So it makes sense to go and research

those third-party libraries,

save it as a local markdown file

so that you're good to go.

But for things that do change

on a decent tempo like your own code,

it's pretty difficult.

What I would say is that

if you've got a large AFK setup

or a large chunk of work that needs to be done

all in one area,

and you have a kind of static piece

that needs to be referenced every single time,

let's say you're building a new feature

and you're using an existing engine within your code,

then it makes sense to create a summary file for it,

and I call this research.

This is another nice phrase I have for this

is just-in-time documentation.

In other words, you create the documentation

based on the code, create a summary of it,

and then you use that summary

to sort of power the rest of it.

So it's just another technique in your arsenal.

I don't...

Like, you want to avoid summary files

for the sake of it,

because actually reading code

is sometimes not that expensive.

But...

And I think often really large repos,

it's often just about finding the right code faster

rather than needing to summarize the code once it's there.

So that means you need to be thinking about...

I've started using this metaphor for local roads and highways.

Agents can explore your code base using local roads,

like, you know, just the roads

that link your house to the shop or something.

And it's a pretty slow process,

but they will eventually get there.

And, you know, they go...

They have to navigate through all these little winding areas.

Wouldn't it be better if you just put a highway down

to say, okay, this...

If you're working in this area of the code base,

this is where you need to go.

And that highway would look like a context pointer

within Claw.md by saying,

okay, if you need to modify the...

I don't know, the optimistic view engine or something, whatever,

then you have a highway that the agent can go on to go,

right, I'm now here.

And that's a really cheap way of speeding up...

Speeding up exploration

without necessarily needing to worry about things going out of date.

So, hopefully that answers your question.

There's a few different things, though.

Who... What has influenced me the most?

Oh, I hate these open-ended questions.

As an educator, as a dev,

or, yeah, I assume you mean as, like, a dev and AI person.

I think I was really influenced by Dex Horthy.

He has a couple of really great talks on the AI Engineer channel.

I sort of took the SmartZone dumb zone language from him.

Geoffrey Huntley as well was the one who really, like...

His Ralph Loops idea really electrified me

and made me see how easy it was,

simple it was to create an AFK agent and start shipping work.

And also I saw an amazing talk by...

What was his name? Oh, no.

It's the CEO of Burintum.

I saw this guy do a talk at a local event

and it blew my mind in terms of what he was setting up,

sort of building a factory

with just GitHub actions and GitHub workflows.

And that's really what I based my kind of new setup on.

So GitHub workflows inside here,

a lot of this is based on this guy's work.

Blimey, what was his name? Lars Brintum?

Brintum? He's basically the CEO of Brintum.

I can't believe I can't remember his name. That's so embarrassing.

Yes, so I think those guys...

I also had an extraordinary conversation with the CEO of Ably.

So we mentioned Ably in the course actually

and I met him after I put it in the course

and he gave me a ton of great tips

on what they're doing internally at Ably

and it's really smart what they're up to.

Sort of similar to the Brintum guy.

So yeah, hopefully that gives you a decent answer.

In my company we use Claude via Bedrock AWS

so I can't use Anthropic API for Sandcastle.

I wonder if you have any suggestions

or running with no AFK flow.

I think you can still do it.

I've seen people... Matt Brintz, thank you.

Thank you, thank you, thank you.

I wonder if I can find that talk as well

because that talk is really, really good.

I think people have set this up

so I don't think you need to worry here.

If you ask in the Discord,

I'm sure someone will have set it up.

What key changes should be called out now that we're at the end

and moving to day-to-day use?

Between course skills and my live ones.

I've not really changed my live ones

while we're running through the course

so they've been pretty static

and even after this PR

you'll still be able to use them in the same way.

I don't think I've done much modification really at all

and anything that I have done like, you know,

grill me turning to grill with Docs,

that's in the appendices.

So I don't think there's a ton to call out here actually

so I think you should just be able to rock and roll.

I do think the one thing I should call out

is that these skills are yours.

You should modify them.

You should not feel like you have to keep up with me

or like it's not like a traditional library

where you're sort of waiting for me to do updates.

Just make the updates yourself.

These are your skills.

Every time I get someone saying,

you know, I pulled down your skills,

I made a modification, is that okay?

Yes, it's okay.

It's wonderful. It's fantastic.

That's exactly what these are for.

Oh, the thing just switched.

Fable 5 was released recently.

What's your take on this model?

Will it boost development or some progress

depend less on the model and more how we steer it?

I think that people are way too focused

on model releases in general.

I've not tried Fable 5 just because I like,

you know, I might give it a go at some points,

but I think eventually it's going to not be on subscription.

It's going to be on API credits,

and so I don't want to get dependent on a model

that will then be modified.

Mostly I just sort of take a week

before I try a new model just to see how it shakes out.

And I think that like the model is very important, obviously,

but the harness, the environment that you put the agent in

are just as important.

I think it's 50-50.

I think that if you...

I had a tweet about this the other day,

which is instead of waiting for a new model

to fix your problems,

why don't you just fix your problems, you know?

And what I mean by that is that if you have,

like if you're having security issues in your code base,

why not just set up Opus to run with a skill

that checks your security every, you know, 24 hours or something?

Why not just build something that does the thing

that you need?

If the new model is revealing some need that you have,

why not just proactively go and address that need?

If you need to improve your code base architecture,

just go and improve your code base architecture.

Like, you know, the environment that your agent sits in

is just as important as the model.

What are my thoughts on making some HTML

for grill me questions to visualise complex design decisions,

et cetera?

Yeah, I think this is smart.

I think that it's a really good way of prototyping, basically.

I think HTML is really useful as people were talking about,

you know, HTML should replace Markdown in everything.

Markdown is really good for agent-to-agent communication,

but it's...

And some decisions are fine for agent-for-human communication,

you know, like a grilling session in Markdown,

which is essentially what it is, is sort of fine.

But sometimes you do need visual examples.

You need to have things kind of visually explained to you.

And that's why, for instance...

Actually, this is something worth calling out,

which is that improved code base architecture,

if you use the live version,

it will give you a HTML readout of, like, everything that...

of all of the possible ways that you can improve your code base.

So for things that are primarily visual

or contain a lot of dense information, HTML is great.

For my review skill,

I've had a lot of luck adding a third architecture axis

with the skill thinking,

have you experimented with this or similar?

No.

Will. Message...

Will send a...

Open a Discord thread about that.

That sounds really interesting.

That sounds really interesting.

Again, I'm still not...

Still haven't released the review skill,

just because I'm not... still not happy with it.

So a third axis would be really useful.

Hmm. Markdown, Taipura, Mermaid, QuickCharts.

Nice.

You recently discovered the advisor model setting,

a tool that lets a smarter model like Opus

consult a faster executor model like Sonnet.

Let's give it a go.

Advisor model, advisor tool.

Huh. I've not seen this.

Pair a faster executor model with a higher intelligence advisor model

that provides strategic guidance mid-generation.

When did this come out?

Advisor tool is in beta. Ha ha.

Faster, lower cost executor model.

So the idea is that you would...

Hmm.

It's a sort of reverse subagent, basically,

where the main agent is the...

is the dumb model,

and the advisor agent is the smart model.

Interesting.

Add Opus as the advisor for a quality lift

similar to lower total cost.

Currently use Haiku, and you want to step up an intelligence.

Yeah.

Interesting.

I mean, I don't...

I feel like the kind of model that we have right now

makes a bit more sense, which is you would have a...

a smart planner model, which is your main model,

and then you delegate to stupider models

like to do exploration.

I've been thinking, actually, I woke up last night in bed.

I thought I should use Haiku for exploration more,

and I went back to sleep.

This is the life of an AI nerd, I suppose.

And I was thinking I should use a dumber model

for exploration on some repos.

Maybe I'm just burning tokens uselessly.

And maybe I should be using...

Because actually passing things down to a dumber model

to implement, maybe that is just smarter.

So I'm going to experiment with that a little bit.

Taking advantage of the models you provide.

Yeah.

All right.

Where are we at?

Oh my God.

Okay, let's do one more question.

Complete beginner to coding.

Can you guide what languages you must learn?

Python, HTML, TS, and what else?

And what should be my roadmap to strategic coding?

Great question.

So it's a good place to end.

It entirely depends on what you want to build.

I have essentially done my entire career since 2017

working in a single language,

working in types...

Or rather, working with TypeScript and JavaScript

as the main language.

Outside of that, then obviously CSS and HTML

to build web apps,

but I've never touched Rust professionally,

never touched Go.

I did a little bit of PHP, I have to say,

back in the day, and a little...

Like, I was supposed to learn Python,

but then the job fell apart before I needed to touch it.

So I've essentially managed to go my whole career

just focused on a single language, really.

And I think that's a good goal,

because it means you can really focus in on that language

and become an expert.

If you are looking for a strategic roadmap

or a roadmap for strategic coding,

then you should check out my Teach Skill.

This is something I'm really proud of.

Teach Skill, Matt Pocock.

And here it is.

It's essentially you set up a new project,

you open the project in VS Code,

you grab the Teach Skill, you install it,

and then you essentially say what you want to learn,

and it gives you HTML lessons that guide you en route.

And it's unreasonably good.

I've been using it to learn Rubik's Cube.

I showed it off in, I think, the third office hours,

and I would recommend that as your path.

It's very, very, very cool.

Okay.

Thank you so much for joining along with the cohort.

It's been, I mean, it's always an absolute joy to run these,

and it's so wonderful seeing so many people,

not only from the new cohort,

but previous cohort joining in and having a whale of a time.

And it's always so good just seeing all the great feedback

and seeing people, like, see their minds explode with,

especially just context paranoia seems to be the big one,

the big takeaway,

and also the idea that they can parallelize themselves

with AFK agents.

And everything that we're doing is hopefully a frame

with which you can use to build out better and better stuff,

more awesome stuff you're putting out in the world,

and hopefully reclaim a little bit of control in this AI age,

because it can feel like you don't know what to delegate,

and you feel like you should be delegating everything,

but hopefully it feels like now you can retain your thinking,

retain your control,

and just delegate what you need to to AI.

Let's finish there.

I could do a little post stream where I solve this Rubik's Cube,

but I'm not going to.

So the Discord channels are never going to go away.

My official support ends tomorrow, basically.

I'm not officially going to be responding to stuff in the Discord,

but folks from the previous cohort know that I can't help not responding.

I check the Discord every day.

I'm going to be around,

but my official support ends tomorrow.

No worries, pals.

All right. I'll see you in the Discord today.

Rafael, well done.

100% completion.

Attending every single session from this cohort in the last Rubik's Cube solve bonus stream.

I'm getting far. I mean, I don't know about that.

I'm getting faster than I was, definitely.

I'm really enjoying it.


### 092-AI Coding for Real Engineers p92 092 Final Office Hours - Afternoon

Hello pals, here we go. We have our final office hours. I'm so glad you can join me again.

Thank you so much for joining this cohort and having fun with everyone and going through

the material. Hopefully you've got a lot out of it. I know I've certainly got a lot

out of it just from seeing all of your questions and all that stuff. It's just so wonderful

seeing people go through the material. I know I see this every time. So welcome. It's the

last one. It's the last one. That's funny. Are people talking about the real engineers

title in the chat? Yeah, Matt was confused. What happened was I had an agent or something

went through the stream and basically created all of these live streams, except it created

all of them with the same name. And then when I go to select the broadcast to stream

to an OBS, it has all of them at the same name, not sorted by date. So for some

reason, I think my brain just picked one and turned out I was streaming to the

wrong one. So turned out now we need a new link for today.

Should have a subscription for more office hours. Design.md. What's it? I don't know

what a design.md is here. So folks, what we're going to do is first 15 minutes,

we're going to do Q&A. Second one, I'm not sure what I'm going to demo today.

It would be nice to hear from you guys what you think I should demo because I've

got some ideas, but I'm not got anything really locked in. Is there a Rubik's cube

question floating around? Yeah, the original link is a different link. Yeah.

And then we'll do 15 minutes more Q&A. That's the theory. So feel free to

upvote questions because the top question is the one that I'm going to

vote on. Then halfway through, we'll mix things up and see where we're at.

I'm especially interested in hearing what your learnings are from this cohort.

I kind of want to, I think in our middle section, sum up the main takeaways

and hopefully the skills that you've developed. England are going to win

the World Cup, that's for sure. Okay. What's been the most substantial

impact in learning you've had between the previous and current cohort that

we can apply beyond skills or course material? Will you always ask these

massive wide open ended questions? I think you've had like five of these from

me. Most substantial impact and learning you've had between the previous and

current cohort. It's such a hard question. Can I come back to it?

Okay, how about this? I'm going to reframe the question slightly, which

is I'm going to answer a different question, which is what am I thinking

about next? Where am I planning on taking this material next? What am I

planning to explore next? I still feel like I'm at the start of my

journey into this stuff and the places I want to go next are

interesting. I want to do more automated review. Automated review is

something I didn't quite manage to squeeze into this cohort. I think

actually that might be something good to cover in the middle section.

There's never enough demoing of St. Calc's usage. Maybe we could do a

little demo there. There's an idea that I haven't been able to get out

of my head, which is I'm continually obsessed by the idea of going back

to what we used to do before AI and taking those techniques and putting

them in the AI era. The big technique that I'm thinking about is

red-green refactor. In the course, we talk about red-green, really. We

talk about writing a broken test or writing a failing test and then

making it pass, but the refactor part of that is a little bit fluffy.

We say refactor if you can, but usually a model, once it's done its

work and it's got the previous implementation in its context window,

that previous implementation then it sycophantically goes, oh yes, that

looks good. It doesn't see many places to refactor. You generally need to

either open up a sub-agent that's going to do that or you open up a

new session in order to get it to review. That's where I think you can

get a lot of juice is use a kind of crapper agent, maybe a crapper

model on the implementation, produce a crap implementation and then get

a really nice agent to walk through that with a really nice diff and

just get it to improve it. I think that's going to end up being a nice

trade-off in terms of cost and in terms of quality. That's where I'm

thinking of going next.

Do you know when the next cohort will take place? Will those who

completed a previous cohort receive a discount for future cohorts?

It depends. The reason I gave... Cohort three people got this one

for free because it was a pretty small incremental upgrade and I didn't

feel like I could give them like an 80% discount or I could just get

them in for free and get all the benefits of the wonderful cohort

three people taking part in the community and stuff. I'm not sure

whether the next one will be a full re-record or whether it will be

a full... Like an incremental change, we will keep you updated. I

do have plans, but I'm not willing to reveal them yet. Could you

provide a walkthrough of your GitHub actions agent setup and how

to replicate it in linear? I did this, I think, in... That was the

topic for office hours three, I think, or possibly two. I

definitely gave a fairly detailed walkthrough of this. I don't want

to repeat that. For those who don't know, if you go into

GitHub, Matt Pocock, and either the Sandcastle repo or the

course video manager, they all have this GitHub workflows where...

And we could probably talk about this soon as well. Basically, each

of these... Let's say you have an agent review. Let's say I have

a pull request that comes in from a contributor and I want that

pull request to be labeled. Or sorry, I want it to be reviewed

by an agent. I then label that with a label of agent colon

review here. And what that does is it does a couple of things.

First of all, it adds the agent in progress label to it. It runs

a GitHub action, checks out the PR branch, installs all the

dependencies, installs Claw code, and runs a NPX TSX

Sandcastle review. Very, very cool. What this does is it

pushes any commits onto the branch. So it creates some

commits. It creates some review comments too. And it sort of

posts the review, etc. Marks the PR ready for review, posts the

thread replies. It's great. And this means I can just with a

label get a random reviewer to come and review the thing. Now

the question then becomes is how do you write prompts that

are good at that? What does the prompt look like? If we

go into .sandcastle, we go into review, we go into

prompt.md, for instance. You are an expert code reviewer.

Your job is not just to comment, actively improve the

code on the branch, explain what changed, review process,

blah, blah, blah, blah. And this is fairly generic, but I

usually get some good stuff out of this. This also

follows the particular coding standards in the repo as well.

So .sandcastle forge slash coding standards, which is

sandcastle coding standards. This has all of my stuff

like use effects, optional parameters, all files and app

root, blah, blah, blah, blah. I usually get really, really

good stuff from here. So that is sort of hopefully answers

your question. You can replicate it in linear by just

having a web hook that you might need to if you're

hooking up linear directly into GitHub, you might need to

have some kind of server that sits between them, where

linear would ping off a web hook to your server and your

server would send through a GitHub workflow request to

actually run this. So that's perfectly possible too. You

should also look at something like OpenAI's

symphony, which is a simpler version of this. Are there

any upcoming AI developments not covered in the course

that you're personally keeping an eye on? And would

suggest others do as well. One thing that actually

happened a couple of days ago is that subagents in

Claude code and probably now will everywhere have the

ability to spawn more subagents. Before, actually,

let me pull up a diagram for this. Before you would

have, let's say you have your main agent up here,

then this main agent would only be able to spawn a

subagent like this. And this would only go one

level deep. You couldn't then, before you couldn't

then have subagents which spawned more subagents. But

now you can actually go crazy. You can actually have

subagents that spawn subagents that spawn subagents,

and you can go five levels deep. So suddenly you've

got this mad kind of like, I don't know, family

tree here that agents can spawn subagents can spawn

subagents. Now usually I'm only sort of

interested in this going two levels deep. But

what it means is you can treat this subagent

before you would have to treat it kind of like

a lower powered main agent, right? Your subagent

was just good for one job, and that was it. But

now that subagents can explore by themselves, can

do tasks by themselves, it's pretty nice. And

sure, okay, let's, someone saying sounds like a

token monster. But let's imagine that this

subagent here is actually a subagent powered by

Sonnet. Your main agent is powered by Opus,

let's say, subagent goes down to Sonnet and

let's say explore is Haiku down here. You

start to realise, oh, interesting. Every time I

go down a level, I can actually drop my token

spend by an order of magnitude. So this

actually could be a nice balance of both. And

so I'm interested in working with subagents

more and seeing what more juice I can squeeze

out of them. Because before I was always be

really annoyed whenever I had to use a subagent,

because subagents just didn't feel powerful

enough. Subagents can't spawn their own

subagents, they don't feel great. But this

seems interesting to me. So I'm experimenting

with that. So I don't know whether that's an

upcoming AI development. I don't usually try

to look into the future. I just sort of get

excited by what's currently been released.

What do you think personally makes a great

design.md? What's a design.md? Am I

missing something here? I don't know what a

design.md is. I'm going to leave this one

up until someone in the chat can tell me

what a design.md is. In an AI world where

devs review code more than they write it,

how can they keep their programming skills

sharp? Personally, I learn best by writing

code myself. Now, I've been doing some

research actually into education, like the

academic basis for education, how people

learn best and what the research says

about it. And it turns out that people

say they have like learning styles, you

know what I mean? I learn best by doing,

I learn best by blah, blah, blah. But

that's not really born out in the

research. Basically, there are good ways

of teaching and bad ways of teaching. And

if you match someone's learning style to

their or like their learning preferences,

if you match that, then they have a

better time while they're learning,

but they don't necessarily learn better.

So what I would say is that, yeah,

sure, devs don't like reading code,

because you feel proud of the code that

you're writing because you're solving a

puzzle while you're doing it. It's kind

of enjoyable. It's very enjoyable. But

you might actually learn best by reading

code. You know, I certainly when I

started looking at open source repos,

and actually reading other people's

code, that was when my career just

took a massive trajectory upwards.

Because I wasn't just reading my

teammates code, who were largely writing

the same stuff I was. I was discovering

all these incredible things that you

could do with code and understanding,

oh, wow, that's just such a cleaner

abstraction. I think I saw my first

generic type by looking at someone else's

repo, right? And I thought, oh,

interesting. So sure, you might feel

like you learn best by writing code,

but actually you can develop yourself

extremely quickly by reading code. And

guess what? There's a lot of code to

read these days. Okay, still don't know

what that one, anyone know what a

design.md is? Anyone know? Anyone

know? Okay. You just spun up your own

learn TypeScript repo using teach will

report back. Given your new skills,

thinking and the work on the AI

dictionary, is there a chance of a

seeded glossary context for AI related

talk in your skills? So what Will is

asking here, for those who don't know,

AIcodingdictionary.com is a kind of

experiment that we're running at the

moment. Let me get my face out of

the way so you can see this beautiful

website. This is built by Vojta, who

is the guy who builds all my stuff for

me really, and works with lots of people.

So if we click on one of these nodes

here, we go to compaction. And this is

a full dictionary of AI coding. So

this is what I've tried to base most

of my material on. It diverges in a

couple of places, but we can see that

like a primary source here, there's a

handoff artifact. There is the

environments that the code runs in,

the agent, the spec, which is kind of

what I call the PRD now. Agents.md, a

context pointer, progressive disclosure,

input tokens. Look at this website,

man. You can actually have colours on.

Oh my God, it's so good. It's so

cool. Vojta really cooked here. So

what am I saying here? What Will is

asking is, is there a chance of a

seeded glossary context for AI related

talk in my skills? So I have applied

this concept of a glossary, because

anyone who's worked with Grille with

docs knows that if you build a

glossary of your own code base, it

means that when you talk to your

agent, you can use really precise

language because you're both talking

about the same stuff. And I've done

the same or trying to do the same

with one of my skills particularly.

So if we look at mapPocot skills,

we look inside skills, engineering,

improve code base architecture,

you'll see a language.md here. And

this, I'm very proud of this. It

describes the exact language that you

should use when you're talking about

code. So here we have a module, a

concept of a module, which has an

interface and implementation. Then

we have a concept of depth. How

deep is that module? And what do

you get from depth? Well, you

get leverage. So more capability

per unit of interface they have

to learn. In other words, if

you have a deep module and it

has lots of capability inside it,

then anyone calling that module

is going to be able to do a

lot with it. It's powerful. And

you also have locality. When you

have a deep module, lots of

related code is grouped together

and that means maintainers really

benefit from it. You get the

idea. If you start to internalise

these terms, you can speak about

code base architecture a lot more

fluidly. It's really, really

cool. And I suppose what Will is

asking is, am I planning to do

this for AI coding itself? I

don't think so. Maybe. I would

like the, I do think skills

benefit when you use a sort of

unified language because it

allows the model to again,

compress its thinking a little

bit. It is something I've thought

about and it's something I'll

continue to think about. Okay.

I'm going to ditch this

question because I don't know

what a design MD is. I can't

see anyone in the chats has

answered me. So maybe I'll

give you a little bit more

time. For GitHub actions agents,

what makes an implement review

skill reliable versus a local

chat skill? How would you

structure inputs and outputs?

Okay. You guys are really

interested in this. So I'll

show you. So Soundcastle has a

little known ability, which is

if we look inside Soundcastle,

we'll look inside review and

we look inside review.ts.

Then what we see here is that

I added this fairly recently

and it didn't quite make it

to the course, but where are

we? Okay. We have a function

here called run with

extraction, which is a

slightly funky name, but what

we can see is that the

output of this, if we go to

Soundcastle.output.output,

you can pass in a tag of

output and then, or a tag of

whatever, this piece of text,

and then a schema of review

output. If we look up at

this schema up here, it is a

Zod schema. So just up,

where is it? I missed it.

Maybe it's coming from

somewhere else. Yeah, review

output up here. So it's a

Zod schema. Can I go see it?

I want to see it. Here it

is. Yeah, there we go.

Review output. So it's a

Zod object. What this means

is that essentially we are

looking inside the output for

a XML tag containing some

JSON and then Soundcastle

will use this schema

validation library, Zod, to

check it out, to basically

make sure that it matches up.

And then we can take that

output, so wherever the

ran output here, so result,

we have, should have

result.output somewhere in

here, result.output.inline

comments. So these are the

inline comments that the

agent is going to leave on

the review. Really, really

cool. Really cool. Replies,

blah, blah, blah, blah,

blah, so output.replies.

It means that you can

essentially use the agent

as a way to get structured

output back and then use

that to then power up

other stuff. So use that

to, you could use it to

kick off other agents if

you wanted to. You could

use it to leave review

comments as we're doing

here. I think in

implementation, do we use

it? I don't know. We use

it in a bunch of places,

but hopefully it gets your

head kind of spinning that

you can actually have an

agent that implements

something and then

return some structured

output so you can do

something with it. That's

really, really powerful.

And that's what makes it

reliable as well as we do

have a sort of retry

function in there. I

really think you should

just go have a look at

the repo itself, get your

agent to sort of look

through all of the code.

This is probably where I'm

going to go in terms of

future material for the

cohort is talking about

this stuff because it's

incredibly powerful, the

stuff you can get done

with it. Google Standard

for design from Google

Stitch. I don't know. I

still don't know what it

is. I've never used

Google Stitch. I don't

know what it is.

Apologies. So creating

skills, compact skills

that call each other when

needed versus big skills

doing multiple tasks.

It's a great question.

Oh, it's a great

question, but we need to

we need to get to the

middle section here. Oh

God, what was I going to

I had an idea for what

I was going to teach in

the middle section, but

I've forgotten it. That's

terrible form. Oh yeah.

Yeah. Okay. I remember.

So I think what I want

you to think about is

and something that's

come up again and again

and again is implementation

versus review. So

implementation on one

side, review on the other.

And I want to split up

review into a few

different places. I want

to split it up into

automated review and then

human review and maybe

even split it up even

further, which is that

you have implementation,

you have automated checks,

then you have automated

review and human review.

And these are all of

the layers that the

implementation needs to

pass through before it

gets to human review. So

implementation is

obviously just the agent

producing some code,

producing some commit

that then goes to

automated checks and

those automated checks.

We know our sort of

feedback loops, right?

So tests and type

checking and any pre

commit hooks, formatting,

et cetera. Those then

I think in a properly

solid system should go

through an automated

review phase where you

take an agent, you

take a look at the diff

from the implementation,

assuming that it's past

the automated checks and

then you get it to

review that to make

sure it matches up to

two things. So what two

things are you checking

during automated review?

You're checking that it

matches the spec first of

all. So a spec or let's

call it a PRD is the

thing that's kind of

driven the

implementation. So during

automated review, you

go ahead and check

whether the PRD is

accurate or rather

whether the PRD has been

implemented properly.

And then you go into

the other thing you

check is whether it

matches your standards.

So these standards can

be written down. A lot

of people write these

in Claw.md, but I

prefer writing them in

coding standards.md.

And there's a bunch of

questions here. There's a

bunch of questions

related to when you

should like put your

coding standards into

context. But I think

that they're perfect

during automated review.

That's when you want

your coding standards.

Now, the final thing to

look at then is then

automated review goes

into human review. And

then finally we can

get to this point. So

implementation happens,

automated checks happen,

all of this is

automated and only when

you get to human review

is it actually the

human is required.

So everyone's sort of

following me so far.

Now, the question here

is how much juice do

you give to implementation

versus automated review?

And by juice, I mean,

how big a model are

you using here? So

let's say we use,

let's have like these

little red dots

represent opus, let's

say. So we could use

opus for this and for

automated review, right?

Or why don't we do this

for like a big model

and this for like a

small model?

Hopefully that sort of...

No, you'll see what

I mean in a second.

I find it so hard to

like narrate while I'm

building a diagram.

So if we use opus for

both of these, if we

use a powerful model

for both implementation

and automated review,

then it's going to be

very tempting to sort of

pull in the coding

standards to have them in

both, right? So both

the implementation and the

automated review use

coding standards.

That's probably where

most people intuitively

land, right? You should

have one set of coding

standards and the

implementation tries to

work from them and the

automated review tries

to work from them.

But if you think about

the implementation,

then it's going to do

a lot of work, right?

It's got to implement

the thing correctly.

It's got to make sure

it passes the automated

checks. It's got to

live up to all of the

standards. It's got to

explore the code base,

look for all the

relevant code. It's

going to do a lot of

jobs. And I personally

think that the best way

to do this is actually

to remove the coding

standards from the

implementation to

actually make it so

only the review sees

the coding standards.

In other words, I think

of there as being an

implementation budget

and a review budget.

And in the

implementation budget,

we zoom out of here.

So let's say this is

the implementation budget.

This is the review

budget.

And review.

Now let's go through

all of the parts of

what makes up a coding

session and see what's

needed in implementation,

what's needed in review.

So in implementation,

you need to explore

the code.

That's going to take up

some chunk of time,

right?

In review, do you

need to explore the

code? You might need to,

but it's a little bit

less, right? Because the

review is passed in

the exact diff of the

implementation.

So the review already

knows exactly where to

look. And any exploring

it's doing is really

just sort of checking

around the code that it

already knows about.

So the review needs to

do much less

exploration.

Implementation needs

to go and actually

implement the thing,

needs to spend a lot

of tokens writing out

the files.

Review doesn't need to

do that. Review just

needs to sort of make

the small changes that

it needs to. So it

often needs to produce

far fewer tokens.

And also, by the way,

not only exploration

and review, but we're

also loading in stuff

on top of this. So

both of these things

need to receive the

PRD. So let's put the

PRD at the start here.

The PRD, any related

issues, blah, blah,

blah, blah. So review

also needs that.

Let's put in the

diff for the review

as well, because the

implementation doesn't

get the diff.

But we can see, start

to see that the review

has lots of small

bits to do, and it

doesn't have these

huge great big chunks.

The other issue with

implementation is it

needs a ton of budget

to make sure things

don't break. So it

needs debugging budget

as well. If you

force the implementation

to do coding standards

on top of that, like

if we imagine oranges

are coding standards,

then you can start

to see the

implementation just gets

massively overloaded.

And I think reducing

the amount that the

implementation has to

do and giving that

to review instead

means you end up with a

lot higher quality code.

So I think that

this is how I'm

starting to think about

things, pulling

information out of

implementation and putting

it into the review phase.

I'm really interested

to know what you

what you guys think

about that. What I'm

seeing is that I can

then take implementation

and put it on a

lower quality model.

So I can put it on

Sonnet instead of Opus

and then review I keep

as the higher quality

model to kind of

catch things. And I

end up spending fewer

tokens and being

still getting the

high quality here.

Does the Automator

Review Agent fix the

culprits? Yes.

So it commits to the

branch. So basically

by the time you get

to human review,

the Automator Review

so just take off there.

The Human Review

basically should have

a perfect PR to look at

in theory. So it

should not have like

what I like doing is

I like the Automator

Review to fix things

and then I like it to

tell the Human Review

what it's fixed.

That increases my

confidence a little bit.

There's even more we

can talk about here

with like a step

between the Automator

Review and the Human

Review to make the

Human Review as easy

as possible.

There's lots of creative

stuff people are doing

here.

Adversarial Agent

concept? Yeah, basically.

So the Automated

Reviewer is like a

a second agent looking

at the previous agent's

work. And you can

of course make the

Automator Review be

GPT 5.5 and the

implementation be

Sonnet. For instance,

you can have different

model providers, let's

say for different

perspectives. I think

that's a bit overblown.

I think that just

clearing the context

does a good job to be

honest.

Is this why you're

doing red green,

red green refactor

at the end? This is

essentially kind of

like red green

refactor basically.

The implementation does

the red green and the

Automated Review does

the refactor.

Do I have any course

or repo on the best

how to do that auto

review in the best way

possible? Yes.

This course video

manager does this

already. So if you

look at, for instance,

in fact, I've done

this already. I had

some bugs that I

noticed in my

implementation earlier.

Sorry, two seconds.

And or that I noticed

in my app earlier.

I have this is so

cool.

Inside the app

itself, I have a

button that can create

an issue and it gets

labeled with agent

implement. Then a

GitHub action, pick

this up and marked

it as agent implement

and opened a draft

PR. That draft PR

was labeled with

agent review.

So it labeled the

agent review, added

the agent in progress,

remove the agent

review and it said

clean correctly

scope PR. This is

nice information to

see like the

Automated Reviewer

likes the stuff.

Every user facing

string is updated.

No code changes

needed from review.

Ship it.

Now, for some reason

it does.

Wait, did it have

both of this?

I don't know.

Something happened there.

Strange.

But I can now

just look at the diff.

I can go, OK,

yes, this all looks

good. Do I want to

delete this?

Delete section.

Yeah, it's a tiny

little diff here,

like nothing.

So I will just

merge it.

Looks good.

Squash and merge.

Bang.

Looking good.

Got to get that white

balance right.

Yeah, for those who

don't know, I just

that thing turned off

and when it turns off,

the white balance

screws up for some reason.

I've got a very

strange setup here.

To be fair,

Fable does an insane

job on the code

generation in the

first place.

Yes, I mean, you can.

You can.

Every time you light

a cigarette, you can

use a blow torch

if you want to.

You can get a flame

thrower to light

your cigarette, but

why not just use a lighter?

You know what I mean?

Why not just use the

tool that's fit for the job?

So.

Hopefully that diagram

gives you a little bit

more insight as to

what automated review

can look like.

And I recommend you

think to yourself,

how would I implement

this in my current setup?

How would I take the

PRs that I'm producing

and create these

automated loops to,

or I don't know,

automated loops.

It's the right word.

It's the hot word right now.

How would I get AFK agents

to review it myself?

Fable is a flame

thrower because it's

extremely expensive.

OK.

So creating skills,

compact skills.

What we'll do now,

by the way, is we'll

spend the next 15 minutes

going through a few

more questions

and then we'll finish up, guys.

Creating skills,

compact skills,

single responsibility

that call each other

when needed versus

big skills doing

multiple tasks,

self-contained.

So Shad Cien recently

released.

Shad Cien Improve.

Is that the one?

Yeah.

Released a skill

called Improve.

And what this skill does

is it does a lot.

It's essentially a big

it's essentially a big old skill.

I think I spec'd it out

about 3000 tokens possibly,

which allows you to

do lots of things.

And.

It allows you to improve

PRs, implementations.

It says like, OK,

we can invoke it

either quick or deep.

Can invoke it to test security,

perf tests,

check the branch,

check the next thing,

do a plan,

review the plan,

execute, reconcile issues.

Bunch of stuff.

And what I think

is that this skill

is a bit too big.

It's a bit too bulky.

It's doing a lot in one box.

I think that where possible skills

should try to prune themselves

so they do just the minimum required.

And.

Yeah, that's that's my feeling about it.

I think

the reason why is that

it's a lot easier to edit

and maintain a smaller skill

because that skill just does one thing.

You don't need to worry

about making it too big or too.

Like you don't need to worry that.

It's kind of like global state,

basically, you don't need to worry

that a little change you make

in this skill is going to affect

something totally random over there.

They're small self-contained modules.

So that's my thinking

is that compact skills,

smaller skills are better.

What do I think about the linear's

idea of the future of developers?

Does this resonate and

conform to my workflow,

complement my workflow?

Issue tracking is dead.

It was built for a handoff

model of software development.

A PM scoped the work.

Engineers picked it up later.

But over time, complexity

started to look like sophistication.

The more process system

of control, the more advanced it seemed.

Linear has always been the opposite, believe.

But but but but but but but but

linear is becoming the shared

product system that turns

context into execution.

When I read this, I didn't understand it.

I still don't really understand it.

Linear agent.

Skills, automations.

Yeah, I sort of don't know what this is.

I find that issue tracking

is actually quite a nice way to work relations.

I know that's lame.

I know it's sort of popular to,

you know, like disavow

GitHub and say, Gaps rubbish.

But I think that a way of tracking

your tasks and then

delegating those tasks

is actually effective and quite

good for working with agents.

I think it could do with some niceties.

And certainly it's not as cohesive

as it should be.

But overall, I think the idea is quite good.

And you need at certain points

human in the loop checkpoints.

You need a human to come into the loop

at the right moment in order to

just check that we're not doing

anything insane and crazy

and that the agent hasn't gone wild.

And the more work you can do

before that, the better.

But yeah, I don't know.

I think issue tracking is fine.

It just needs a little bit extra

to do with them.

Yeah, issue trackers are more important now.

What are your top tips

on keeping a grilling session

not too fluffy and not too deep?

It's a good question.

Again, Will, you're killing it

with these questions.

This is a really good one.

So.

When you're grilling,

I found myself today in a grilling session.

The agent asked me a question

and I typed the words, I don't care.

It was like choosing

whether to reuse a piece of code

or just like create

a new function or something.

And I just typed, I don't care.

And that seemed like a good signal

to the agent to just

low bring up the tone

to more important stuff.

Right.

It's kind of like when you bother

when you're a junior developer,

and of course, junior

developers should do this.

They should ask questions

of their seniors.

But sometimes a junior

developer will ask you

ask a senior a question.

And internally, the senior will go.

Doesn't matter.

Does not matter which one you pick.

You can just choose either one.

And maybe they will give

some thoughtful answer,

or maybe they will be honest

and just say that.

So that's part of it is that sometimes

you just need to like

delegate those decisions to the agent.

Sometimes a decision will not matter

and you'll just have to delegate it.

Another one is that you

you also don't want the discussion

to be too shallow.

Or rather, you want to have

the discussion at the right fidelity.

So.

Fidelity.

Is an interesting idea.

And it comes from

or at least I stole it from

Ryan Singer's Shape Up.

And fidelity is basically like a scale.

So if we have high fidelity things

and low fidelity things.

So a low fidelity asset,

let's call it, is like a text question.

It's low fidelity because you can't

really see what you're talking about.

It's hard to get a sense

for what the thing is.

If we say, do you want the button

to be round or square?

That's quite a hard question to answer

without seeing the thing.

But however you can, let's say,

just raise the fidelity a little bit.

And maybe you have a

maybe you have a

what do you call them?

Oh, no, I can't remember.

A vague sketch,

whatever the word is for that.

You have a sort of vague like.

What does he call it?

Like whiteboard marker or something

thick marker,

black marker sketch or something

and someone might know.

You have a sort of vague sketch of the

yeah, wireframe door.

You build a small,

very basic wireframe of the idea.

Maybe you discussed the

buttons or something,

but you have a bit more.

It's a bit higher fidelity,

a bit closer to where you're going,

because the highest fidelity thing

is the actual app.

Right.

And so when you're making decisions,

you could actually go ahead

and sort of like code them

on the actual app and see how they go.

But it's probably better to

wireframe it first.

Or maybe to create a prototype

and a prototype doesn't connect

up to the actual data,

but it might in embed

with the UI itself,

or it might be on a throwaway route

or something.

But again, you're able to have

the discussion at a higher fidelity.

And so you should be thinking

about fidelity when you're

or what fidelity is right

for that question

when you're doing grill mean,

because sometimes.

You will have a question

that's like.

What's the best way this should look?

And it's just really hard

to answer that in text.

You don't know how it's going to look

because you can't give feedback on it.

It's best to either go to a wireframe

to do a bit of design

or go to a full prototype.

Or maybe even there might be questions

that you can only answer

by just coding the thing

and seeing how it feels.

Though mostly.

You can prototype.

It's often very good

to stay at a low fidelity

because this text question

is very cheap to answer.

It's an easy decision

or a quick decision to make.

It's spent.

It's like, you know,

you do spend time creating wireframes.

You spend time creating prototypes

and you can actually operate

at too high a fidelity sometimes.

So operating at low fidelity

by default is good,

but jumping to prototypes

is very important to.

Where are we here?

We are.

What is a CS degree now?

What should our approach?

What should be our approach now

as a student?

Does foundation still matter

for a college graduate?

I never did a CS degree,

so I'm a second career dev.

I used to be a voice coach.

I train myself in development

and, you know,

10 years ago or something.

And it was 10, 11 years ago, Jesus.

And I got into the industry

2016, 2017,

and now I'm here.

What should our approach be now

as a student?

I don't think things

have changed that much.

Honestly, the fundamental

that you'll learn in a CS degree

are the same stuff

that I'm talking about here, really.

Learning about test scenes,

learning about interfaces,

learning about, you know,

essentially moving code around,

building good code bases.

That's more important than ever.

I do think that you need to

take these agents

and think about adopting them

into your flow a lot

earlier than you would.

I mean, very, very early, basically.

They should be doing all

of your tactical coding for you

and you should be thinking

about the strategic stuff.

Because a computer science degree

can teach you the knowledge

and skills that you need

to be a very good

strategic programmer.

A lot of the best

strategic programmers I know

did CS degrees.

But obviously, the wisdom

that you get from working

an actual job is something

that you can't replicate

in a degree.

So I still think a CS degree

is a great place to go.

And, you know, university,

college is great.

After the last cohort,

we created a wiki from the materials

and discussions.

Was it helpful?

And if so, would you be interested

in doing so again?

Extend fresh.

Fresh, I think, probably.

I haven't used it enough,

to be honest.

Mostly, I use the one

that I just created.

I would say,

I would say, why not

ask the folks in the previous cohort

if they liked it?

And because I don't want you

burning open about it.

I don't want you to be

burning open tokens for no reason.

Well, so, yeah, it was cool

last time. Maybe it would be cool again.

What's the hype with loop engineering?

It's a really good question

because when, and I think

this might be our closing question.

Actually, I'll just answer this one first,

which is the state of my writing

skills. I've not really tried.

I have three skills

that I've been working

with in my repo to get good

at creative writing.

I've just not had enough

reasons to use them recently,

so I just haven't worked on them.

But I am, they're still in my head.

So, okay, loop engineering.

So, for those who don't know,

Peter Steinberger had a tweet

that went mega viral, saying

that you shouldn't be prompting AI

yourself. You should be writing

loops that prompt AI.

And I think that this,

you know, it's sort of like

the Zen master from the top of the mountain

has said something, so we must all pay attention.

What he's really talking about

is that if we dig out,

here we go, the seven phases of

AI development or AI coding,

this is something you'll probably see

from the appendixes.

And what he's basically

saying is that

if we think about the life cycle

from getting code from an idea

to shipped,

there are several

parts in here that will need

a human form.

So, let's imagine that the

process looks like this.

Let's imagine that there are, I don't know,

X number of these little arrows over here.

And let's imagine these are the stages

in the process. We're just going to treat this really abstractly

for now. So one of these might be to

explore the thing,

to plan it, to grill it, to create

a PRD, to implement it, etc.

Now, in this

little world here,

some of these phases

are going to be

done by

humans, and some of them

are going to be done by AI, right?

Really making a hash

of this diagram. So these

little checkpoints here,

some of them might be done by

AI. So let's imagine that we

have them like this.

Let's make them a bit thicker.

Oh, they look terrible.

Like that.

That's fine.

Sorry, I'm just diagram

maxing.

The goal, I think, of

what Peter's really talking

about is that a lot of people are

using AI where,

let's imagine that blue is

AI and

red is human.

A lot of people are using AI like

this, where they

essentially, as the human, they

check in on every

single stage. They will grill

and they will then

do a little bit of grilling

and then maybe they produce a PRD and they check the

PRD. Then they check

the issues that are created. Then they

check the implementation

that's produced. Then they check the next thing, they check

the next thing, and they're present for all of it.

But what you should be instead doing is

thinking about these checkpoints and thinking,

how can I remove myself from them?

How can I go from being

mostly human in the loop

to mostly AI in the loop?

If you do have any involvement, it needs

to be towards the end of the life

cycle here. So far,

in sort of MDD, as

the cool kids are calling it, map-driven development,

the approach I teach in this course, is

we kind of have an approach that looks like this,

where we have a human kick

things off with the grilling session,

then they create a PRD,

and then we go through

some AFK stuff,

and then we check it

at the end. That's essentially

what this looks like.

But there are certain situations

where you can remove yourself from

the planning too. So for instance,

in my Sandcastle

repo, I have a tool

that's, or a loop,

I suppose we can call it, that

if someone pings a new issue at me,

and I need to investigate it,

I can either sort of check that out

locally and investigate it and check

if their claims are true, or

I could get an AI to do it, so I have an AI

explore. And so,

there's a sort of an agent that goes

and explores it.

Yeah, MDD, that's what it stands for.

I have an agent that goes and explores it.

And then maybe, I like

what it's explored, maybe I

have a little human checkpoint here, and I decide

to implement it. At which point it implements it,

then it reviews it, and then there's a

PR for me to review,

and maybe, maybe that's

the end of the loop, you know, and so I review the PR

and then we're good to go. And so

the idea here is how many human

in the loop checkpoints can you remove

from your own process?

Because the more you remove, the more

you're able to parallelise yourself.

And that's the theory.

Yeah, that's the theory. So

that's what loop engineering is. And

what Peter means is that you should write

literal loops that run on your

computer that check these things again

and again and again. I think

it's better to automate it in different ways.

You can automate it not using

loops, let's say.

But overall, I'm just loving this.

And I'm starting to take

this approach in my own life too.

That means that if you fanatically create issues in the

Sandcastle repo, you can make you go broke.

No, I do actually, the first thing I do

is I have to manually explore it myself.

In the end, do you completely remove the human in the loop?

No. You do not

completely remove the human in the loop. You still

have human in the loop

checkpoints. Peter Seinberger is the guy who

invented OpenClaw.

Bit sad for you, you're

really proud of the code you used to write.

The model will let you down always. Guys!

Guys!

Let's have a

sort of closing thought here, which

is I really like this new age.

I really like, I've always

been primarily a strategic

programmer, not a tactical programmer.

Even when I was a junior, I was

trying to think about how to

increase our velocity, how to

create abstractions that

would mean we could move faster.

We had a front-end team and a back-end team in one of my early jobs.

The back-end team

was like, when I joined,

the front-end team was incredibly slow

and the back-end team seemed to us

to be super fast.

Nine months in, the front-end

team was killing the back-end team. We would just

implement features like that.

I've always wanted to do that and

try to

make code bases that are easy to contribute

to, because throughout my whole career, that's

what I found most

interesting. I love this new age, because

now I can think at that level.

I can be planning the code

base and understanding it

in a deep way and

trying to

make my teammates better.

It's just my teammates now are mostly robots,

which is okay.

As a trade-off, I'm okay with.

It means that I can produce a lot more,

because robots can

work while I sleep.

But those same

attitudes of

trying to make my teammates better, thinking

about the plumbing, obsessively

really,

benefited me when I was

a pre-AI dev,

and now they benefit me even more.

This new age, I think it means

that if you're just a pure tactical program,

if you're not willing to

think about how to make your teammates better,

if you're just thinking about your own lane,

then you're not going to have fun. But I'm

really having fun.

Bloon the knuckle duster?

What are you talking about?

Good.

Always more proud of the value

software provided to the user.

If AI is going to allow me to

provide better results quicker, I'm okay

with that. Definitely.

We're all in this to

I think that coding

is such an attractive

form of engineering because all of the

parts of it are

kind of magical little building blocks.

They're little magical,

like it's all sort of

working

in empty air and kind of

playing with these cool structures that don't exist

in reality. And that kind of

infinite flexibility, infinite malleability

is sort of what attracted me to coding

in the first place. And

I think AI just sort of leaned into that even more.

Thank you so much for joining. It's been really fun.

I'll be

hanging around the Discord over the weekend

as well, just catching up with threads. There are some

threads I haven't replied to yet and stuff

that I need

to get down in the Discord.

I'm so glad

that you've

yeah, it's Legos, exactly.

I'm so thankful for you to be able to join me

in all of these office hours

in the chat and

I hope you've got value out of the cohort. I've certainly

had value from you guys attending

and being so helpful.

It's been wonderful. It's not a

blue Lego duster. It is a little

holder that came with my Rubik's Cube

for some reason. I don't know why. I would chuck it

in the bin. I just like filling

with things while I'm presenting.

Great. I'm glad you guys

are loving it.

Alright, time to go.

Pure gold? Good.

Well, you guys have been pure gold. Thank you so much.

I'm going to go have some dinner.

Go and pick up my son.
