# Thomas Cholak

# Problem 12

import re
import string        # for removing punctuation from a string
import pandas as pd  # for counting words


def find_words(m):
    count_words = len(re.findall('[a-zA-Z]+', m))                # counts words
    count_characters = len(re.findall('[a-zA-Z0-9-_.]', m))      # counts characters
    word_length = str(round(count_characters / count_words, 2))  # finds average word length

    print(f'There are {count_words} words.'
          + f'\nThere are {count_characters} characters.'
          + f'\nAverage word length is \'{word_length}\' characters.\n')


def sentence_length(n):
    remove_paren = re.sub("[\(\[].*?[\)\]]", "", n)  # omits sentences within parenthesis
    tokenizer = re.split(r'[.!?]+', remove_paren)    # tokenizes new string

    z = 0
    for x in tokenizer:
        new_str = re.split(r"\s+", x)
        updated_list = list(filter(None, new_str))   # removes empty strings from array
        for y in updated_list:
            z += 1

    count_sen_length = str(round(z / len(tokenizer), 2))  # counts average sentence length
    print(f'The average sentence length is \'{count_sen_length}\' words.')


def longest_words(p):
    new_str = re.split(r"\s+", p)  # tokenizes string with spaces
    r = re.compile(r'\b(\w+ly)\b')
    ly_words = list(filter(r.match, new_str))
    print("Words ending with '-ly'\n", ly_words, "\n\n10 longest words:")  # outputs words ending with '-ly'

    new_str = [''.join(c for c in s if c not in string.punctuation or c == '-') for s in new_str]  # removes punctuation
    for i in range(1, 11):
        longest_word = sorted(new_str, key=len)[-i]
        print(longest_word)

    count = pd.Series(new_str).value_counts()
    print("\nWord counter for all elements:"
          + "\nWord         Count")
    print(count)


