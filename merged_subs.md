
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