# https://millercenter.org/the-presidency/presidential-speeches/may-15-2016-commencement-address-rutgers-university
obama_speech = """Hello Rutgers!  (Applause.)  R-U rah-rah!  (Applause.)  Thank you so much.  Thank you.  Everybody, 
please have a seat.  Thank you, President Barchi, for that introduction. Let me congratulate my extraordinarily 
worthy fellow honorary Scarlet Knights, Dr. Burnell and Bill Moyers. Matthew, good job.  (Applause.)  If you are 
interested, we can talk after this.  (Applause.) One of the perks of my job is honorary degrees.  (Laughter.) But I 
have to tell you, it impresses nobody in my house.  (Laughter.)  Now Malia and Sasha just say, “Okay, Dr. Dad, 
we’ll see you later.  Can we have some money?”  (Laughter.) To the Board of Governors; to Chairman Brown; to 
Lieutenant Governor Guadagno; Mayor Cahill; Mayor Wahler, members of Congress, Rutgers administrators, faculty, 
staff, friends, and family -- thank you for the honor of joining you for the 250th anniversary of this remarkable 
institution.  (Applause.)  But most of all, congratulations to the Class of 2016!  (Applause.) I come here for a 
simple reason -- to finally settle this pork roll vs. Taylor ham question.  (Laughter and applause.)  I'm just 
kidding.  (Laughter.)  There’s not much I’m afraid to take on in my final year of office, but I know better than to 
get in the middle of that debate.  (Laughter.) The truth is, Rutgers, I came here because you asked.  (Applause.)  
Now, it's true that a lot of schools invite me to their commencement every year.  But you are the first to launch a 
three-year campaign.  (Laughter.)  Emails, letters, tweets, YouTube videos.  I even got three notes from the 
grandmother of your student body president.  (Laughter.)  And I have to say that really sealed the deal.  That was 
smart, because I have a soft spot for grandmas.  (Laughter.) So I'm here, off Exit 9, on the banks of the Old Raritan 
-- (applause) -- at the site of one of the original nine colonial colleges.  (Applause.)  Winners of the first-ever 
college football game.  (Applause.)  One of the newest members of the Big Ten.  (Applause.)  Home of what I 
understand to be a Grease Truck for a Fat Sandwich.  (Applause.)  Mozzarella sticks and chicken fingers on your 
cheesesteaks -- (applause.)  I’m sure Michelle would approve.  (Laughter.) But somehow, you have survived such 
death-defying acts.  (Laughter.)  You also survived the daily jockeying for buses, from Livingston to Busch, to Cook, 
to Douglass, and back again.  (Applause.)  I suspect that a few of you are trying to survive this afternoon, 
after a late night at Olde Queens.  (Applause.)  You know who you are.  (Laughter.) But, however you got here, 
you made it.  You made it.  Today, you join a long line of Scarlet Knights whose energy and intellect have lifted 
this university to heights its founders could not have imagined.  Two hundred and fifty years ago, when America was 
still just an idea, a charter from the Royal Governor -- Ben Franklin’s son -- established Queen’s College.  A few 
years later, a handful of students gathered in a converted tavern for the first class.  And from that first class in 
a pub, Rutgers has evolved into one of the finest research institutions in America.  (Applause.) This is a place 
where you 3D-print prosthetic hands for children, and devise rooftop wind arrays that can power entire office 
buildings with clean, renewable energy.  Every day, tens of thousands of students come here, to this intellectual 
melting pot, where ideas and cultures flow together among what might just be America’s most diverse student body.  (
Applause.)  Here in New Brunswick, you can debate philosophy with a classmate from South Asia in one class, 
and then strike up a conversation on the EE Bus with a first-generation Latina student from Jersey City, 
before sitting down for your psych group project with a veteran who’s going to school on the Post-9/11 GI Bill.  (
Applause.) America converges here.  And in so many ways, the history of Rutgers mirrors the evolution of America -- 
the course by which we became bigger, stronger, and richer and more dynamic, and a more inclusive nation. But 
America’s progress has never been smooth or steady.  Progress doesn’t travel in a straight line.  It zigs and zags in 
fits and starts.  Progress in America has been hard and contentious, and sometimes bloody.  It remains uneven and at 
times, for every two steps forward, it feels like we take one step back. Now, for some of you, this may sound like 
your college career.  (Laughter.)  It sounds like mine, anyway.  (Laughter.)  Which makes sense, because measured 
against the whole of human history, America remains a very young nation -- younger, even, than this university. But 
progress is bumpy.  It always has been.  But because of dreamers and innovators and strivers and activists, 
progress has been this nation’s hallmark.  I’m fond of quoting Dr. Martin Luther King, Jr., who said, “The arc of the 
moral universe is long, but it bends towards justice.”  (Applause.)  It bends towards justice.  I believe that.  But 
I also believe that the arc of our nation, the arc of the world does not bend towards justice, or freedom, 
or equality, or prosperity on its own.  It depends on us, on the choices we make, particularly at certain inflection 
points in history; particularly when big changes are happening and everything seems up for grabs. And, Class of 2016, 
you are graduating at such an inflection point.  Since the start of this new millennium, you’ve already witnessed 
horrific terrorist attacks, and war, and a Great Recession.  You’ve seen economic and technological and cultural 
shifts that are profoundly altering how we work and how we communicate, how we live, how we form families.  The pace 
of change is not subsiding; it is accelerating.  And these changes offer not only great opportunity, but also great 
peril. Fortunately, your generation has everything it takes to lead this country toward a brighter future.  I’m 
confident that you can make the right choices -- away from fear and division and paralysis, and toward cooperation 
and innovation and hope.  (Applause.)  Now, partly, I’m confident because, on average, you’re smarter and better 
educated than my generation -- although we probably had better penmanship -- (laughter) -- and were certainly better 
spellers.  We did not have spell-check back in my day.  You’re not only better educated, you’ve been more exposed to 
the world, more exposed to other cultures.  You’re more diverse.  You’re more environmentally conscious.  You have a 
healthy skepticism for conventional wisdom. So you’ve got the tools to lead us.  And precisely because I have so much 
confidence in you, I’m not going to spend the remainder of my time telling you exactly how you’re going to make the 
world better.  You’ll figure it out.  You’ll look at things with fresher eyes, unencumbered by the biases and blind 
spots and inertia and general crankiness of your parents and grandparents and old heads like me.  But I do have a 
couple of suggestions that you may find useful as you go out there and conquer the world. Point number one:  When you 
hear someone longing for the “good old days,” take it with a grain of salt.  (Laughter and applause.)  Take it with a 
grain of salt.  We live in a great nation and we are rightly proud of our history.  We are beneficiaries of the labor 
and the grit and the courage of generations who came before.  But I guess it's part of human nature, especially in 
times of change and uncertainty, to want to look backwards and long for some imaginary past when everything worked, 
and the economy hummed, and all politicians were wise, and every kid was well-mannered, and America pretty much did 
whatever it wanted around the world. Guess what.  It ain’t so.  (Laughter.)  The “good old days” weren’t that great.  
Yes, there have been some stretches in our history where the economy grew much faster, or when government ran more 
smoothly.  There were moments when, immediately after World War II, for example, or the end of the Cold War, 
when the world bent more easily to our will.  But those are sporadic, those moments, those episodes.  In fact, 
by almost every measure, America is better, and the world is better, than it was 50 years ago, or 30 years ago, 
or even eight years ago.  (Applause.) And by the way, I'm not -- set aside 150 years ago, pre-Civil War -- there’s a 
whole bunch of stuff there we could talk about.  Set aside life in the ‘50s, when women and people of color were 
systematically excluded from big chunks of American life.  Since I graduated, in 1983 -- which isn't that long ago -- 
(laughter) -- I'm just saying.  Since I graduated, crime rates, teenage pregnancy, the share of Americans living in 
poverty -- they’re all down.  The share of Americans with college educations have gone way up.  Our life expectancy 
has, as well.  Blacks and Latinos have risen up the ranks in business and politics.  (Applause.)  More women are in 
the workforce.  (Applause.)  They’re earning more money -- although it’s long past time that we passed laws to make 
sure that women are getting the same pay for the same work as men.  (Applause.) Meanwhile, in the eight years since 
most of you started high school, we’re also better off.  You and your fellow graduates are entering the job market 
with better prospects than any time since 2007.  Twenty million more Americans know the financial security of health 
insurance.  We’re less dependent on foreign oil.  We’ve doubled the production of clean energy.  We have cut the high 
school dropout rate.  We've cut the deficit by two-thirds.  Marriage equality is the law of the land.  (Applause.) 
And just as America is better, the world is better than when I graduated.  Since I graduated, an Iron Curtain fell, 
apartheid ended.  There’s more democracy.  We virtually eliminated certain diseases like polio.  We’ve cut extreme 
poverty drastically.  We've cut infant mortality by an enormous amount.  (Applause.) Now, I say all these things not 
to make you complacent.  We’ve got a bunch of big problems to solve.  But I say it to point out that change has been 
a constant in our history.  And the reason America is better is because we didn’t look backwards we didn’t fear the 
future.  We seized the future and made it our own.  And that’s exactly why it’s always been young people like you 
that have brought about big change -- because you don't fear the future. That leads me to my second point:  The world 
is more interconnected than ever before, and it’s becoming more connected every day.  Building walls won’t change 
that.  (Applause.) Look, as President, my first responsibility is always the security and prosperity of the United 
States.  And as citizens, we all rightly put our country first.  But if the past two decades have taught us anything, 
it’s that the biggest challenges we face cannot be solved in isolation.  (Applause.)  When overseas states start 
falling apart, they become breeding grounds for terrorists and ideologies of nihilism and despair that ultimately can 
reach our shores.  When developing countries don’t have functioning health systems, epidemics like Zika or Ebola can 
spread and threaten Americans, too.  And a wall won't stop that. (Applause.) If we want to close loopholes that allow 
large corporations and wealthy individuals to avoid paying their fair share of taxes, we’ve got to have the 
cooperation of other countries in a global financial system to help enforce financial laws.  The point is, 
to help ourselves we’ve got to help others -- (applause) -- not pull up the drawbridge and try to keep the world out. 
(Applause.) And engagement does not just mean deploying our military.  There are times where we must take military 
action to protect ourselves and our allies, and we are in awe of and we are grateful for the men and women who make 
up the finest fighting force the world has ever known.  (Applause.)  But I worry if we think that the entire burden 
of our engagement with the world is up to the 1 percent who serve in our military, and the rest of us can just sit 
back and do nothing.  They can't shoulder the entire burden.  And engagement means using all the levers of our 
national power, and rallying the world to take on our shared challenges. You look at something like trade, 
for example.  We live in an age of global supply chains, and cargo ships that crisscross oceans, and online commerce 
that can render borders obsolete.  And a lot of folks have legitimate concerns with the way globalization has 
progressed -- that's one of the changes that's been taking place -- jobs shipped overseas, trade deals that sometimes 
put workers and businesses at a disadvantage.  But the answer isn’t to stop trading with other countries.  In this 
global economy, that’s not even possible.  The answer is to do trade the right way, by negotiating with other 
countries so that they raise their labor standards and their environmental standards; and we make sure they don’t 
impose unfair tariffs on American goods or steal American intellectual property.  That’s how we make sure that 
international rules are consistent with our values -- including human rights.  And ultimately, that's how we help 
raise wages here in America.  That’s how we help our workers compete on a level playing field. Building walls won't 
do that. (Applause.)  It won't boost our economy, and it won’t enhance our security either.  Isolating or disparaging 
Muslims, suggesting that they should be treated differently when it comes to entering this country -- (applause) -- 
that is not just a betrayal of our values -- (applause) -- that's not just a betrayal of who we are, 
it would alienate the very communities at home and abroad who are our most important partners in the fight against 
violent extremism.   Suggesting that we can build an endless wall along our borders, and blame our challenges on 
immigrants -- that doesn’t just run counter to our history as the world’s melting pot; it contradicts the evidence 
that our growth and our innovation and our dynamism has always been spurred by our ability to attract strivers from 
every corner of the globe.  That's how we became America.  Why would we want to stop it now?  (Applause.) AUDIENCE 
MEMBER:  Four more years! THE PRESIDENT:  Can't do it.  (Laughter.) Which brings me to my third point:  Facts, 
evidence, reason, logic, an understanding of science -- these are good things.  (Applause.)  These are qualities you 
want in people making policy.  These are qualities you want to continue to cultivate in yourselves as citizens.  (
Applause.)  That might seem obvious. (Laughter.)  That's why we honor Bill Moyers or Dr. Burnell. We traditionally 
have valued those things.  But if you were listening to today’s political debate, you might wonder where this strain 
of anti-intellectualism came from.  (Applause.)  So, Class of 2016, let me be as clear as I can be.  In politics and 
in life, ignorance is not a virtue.  (Applause.)  It's not cool to not know what you're talking about.  (Applause.)  
That's not keeping it real, or telling it like it is.  (Laughter.)  That's not challenging political correctness.  
That's just not knowing what you're talking about.  (Applause.)  And yet, we've become confused about this. Look, 
our nation’s Founders -- Franklin, Madison, Hamilton, Jefferson -- they were born of the Enlightenment.  They sought 
to escape superstition, and sectarianism, and tribalism, and no-nothingness.  (Applause.)  They believed in rational 
thought and experimentation, and the capacity of informed citizens to master our own fates.  That is embedded in our 
constitutional design.  That spirit informed our inventors and our explorers, the Edisons and the Wright Brothers, 
and the George Washington Carvers and the Grace Hoppers, and the Norman Borlaugs and the Steve Jobses.  That's what 
built this country. And today, in every phone in one of your pockets -- (laughter) -- we have access to more 
information than at any time in human history, at a touch of a button.  But, ironically, the flood of information 
hasn’t made us more discerning of the truth. In some ways, it’s just made us more confident in our ignorance. (
Applause.)  We assume whatever is on the web must be true.  We search for sites that just reinforce our own 
predispositions. Opinions masquerade as facts.  The wildest conspiracy theories are taken for gospel. Now, 
understand, I am sure you’ve learned during your years of college -- and if not, you will learn soon -- that there 
are a whole lot of folks who are book smart and have no common sense.  (Applause.)  That's the truth.  You’ll meet 
them if you haven't already.  (Laughter.)  So the fact that they’ve got a fancy degree -- you got to talk to them to 
see whether they know what they’re talking about.  (Laughter.)  Qualities like kindness and compassion, honesty, 
hard work -- they often matter more than technical skills or know-how.  (Applause.) But when our leaders express a 
disdain for facts, when they’re not held accountable for repeating falsehoods and just making stuff up, while actual 
experts are dismissed as elitists, then we’ve got a problem.  (Applause.) You know, it's interesting that if we get 
sick, we actually want to make sure the doctors have gone to medical school, they know what they’re talking about.  (
Applause.)  If we get on a plane, we say we really want a pilot to be able to pilot the plane.  (Laughter.)  And yet, 
in our public lives, we certainly think, “I don't want somebody who’s done it before.”  (Laughter and applause.)  The 
rejection of facts, the rejection of reason and science -- that is the path to decline.  It calls to mind the words 
of Carl Sagan, who graduated high school here in New Jersey -- (applause) -- he said:  “We can judge our progress by 
the courage of our questions and the depths of our answers, our willingness to embrace what is true rather than what 
feels good.” The debate around climate change is a perfect example of this.  Now, I recognize it doesn’t feel like 
the planet is warmer right now.  (Laughter.)  I understand.  There was hail when I landed in Newark.  (Laughter.)  (
The wind starts blowing hard.)  (Laughter.)   But think about the climate change issue.  Every day, there are 
officials in high office with responsibilities who mock the overwhelming consensus of the world’s scientists that 
human activities and the release of carbon dioxide and methane and other substances are altering our climate in 
profound and dangerous ways. A while back, you may have seen a United States senator trotted out a snowball during a 
floor speech in the middle of winter as “proof” that the world was not warming.  (Laughter.)  I mean, listen, 
climate change is not something subject to political spin.  There is evidence.  There are facts.  We can see it 
happening right now.  (Applause.)  If we don’t act, if we don't follow through on the progress we made in Paris, 
the progress we've been making here at home, your generation will feel the brunt of this catastrophe. So it’s up to 
you to insist upon and shape an informed debate.  Imagine if Benjamin Franklin had seen that senator with the 
snowball, what he would think.  Imagine if your 5th grade science teacher had seen that.  (Laughter.)  He’d get a D.  
(Laughter.)  And he’s a senator!  (Laughter.) Look, I'm not suggesting that cold analysis and hard data are 
ultimately more important in life than passion, or faith, or love, or loyalty.  I am suggesting that those highest 
expressions of our humanity can only flourish when our economy functions well, and proposed budgets add up, 
and our environment is protected.  And to accomplish those things, to make collective decisions on behalf of a common 
good, we have to use our heads.  We have to agree that facts and evidence matter.  And we got to hold our leaders and 
ourselves accountable to know what the heck they’re talking about.  (Applause.) All right.  I only have two more 
points.  I know it's getting cold and you guys have to graduate.  (Laughter.)  Point four:  Have faith in democracy.  
Look, I know it’s not always pretty.   Really, I know.  (Laughter.)  I've been living it.  But it’s how, bit by bit, 
generation by generation, we have made progress in this nation.  That's how we banned child labor.  That's how we 
cleaned up our air and our water.  That's how we passed programs like Social Security and Medicare that lifted 
millions of seniors out of poverty.  (Applause.) None of these changes happened overnight.  They didn’t happen 
because some charismatic leader got everybody suddenly to agree on everything.  It didn’t happen because some massive 
political revolution occurred.  It actually happened over the course of years of advocacy, and organizing, 
and alliance-building, and deal-making, and the changing of public opinion.  It happened because ordinary Americans 
who cared participated in the political process. AUDIENCE MEMBER:  Because of you!  (Applause.) THE PRESIDENT:  Well, 
that's nice.  I mean, I helped, but -- (applause.) Look, if you want to change this country for the better, 
you better start participating.  I'll give you an example on a lot of people’s minds right now -- and that’s the 
growing inequality in our economy.  Over much of the last century, we’ve unleashed the strongest economic engine the 
world has ever seen, but over the past few decades, our economy has become more and more unequal.  The top 10 percent 
of earners now take in half of all income in the U.S.  In the past, it used to be a top CEO made 20 or 30 times the 
income of the average worker.  Today, it’s 300 times more.  And wages aren’t rising fast enough for millions of 
hardworking families. Now, if we want to reverse those trends, there are a bunch of policies that would make a real 
difference.  We can raise the minimum wage.  (Applause.)  We can modernize our infrastructure. We can invest in early 
childhood education.  We can make college more affordable.  (Applause.)  We can close tax loopholes on hedge fund 
managers and take that money and give tax breaks to help families with child care or retirement.  And if we did these 
things, then we’d help to restore the sense that hard work is rewarded and we could build an economy that truly works 
for everybody.  (Applause.) Now, the reason some of these things have not happened, even though the majority of 
people approve of them, is really simple. It's not because I wasn’t proposing them.  It wasn’t because the facts and 
the evidence showed they wouldn't work.  It was because a huge chunk of Americans, especially young people, 
do not vote. In 2014, voter turnout was the lowest since World War II.  Fewer than one in five young people showed up 
to vote -- 2014.  And the four who stayed home determined the course of this country just as much as the single one 
who voted.  Because apathy has consequences.  It determines who our Congress is.  It determines what policies they 
prioritize.  It even, for example, determines whether a really highly qualified Supreme Court nominee receives the 
courtesy of a hearing and a vote in the United States Senate.  (Applause.) And, yes, big money in politics is a huge 
problem.  We've got to reduce its influence.  Yes, special interests and lobbyists have disproportionate access to 
the corridors of power. But, contrary to what we hear sometimes from both the left as well as the right, the system 
isn’t as rigged as you think, and it certainly is not as hopeless as you think.  Politicians care about being 
elected, and they especially care about being reelected.  And if you vote and you elect a majority that represents 
your views, you will get what you want.  And if you opt out, or stop paying attention, you won’t.  It’s that simple. 
(Applause.)  It's not that complicated. Now, one of the reasons that people don’t vote is because they don’t see the 
changes they were looking for right away.  Well, guess what -- none of the great strides in our history happened 
right away.  It took Thurgood Marshall and the NAACP decades to win Brown v. Board of Education; and then another 
decade after that to secure the Civil Rights Act and the Voting Rights Act.  (Applause.)  And it took more time after 
that for it to start working.  It took a proud daughter of New Jersey, Alice Paul, years of organizing marches and 
hunger strikes and protests, and drafting hundreds of pieces of legislation, and writing letters and giving speeches, 
and working with congressional leaders before she and other suffragettes finally helped win women the right to vote.  
(Applause.) Each stage along the way required compromise.  Sometimes you took half a loaf.  You forged allies.  
Sometimes you lost on an issue, and then you came back to fight another day.  That’s how democracy works.  So you’ve 
got to be committed to participating not just if you get immediate gratification, but you got to be a citizen 
full-time, all the time. And if participation means voting, and it means compromise, and organizing and advocacy, 
it also means listening to those who don’t agree with you.  I know a couple years ago, folks on this campus got upset 
that Condoleezza Rice was supposed to speak at a commencement.  Now, I don't think it's a secret that I disagree with 
many of the foreign policies of Dr. Rice and the previous administration.  But the notion that this community or the 
country would be better served by not hearing from a former Secretary of State, or shutting out what she had to say 
-- I believe that’s misguided.  (Applause.)  I don't think that's how democracy works best, when we're not even 
willing to listen to each other.  (Applause.)  I believe that's misguided. If you disagree with somebody, bring them 
in -- (applause) -- and ask them tough questions.  Hold their feet to the fire.  Make them defend their positions.  (
Applause.)  If somebody has got a bad or offensive idea, prove it wrong.  Engage it.  Debate it.  Stand up for what 
you believe in.  (Applause.)  Don't be scared to take somebody on.  Don't feel like you got to shut your ears off 
because you're too fragile and somebody might offend your sensibilities.  Go at them if they’re not making any sense. 
Use your logic and reason and words.  And by doing so, you’ll strengthen your own position, and you’ll hone your 
arguments.  And maybe you’ll learn something and realize you don't know everything.  And you may have a new 
understanding not only about what your opponents believe but maybe what you believe.  Either way, you win.  And more 
importantly, our democracy wins.  (Applause.) So, anyway, all right.  That's it, Class of 2016 -- (laughter) -- a few 
suggestions on how you can change the world. Except maybe I've got one last suggestion.  (Applause.)  Just one.  And 
that is, gear yourself for the long haul.  Whatever path you choose -- business, nonprofits, government, education, 
health care, the arts -- whatever it is, you're going to have some setbacks.  You will deal occasionally with foolish 
people.  You will be frustrated.  You’ll have a boss that's not great.  You won’t always get everything you want -- 
at least not as fast as you want it.  So you have to stick with it.  You have to be persistent.  And success, 
however small, however incomplete, success is still success.  I always tell my daughters, you know, better is good.  
It may not be perfect, it may not be great, but it's good.  That's how progress happens -- in societies and in our 
own lives. So don’t lose hope if sometimes you hit a roadblock.  Don't lose hope in the face of naysayers.  And 
certainly don’t let resistance make you cynical.  Cynicism is so easy, and cynics don’t accomplish much.  As a friend 
of mine who happens to be from New Jersey, a guy named Bruce Springsteen, once sang -- (applause) -- “they spend 
their lives waiting for a moment that just don’t come.”  Don’t let that be you.  Don’t waste your time waiting. If 
you doubt you can make a difference, look at the impact some of your fellow graduates are already making.  Look at 
what Matthew is doing.  Look at somebody like Yasmin Ramadan, who began organizing anti-bullying assemblies when she 
was 10 years old to help kids handle bias and discrimination, and here at Rutgers, helped found the Muslim Public 
Relations Council to work with administrators and police to promote inclusion.  (Applause.) Look at somebody like 
Madison Little, who grew up dealing with some health issues, and started wondering what his care would have been like 
if he lived someplace else, and so, here at Rutgers, he took charge of a student nonprofit and worked with folks in 
Australia and Cambodia and Uganda to address the AIDS epidemic.  “Our generation has so much energy to adapt and 
impact the world,” he said.  “My peers give me a lot of hope that we’ll overcome the obstacles we face in society.” 
That's you!  Is it any wonder that I am optimistic?  Throughout our history, a new generation of Americans has 
reached up and bent the arc of history in the direction of more freedom, and more opportunity, and more justice.  
And, Class of 2016, it is your turn now -- (applause) -- to shape our nation’s destiny, as well as your own. So get 
to work.  Make sure the next 250 years are better than the last.  (Applause.) Good luck.  God bless you.  God bless 
this country we love.  Thank you.  (Applause.)"""

find_words(obama_speech)       # accesses 'find_words' function
sentence_length(obama_speech)  # uses sentence length function to count average words
longest_words(obama_speech)    # passes string into 'longest_words' function
