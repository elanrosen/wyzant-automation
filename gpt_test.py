# openai_client.py

from decouple import config
from openai import OpenAI


OPENAI_API_KEY = config('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

system_message = """"
        Here is a book (Kochland) that I read
        
Every year, in December, Charles Koch hosted a private party at his home. It was a
gathering for the elite group of Koch Industries employees who donated the
maximum legal amount of money to Koch Industries’ political action committee. As
the evening got underway, a parade of cars drove through the gates into the wooded
compound of Charles Koch’s childhood home. The attendees parked their cars in
neat rows on the spacious lawn and walked up the driveway through the winter wind
and into the warm, brightly lit entryway.
There was a cheerful cacophony inside, with about two hundred people milling
around in large rooms and hallways. The attendees were employees, executives, and
their spouses, dressed in their holiday best, eating heavy hors d’oeuvres from the trays
carried by uniformed waiters. Charles and David Koch held court in the living room,
sometimes standing side by side, as guests filed past to pay their respects. Charles was
courteous and smiling. But he also had a habit of managing the party like a company
meeting. When David Koch and a guest began talking at length about David’s art
collection, Charles Koch interrupted to remind the pair that there were guests
waiting behind them in the line. “Charles says, ‘David, you’ve got to move it along,’”
one guest recalled. “That’s kind of Charles. It’s kind of like ‘This is the process. We’re
greeting everybody. We’re having pleasantries.’ And then they move.”
There was a sense of exclusivity, of special belonging, that animated the people in
the room. The holiday party was held around the time of the annual board meeting,
so many board members and senior executives found time to attend. To receive an
invite, an employee needed to donate $5,000 during the year to Koch’s PAC. The
money was bundled and donated en masse to political candidates who were favored
by Koch’s PAC officials. It was understood that the PAC always needed donations
and that Charles Koch paid close attention to its performance. Having one’s name
listed in federal campaign disclosures was something akin to being listed in a country
club directory. It looked good. There was another, unspoken perk to donating: it
indicated that the employee in question had just finished a profitable year and had a
big bonus to show for it. When employees didn’t show up from one year to the next,
it created suspicion that maybe their bonuses hadn’t been so fat.
While the gathering was always festive, there was an air of tension hanging over the
party in 2009. The attendees had put lots of money into the PAC during the previous
election—a total of $2.6 million in 2008—and yet Barack Obama still won and
Democrats held large majorities in Congress. Virtually every political cause that Koch
Industries cherished was in retreat. The Republican Party seemed in danger of
becoming a permanent minority. The Libertarian Party didn’t even rate as a political
afterthought.
In the corner of Charles Koch’s living room, there was an elevated area that held a
bookcase, filled with collector’s editions of Charles Koch’s favorite thinkers, like
Hayek and von Mises. The collection seemed like a museum piece now, a collection
of antiques that were being left behind by the march of history. The guests stood in
clusters near the books, commiserating about the state of politics, the free-falling
markets, and waiting to hear what Charles Koch might say about itall.
Every year, Charles Koch made a short speech at the party. Sometimes he was
joined by Richard Fink, the top executive over Koch’s political operations. Charles
Koch’s speeches tended to be anodyne and courteous. He thanked the gathered
employees for their support and reminded them how vital it was to maintain
economic freedom in the United States, both for the long-term health of Koch
Industries and for the populace. In 2009, however, Charles Koch’s speech was
urgent. He felt that the future of America was imperiled. He thanked his guests for
their contributions, but the guests understood that the political fight was just
beginning.
One threat from the Obama administration seemed more dangerous than the rest.
It was the threat of a massive new regulatory regime to limit greenhouse gas emissions
that trapped heat in the Earth’s atmosphere. The threat of such had been slowly
building for decades, under both Republican and Democratic administrations.
Charles Koch fought against it the entire time. Now the threat appeared to be
imminent. While both Obama and his Republican opponent, Senator John McCain,
campaigned on a promise to limit uncontrolled carbon emissions, Obama made
carbon control a pillar of his platform. Since the very month Democrats took control
of Congress in 2006, they started working on a carbon-control regime. That effort
was well under way, with a proposed law working its way through Congress that was
more than a thousand pages long. With their wide majorities in the House and
Senate, Democrats were ready to hand the bill to a president who was eager to sign it.
There was a belief, within Koch Industries, that the carbon-control regime could
put the company out of business. It was impossible to overstate the stakes of the
coming fight. The bill in Congress sought to wholly reorganize America’s energy
system. If this happened, there was reason to believe that the world would follow
America’s lead. There were already two global treaties seeking to impose carbon limits
worldwide—one signed in Rio de Janeiro in 1992 and the other in Kyoto in 1997—
and the American regulatory regime could be quickly incorporated into this global
framework.
A carbon-control regime would expose Koch to a brand-new regulatory structure,
but it could also choke off decades of future profits as the world shifted away from
burning fossil fuels. Koch’s sunk investment in the fossil fuel business was measured
in billions of dollars, reflected in the value of its two oil refineries, pipelines, and other
assets. The future revenue to be derived from these assets arguably numbered in the
trillions of dollars in future decades.
In 1989, Charles Koch was caught unprepared when the US Senate investigated
oil theft on Indian reservations in Oklahoma. Charles Koch learned from the
experience. Things were very different in 2009. As recently as 1998, Koch Industries
spent as little as $200,000 a year on lobbyists in Washington, DC. By 2005, Koch was
spending $2.19 million. When the Democrats took over Congress in 2006, the
spending exploded, reaching $3.97 million in 2006, then $5.1 million in 2007. The
prospect of an Obama presidency intensified the effort. Koch Industries spent $20
million on lobbying in 2008. Koch augmented these lobbying expenditures with
campaign donations. In 1998, the Koch Industries PAC spent just over $800,000. In
2006 it spent $2 million. In 2008 it spent $2.6 million.
Even these expenditures didn’t come close to capturing the size of Charles Koch’s
political machine. Since at least 1974, Charles Koch had envisioned a political
influence machine that was multifaceted, including think tanks, university research
institutes, industry trade associations, and a parade of philanthropic institutions to
support it financially. The machine was areality now.
The think tanks and academic programs were funded through nonprofit
foundations such as the Charles G. Koch Charitable Foundation and the Claude R.
Lambe Charitable Foundation. In 2008 alone, the Charles Koch Foundation gave
out $8.39 million in grants and gifts, while the Lambe Foundation gave $2.56 million.
These grants supported conservative scholars and paid for supposedly independent
policy reports released by Washington think tanks. The libertarian Cato Institute
think tank, which Charles Koch cofounded and continued to support, operated with
annual revenue of $23.7 million in 2008, up from $17.6 million in 2001.
In later years, this political operation became known as the “Kochtopus,” a name
that evoked a many-tentacled entity that seemed to grasp every lever of policy making.
This nickname gave the Koch political apparatus an air of invincibility, as if it were an
unbeatable juggernaut with which Charles and David Koch could buy off politicians,
write policies, and tame the federal government to their wishes. This caricature failed
to recognize a central truth about the market for influence in Washington, DC: there
is no straight line between spending money and getting what you want. The market
for influence and policy outcomes was a murkier and more complex market than any
other in which Koch operated.
That night, at his home in Wichita, Charles Koch made it clear that he was
determined to win in this market, just as Koch Industries had won in so many others.
The survival of the company seemed at stake.
At that very moment, the biggest source of trouble for Koch Industries was asmall
group of dedicated liberal congressional staffers working long hours in an obscure
basement office in Washington. This team had been laboring for years to write the
thousand-page law controlling greenhouse gas emissions. The team was composed of
underpaid, overworked idealists. One of them was a workaholic named Jonathan
Phillips. Phillips didn’t know much about Charles Koch at that time. Which helps
explain why Phillips was still optimistic that history was on his side.
In a different world, Jonathan Phillips could have ended up as a Koch Industries
employee. He fit the Koch mold. He was entrepreneurial, idealistic, and thoroughly
midwestern. The first time he was old enough to vote for president, in 2000, he voted
for George W. Bush. Like so many Koch employees, he was trim and athletic. Phillips
had short blond hair, and his blue eyes projected an air of absolute sincerity when he
spoke.
Phillips might have become a perfectly respectable conservative if he hadn’t served
in the Peace Corps, which took him from the cozy confines of suburban Chicago to a
tent in Mongolia. He gained a broader view of the world and America’s role in it. He
lived amid extreme poverty and developed nuanced views about capitalism. He
watched from overseas as George Bush launched an invasion of Iraq that was
strategically disastrous and morally troubled. Phillips returned home from the Peace
Corps and tried to figure out how he could help make the world a better place. He
enrolled in the John F. Kennedy School of Government at Harvard and, after
graduation, got a job on Capitol Hill as a congressional staffer in the House of
Representatives. This is how Phillips found himself in the center of an effort to
redraw America’s energy system.
In the winter months of 2009, Phillips worked in the Longworth House Office
Building, a towering stone complex near the US Capitol. The hallways inside the
Longworth Building were austere and cold, lined with marble and capped with
vaulted ceilings. Every morning, Phillips walked past these grand corridors to a
stairwell that took him to the basement. Down there, the floors were made of
varnished cement and the ceiling was covered in exposed ducts, pipes, and vents.
Phillips walked to a set of doors that looked like they might conceal a utility closet.
This was the headquarters for the Select Committee on Energy Independence and
Global Warming.
The Committee on Global Warming was formed in 2007, one of Nancy Pelosi’s
first official acts after she became the Speaker of the House. Creating a select
committee sounds mundane, but it was actually a radical act of rebellion, at least in
congressional terms. To understand why, it’s important to understand the structure
of Congress.
It’s common to think of the US House of Representatives as a single organization
with 435 members who propose laws and then vote on them. In fact, the House is a
collection of smaller governing bodies, each with its own authority, called
committees. There’s a committee to write tax law and another to write environmental
law, for example. Each committee has a chairperson, who acts as the committee’s
CEO. Bills in the House are written by committees, then passed by a vote of the
committee members. This structure gives tremendous power to committee chairs,
and it explains why any bill to limit greenhouse gas emissions never had a chance of
passing.
The committee that oversaw climate change was the House Committee on Energy
and Commerce, which in 2007 was led by the Michigan Democrat John Dingell Jr.
Dingell had been chair of the committee, or the ranking Democrat on the committee,
since 1981, and he wasn’t friendly to any bills that might limit carbon emissions.
Dingell wasn’t just close to the Detroit automakers in his home state, he was the
Detroitautomakers, owning more than $500,000 worth of stock in the auto industry.
Rather than push Dingell to pass a climate change bill, Pelosi just went around
him and created the new House Committee on Global Warming and Climate
Change out of thin air and stowed it in the basement of the Longworth Building.
Dingell was less than enthusiastic. “These kinds of committees are as useful and
relevant as feathers on a fish,” he told a reporter. So Pelosi put the Massachusetts
congressman Ed Markey in charge of her new subcommittee. Markey was a
passionate advocate for environmental regulation, and from the very beginning,
Markey seemed dedicated to getting real results. He hired in the most talented staffers
he could find and he immediately set to work to break down the barriers that had
prevented climate change regulation for years.
Ed Markey built a team that resembled one of those motley groups of experts who
are drawn together to pull off a bank heist. There was Jon Phillips, an expert in
renewable-energy legislation. There was Joel Beauvais, a well-paid attorney and Clean
Air Act expert who took a horrific pay cut to help the committee write its carbon
control bill. There was Ana Unruh Cohen, a onetime congressional staffer who later
studied climate change policy for the Center for American Progress, a liberal think
tank. There was Michael Goo, a congressional staffer who seemed to know everyone
in the House. And there was Jeff Sharp, a onetime lobbyist and campaign worker
who specialized in communications. Everyone on the team knew that they were
overworked and underpaid. But they felt like they were part of something big. Lots of
people came to Washington to change the world. This committee was on the
precipice of actually doing it.
Almost immediately, the Committee on Global Warming started to agitate and
provoke virtually everyone in Congress. The committee didn’t have the authority to
pass bills, but it had the authority to hold hearings, which it began to do at a militant
pace. Phillips spent a great deal of his time booking hearing rooms and bringing in
experts to testify. Sharp, the communications guy, helped calibrate the hearings to
generate as much media attention as possible. Along with experts and politicians, the
committee began inviting celebrities to testify. Phillips met the actor Rob Lowe and
ushered him around the Capitol before Lowe testified ata hearing on electric cars.
“We were always looking for celebrities. We’re always looking for, like, tearful
stories,” Phillips recalled. “We’re always looking for ways to connect emotionally
with people to raise the profile of the issue. It’s as much a communications apparatus
as it is afact-finding mission.”
Jonathan Phillips and his teammates weren’t driven by the hunger for attention.
They were driven by a cause. They truly believed that the future existence of human
life on Earth was hanging in the balance. To understand their dedication to this
cause, it is useful to consider the story that the committee was trying to communicate
through its marathon series of hearings.
This was a story of an unprecedented geological event that was initiated by
humankind. It could be described as the detonation of a gigantic carbon bomb. The
essence of this story would become a contested battlefield in itself, with groups like
Koch Industries spending millions of dollars to sow doubt about the basic facts of the
matter and the broader meaning of those facts.
The fuse of the carbon bomb began to smolder sometime around the year 1800,
when industrialized cities started burning coal to heat homes and power primitive
engines. In 1850, about 198 million tons of carbon were released into the
atmosphere.
Carbon is a curiously durable element. It can float in the sky for thousands of
years without breaking down. Carbon has another important characteristic—it is
translucent. That means that it blocks sunlight, just slightly, like a veil of smoke. This
translucence is vitally important to life on Earth. A thin layer of compounds like
carbon dioxide and water vapor in the atmosphere act like a shield, retaining some of
the sun’s warmth on the surface of the planet. The mechanics of how this works are
simple and well understood. About two-thirds of the sun’s heat hits the Earth, but
then bounces off into space. The remaining third of the heat is kept on Earth because
the thin layer of translucent elements trap it there. For about the past four hundred
thousand years, carbon levels in the atmosphere bounced around in a very narrow
band, between roughly 200 and 400 parts per million. This period of relative climate
stability coincided with the rise of agriculture and the development of civilization.
The fuse of the carbon bomb was truly lit in 1859, when Edwin Drake hit his
gusher of an oil well in Pennsylvania and began the age of oil in America. When a
barrel of crude oil was burned, it released about 317 kilograms of invisible carbon
dioxide into the air. In 1890, 1.3 billion tons of carbon were released into the sky.
Some of it went back into the trees, some of it went into the oceans, but some of it
stayed in the atmosphere. In 1930, 3.86 billion tons of carbon were released into the
atmosphere. In 1970, 14.53 billion tons of carbon were released into the atmosphere.
It was joined by other industrial gases that wafted up from factories, refineries,
feedlots, and fertilizer plants, gases like methane and nitrous oxide that were also
invisible and seemingly harmless. Some of these gases blocked far more light than
carbon, on the order of thirty to fifty times more. As more of these gases were released
into the atmosphere, more heat would be trapped. This is incontrovertible.
In the 1950s, a chemist and oceanographer named Charles David Keeling installed
an air monitor on top of Mauna Loa volcano in Hawaii. Its measurements showed
that carbon was accumulating in the atmosphere. In 1959, carbon composed 316
parts per million in the atmosphere. In 1970, it composed 325 parts per million. In
1990, it was 354 parts per million. Concurrent with this discovery, scientists tested air
samples that were trapped in tiny bubbles in the glaciers of Antarctica. This proved
that during the early millennia of human existence, carbon levels remained in the
narrow band between roughly 200 and 300 parts per million. Now that carbon levels
exceeded that threshold, it raised troubling questions: What would the world’s
climate be like at 360 parts per million? Or at 380? Or at 400? There was no certain
answer.
In 1988, a group of scientists working with the United Nations formed a
consortium called the Intergovernmental Panel on Climate Change, or IPCC, which
set out to synthesize the research on global climate change occurring around the
world. Initially, the IPCC was very cautious and even seemed to downplay the
potential risks from higher carbon concentrations. The panel said that more study
was needed, and that no rash actions should be taken that might dampen the
prosperity that came from burning fossil fuels. Each ensuing IPCC report, however,
became more certain than the last. Carbon concentrations were increasing, which
inevitably trapped more heat in the atmosphere. Humans were responsible for the
increase. The future implications were unpredictable, but could be severe. The world
could expect more dramatic rainfall events and bigger storms in part because warmer
air held more moisture. Areas that were parched would become drier. Weather data
showed that the world was already getting warmer, as would be predicted when
greenhouse gases increased.
While the scientific community was in agreement on these facts, the American
public was in doubt. This wasn’taccidental. As early as 1991, Charles Koch and other
executives in the fossil fuel industry helped foster skepticism about the evidence of
climate change. When George H. W. Bush announced that he would support a treaty
to limit carbon emissions, the Cato Institute held a seminar in Washington called
“Global Environmental Crises: Science or Politics?”
The seminar featured scientists who questioned the prevailing view that
humankind’s carbon emissions caused the Earth to warm, including Richard S.
Lindzen, a professor of meteorology at MIT, Charles Koch’s alma mater. A brochure
for the seminar featured a large-print quote from Lindzen in which he said: “The
notion that global warming is a fact and will be catastrophic is drilled into people to
the point where it seems surprising that anyone would question it, and yet,
underlying it is very little evidence atall.”
The seminar was not a fringe event. Lindzen and other speakers at the conference
were invited to join White House staffers in the Roosevelt Room while they were in
town for the conference, according to an internal White House memo from Nancy
G. Maynard, who worked for the president’s Office of Science and Technology
Policy. Maynard’s boss forwarded the invitation to Bush’s chief of staff, John H.
Sununu, under the subject line “Alternative Perspectives on Global Warming.”
Koch Industries, ExxonMobil, and other firms spent millions of dollars to support
the idea that there was an “alternative” view about climate change between 1991 and
2009. These groups had a distinct advantage in the debate. It took many decades for
firm scientific consensus to take shape. Scientists are, by nature, cautious and selfdoubting. They were hesitant to push the narrative further than the data would
support. And the mechanisms of climate change were impossibly complex and hard
to quantify. It was difficult to estimate, for example, just how much carbon the
world’s oceans might be able to absorb over time, or exactly how many degrees the
earth might warm over a hundred years if the atmospheric levels of carbon reached
400 parts per million. Even as the global scientific community slowly cohered around
the understanding that human activity caused climate change, this cottage industry
thrived—a cottage industry built to highlight all the points of uncertainty in the
scientific debate.
ExxonMobil eventually abandoned this strategy, but Koch Industries persevered.
In 2014, Koch Industries’ top lobbyist, Philip Ellender, said that the evidence was in
doubt. “I’m not a, you know, climatologist or whatever,” Ellender said. “Over the
past, I think, hundred years, the earth is warmer. Over the past roughly eighteen, it’s
cooler.
I
. . . Whether or not the increases and fluctuations are anthropologic or not is
still a question.”
In private, Koch Industries officials were even more dismissive of the science
around climate change. One former senior Koch Industries executive, a trained
scientist who only made business decisions after first analyzing reams of data,
explained that he believed global warming was a hoax invented by liberal politicians
who sought to use the fiction as a way to unite the populace against an invented
enemy. After the fall of the Soviet Empire in 1991, this executive explained, American
elites needed a new, all-encompassing enemy with which to frighten the masses, and
so they invented one with global warming. All the data on atmospheric carbon levels
and rising temperatures were part of this conspiracy, the executive said.
This is what lent the sense of desperation to Phillips and his team, as they
conducted their series of hearings on climate change. Phillips and his colleagues were
painfully aware of the data underpinning climate change. They spent their days
reading the scientific research about global climate change, and they felt like they had
a window into a terrible truth that most people needed to see. This was the reason
behind the parade of hearings and the celebrity appearances that they held on Capitol
Hill. Their desperation derived from the fact that no one seemed to be listening.
When Markey’s committee realized that hearings alone weren’t changing the political
dynamic, they took a more provocative step. They wrote a bill of their own. The
Select Committee couldn’t pass the bill or even introduce it for a vote. But the team
knew that the mere existence of a bill would make the issue all the harder to ignore.
The shape of the bill reflected the politics of the time. There were many ways that
the government could stanch greenhouse gas emissions. Congress could tax carbon
emissions, incentivizing companies to use lower-carbon sources of energy. Or
Congress could regulate carbon like a pollutant, setting strict limits on its release.
Rather than take these straightforward approaches, the committee settled on a
complicated, far-reaching regulatory structure that embodied the internal paradoxes
of the neoliberal philosophy that dominated policy making from the Clinton
administration onward. The bill sought to dramatically expand the reach of
government, while harnessing the power of private markets. In this case, the approach
was called cap and trade.
There was surprisingly little dissent within the committee against this approach.
“Very early on, people got the sense that this is going to be a cap-and-trade bill,”
Phillips recalled. “The think tanks in town and everyone in the talking head
community—no one was talking about a carbon tax. Everyone was talking about cap
and trade as being the vehicle. At that time, there was sort of this consensus that it
was the moderate, most economically efficient way of dealing with pollution.”
Phillips said it was also attractive because it had the advantage of enjoying
bipartisan support. “It was a Republican idea,” he said.
The cap-and-trade policy was made famous under President George H. W. Bush,
who used it as a way to combat acid rain. The concept was simple. The government
capped the total amount of a certain pollutant that could be released. But then it gave
companies a license to release that pollution. A company could pollute as much as it
desired, but it paid the price to do so by purchasing pollution “credits.” If a company
cut the amount of pollution it released, it could earn credits for doing so and turn
around and sell them. This created a “market” for pollution. Polluters paid to pollute,
companies earned money by cutting pollution. All the while, government determined
how much total pollution was allowed by setting the cap. The government could
turn the screws and push the caps downward, making a stronger and stronger
incentive to cut emissions.
Cap-and-trade gained support after Bush imposed it on power plants that released
sulfur dioxide, which created acid rain. By 2008, emissions were 60 percent lower
than they had been in 1980. More importantly, the cuts were made at much lower
costs than people had predicted. The cap and trade system on sulfur dioxide was
imposed in 1990.
With their bill, the Markey committee aimed to create the largest cap-and-trade
system in history. The limit on greenhouse emissions affected virtually every corner
of the modern economy, from automobiles, to power plants, to factories. The policy
mechanisms to do so, laid out in the bill’s thousand pages, were almost impossibly
complex.
Ed Markey unveiled the bill in May of 2008, giving it the consumer-friendly name
of “iCAP.” After Obama became president, Nancy Pelosi became emboldened. She
helped initiate a coup in the Energy and Commerce Committee. A usually
perfunctory vote on the chairmanship went against Dingell. He was replaced by the
California liberal Henry Waxman, who vowed to pass a law to control carbon
emissions. Ed Markey and his committee, after years of agitating from their basement
office, were now in a position to do more than agitate. They were in a position to
govern. They had opened a pathway to push their bill through Waxman’s committee.
The iCAP bill was put on the legislative operating table in 2009 and opened back
up. It would become known as the Waxman-Markey bill, an ambitious cap-and-trade
system that quickly became a centerpiece of Obama’s legislative agenda. The bill had
been in the works for years and had been the subject of hundreds of hours of
congressional hearings. In the early days of the Obama era, even more hearings were
held. The select committee worked even harder as it drafted new language and met
with members of Congress and lobbyists from the energy companies and
environmental groups.
The long days of grinding work in the basement office were thrilling, in a way, for
Phillips. He had the sense that he was a part of history. And he wasn’t the only one.
At night, Phillips and his friends went out to drink at cheap bars. They must have felt
something like the young staffers back in the 1930s, when the mighty legislative
pillars of the New Deal were being put into place. They were laying the governing
framework of future generations.
They were part of the strongest governing coalition in years, or perhaps decades.
An acquaintance of Phillips’s, a young speechwriter named Dylan Loewe, wrote a
book during that time entitled Permanently Blue: How Democrats Can End the
Republican Party and Rule the Next Generation. Galley copies were passed around
Washington. People read Loewe’s prediction that the Democratic Party was in a
position to hold the White House and Congress for the next quarter century, and this
prediction seemed entirely believable. The Republicans had been reduced to a
factional minority with no clear path back to power. The Democratic Party had the
force of history at its back, pushing it forward.
Koch Industries’ lobbying office was located on the eighth floor of a majestic stone
building two blocks from the White House. In early 2009, David Hoffmann—the
environmental attorney who’d helped impose Koch’s “10,000 percent compliance”
doctrine at Invista’s factories—was still relatively new to Washington, DC. After
working for several years in Wichita, he requested a transfer to Washington in 2007
so that he and his wife could enjoy more big-city culture. He moved into an office at
Koch’s lobbying shop, even though he was still a compliance attorney. If Hoffmann
sympathized with certain elements of the Obama revolution, he also saw the ugly side
of the federal government—the complex bureaucracy, and the overbearing
paperwork to comply with environmental laws. The Clean Air Act, he said, was a
prime example. To comply with the law, there are “literally thousands of items that
you need to go over to determine compliance. It takes a full-time staff, working
around the clock, to get some of these compliance reviews completed.”
Even though he wasn’t a lobbyist, Hoffmann helped his peers in Koch’s public
affairs division by lending his expertise on compliance matters. That’s why he got
dragged into the largest lobbying fight Koch had ever waged, against the cap-andtrade bill that Phillips and his team were then constructing.
Before 2008, Koch’s lobbying efforts had been fragmented. There was a team of
lobbyists working for Invista, one for Georgia-Pacific, and another for the oil refining
division, Flint Hills Resources. This fragmentation reflected Koch’s commitment to
maintain its corporate veil, organizing its various divisions under a legal structure that
categorized each division as an independent business. This structure helped Koch
contain its legal liabilities, but it also hobbled its corporate lobbying efforts. Because
Invista and Flint Hills didn’t coordinate closely, they might be duplicating their
efforts or sending mixed messages to lawmakers. In 2008, Koch Industries
consolidated its lobbying operations into a single, newly formed company called
Koch Companies Public Sector. Now all of Koch’s lobbyists worked side by side,
sharing information and strategies as they worked toward common goals.
Hoffmann led an internal committee at Koch, studying how the company might
not only adapt to a cap-and-trade regulatory scheme but how it might prosper from
it. He came to this role almost accidentally. The newspapers were full of stories about
the Waxman-Markey bill. Hoffmann knew that if the law passed, it would instantly
become the most significant law that he and his compliance team at Invista would
need to contend with. He formed the committee to study the issue. He thought that
Invista might find novel ways to comply with the law that could be copied by other
divisions at Koch Industries. He was steeped in the ways of Market-Based
Management and believed that adapting to a cap-and-trade regime fit perfectly within
the MBM framework. “Charles Koch wants to empower his employees to project
where industry is going,” Hoffmann said. “We felt like we were doing exactly what
the Koch philosophy meant to us. Which is: hope for the best but prepare for the
worst.”
Hoffmann enlisted a handful of fellow Invista employees to help him. He
consulted with Koch’s lobbyists. And he quickly realized that there was reason to be
optimistic about Koch’s future in a cap-and-trade world—or at least there was reason
to be optimistic about Invista’s. Invista was already making investments that cut its
carbon output. The company was refitting older factories with new furnaces, for
example, fired by natural gas rather than coal. Such efforts saved money and increased
efficiency, but they could also be transformed into carbon credits that Invista could
sell. Koch Industries also operated smaller divisions that made pollution-control
equipment. If cap and trade passed, those divisions could see a boost in business.
Hoffmann labored under the assumption that some sort of cap-and-trade bill was
inevitable. What he didn’t know then was that he held the minority opinion within
Koch’s lobbying office.
Every Monday morning, Koch’s team of lobbyists gathered in a large meeting room
just down the hallway from the office’s main reception area. As the lobbyists filed in
for their weekly meeting, they took their seats around a large wooden table in the
center of the room. The table was set with thick leather coasters with the Koch
Industries logo embossed on them. Other than that, the decorations were spartan. A
pad of white paper stood on a tripod near the window, on which to write ideas and
sketch out strategies. The only artistic adornment in the room was a small metal
sculpture on the shelf of a lumberjack, an apparent homage to Georgia-Pacific and its
past workforce.
The weekly meeting was led by Koch’s top lobbyist, Philip Ellender. He didn’t
share the habits of a typical lobbyist. He lived in Atlanta, working out of Koch’s
offices there, and commuted to DC by airplane. While most lobbyists arrived for
work around nine thirty or ten in the morning after spending late nights at dinner
parties, Ellender operated on Wichita time. He arrived early and spoke frequently on
the phone with colleagues in Kansas. He was also a true believer in Charles Koch’s
philosophy. “We’re a bit philosophically more pure,” Ellender explained, “in that we
recognize that we are unabashedly free traders, that we believe in profiting by the
economic, not political, means. We’re against cronyism. We’re against subsidies.
We’re against mandates.” He peppered his speech with the vocabulary of MarketBased Management.
As Koch Industries became more politically influential, it became increasingly
insistent that its lobbyists were pursuing a purely ideological mission. Koch’s
lobbyists and public relations teams said their goal wasn’t to boost Koch Industries’
profits, but to champion the ideas of freedom and prosperity. Ellender and others
were quick to highlight the times when Koch lobbied against subsidies or tax breaks
that might benefit the company. Still, Ellender and his team focused overwhelmingly
on the issues that did matter to Koch’s business, such as arcane rules about chemical
safety, rate billing, and taxes on oil companies. Koch Industries also accepted the
subsidies and tax breaks that were in place for it—Ellender said that refusing to do so
would put Koch atan unacceptable disadvantage to its competitors.
For all the talk about ideological purity, Ellender’s operation reflected a more
complicated reality. The lobbying business didn’t operate along clean partisan lines.
There was a cartoonish image of a Washington lobbyist that most Americans held in
their mind—the image of a well-dressed influence peddler who took politicians out to
expensive dinners and cocktail cruises on the Potomac River. With enough steak
dinners, enough cruises, and enough campaign contributions, the thinking went, any
politician eventually succumbed to the lobbyist’s wishes. If this view of lobbying was
ever accurate, it was certainly irrelevant by 2009. The reason for this was structural:
the number of corporate lobbyists had exploded over the previous thirty years.
Thousands of lobbyists were trying to push their message, but the messages could
only be received by a very narrow audience. There were only 435 members of the
House of Representatives and 100 members of the Senate, a total of 535 channels
into which all of America’s special interests were forced to funnel their message.
The competition for those channels was more intense with each election cycle. In
1983, groups seeking to influence Washington policy spent about $200 million. By
2002, these groups—including corporations, labor unions, and advocacy groups
representing retirees or environmental activists—spent $1.82 billion on lobbying, a
sevenfold increase. By 2010, spending on lobbying had nearly doubled again to $3.55
billion. And this figure captured only a share of all lobbying expenditures—the share
that was reported under public disclosure laws, which didn’t account for campaign
contributions or issue-related advertising.
The rise in lobbying spending was not spread evenly across interest groups.
Corporations and business groups far outspent other interests, like labor unions and
consumer advocates. By 2012, corporations, trade associations, and businesswide
associations were responsible for 78 percent of all lobbying expenditures, according
to an analysis by the political scientist Lee Drutman. Business interests outspent other
interest groups by aratio of 22 to 1 in 1998, and 35 to 1 in 2008, Drutman found.
Even within these ranks of big corporate spenders, Koch Industries stood apart.
The biggest corporations far outspent everyone else. About 90 percent of all US
corporations did not even have one full-time lobbyist, and were only represented
through trade associations. The biggest companies, like Koch, had a significant
advantage.
In this environment, the primary job of Koch’s lobbyists was to gather and analyze
information. Inside information was perhaps even more important in the market for
influence than it was in the market for crude oil. Congress was an impossibly opaque
system, a complex pipeline network of policy ideas that flowed between 535 offices in
the House and Senate. Minute-by-minute updates on the inner workings of Congress
were extraordinarily valuable, and out of reach for most companies. Koch’s lobbyists,
like most other corporate lobbyists, spent their time gathering detailed intelligence.
They determined which bills were originating from which offices, which bills had
momentum and which didn’t, which politician needed help with a campaign and
where that politician stood on issues that were important to Koch. This need for
inside information explains why so many lobbyists are former congressional staffers.
The former staffers have personal relationships with lawmakers and their staffers.
They know which bills will be debated and moved forward through the system. A
lobbyist’s value comes just as much from knowing about this process as it does from
being able to influence it.
Ellender’s team was small, considering the size of their job. Koch Companies
Public Sector had only five full-time registered lobbyists in 2009. The defense
contractor Lockheed Martin, by contrast, had an in-house team of thirty lobbyists
that year.
Ellender’s permanent team of lobbyists knew a great deal about Republicans in
the House and Senate. Koch Industries had given generously to Republican
candidates and conservative causes over the years—in the 2008 election cycle, Koch
Industries gave $1 million to Republicans and just $186,500 to Democrats.
When Ellender and his team met in 2009, they needed to figure out a way to learn
more about the newly empowered Democrats. This might seem like an impossible
task for Koch’s small cadre of lobbyists—the entire Koch team could fit around the
conference table, with chairs to spare. But their lobbying power was bigger than their
numbers might suggest. Each Koch lobbyist was like the regional manager of a
franchise. They built expertise on certain policy issues, like climate change legislation
or derivatives trading, and they had the ability to hire contractors from outside firms
if they needed to beef up staff. This allowed Koch to build up or reduce its expertise
on different topics as they arose in Congress. Sometimes, the outside contractors
joined Koch’s team for its Monday meetings.
One of the lobbyists at Ellender’s meeting table was a woman named Kelly Bingel,
a contractor with Mehlman Vogel Castagnetti, a bipartisan lobbying shop. Firms like
Mehlman Vogel were a shock absorber that protected corporations from populist
passion. When conservatives took over Congress, Mehlman Vogel hired out its
Republican lobbyists to help negotiate the new environment. When liberals took
over, Mehlman Vogel hired out its Democrats.
Koch Industries first retained Mehlman Vogel in 2007, when Democrats gained
control of Congress, paying the firm $10,000 a month through 2008. By the end of
2009, Koch was paying the firm $20,000 a month and retaining thirteen of its
lobbyists, including Bingel. She was a former staffer for Senator Blanche Lincoln, the
Arkansas Democrat, and was on a first-name basis with many Democratic senators
and staffers.
Bingel was part of a hidden political movement in 2009 that could be called
“Democrats for Koch Industries.” She spent time hanging around the cheap
congressional cafeterias, like the one in the basement near Jonathan Phillips’s office.
When Bingel saw a staffer she knew, she sat down and traded gossip. She spent time
on the phone, collecting tips. When her staffer friends wanted to get out of the office,
Bingel took them out to lunch. Bingel became a liaison between Koch Industries and
the liberal politicians whom the company had spurned for so many years. “My job
was to introduce them to Democrats,” she said.
There were two ways for a lobbyist like Bingel to get the attention of a politician.
The first was to work for that politician and remain close to their staffers after
leaving, as Bingel had done. The second way was to raise money for the politician.
This is why lobbyists frequently host fund-raising lunches, banquet dinners, and
other events. The issue of fund-raising had to be treated delicately. Bribery is illegal in
the United States. If a lobbyist offered money to a legislator in return for a vote, then
both people could end up in prison.
To compensate for this fact, an elaborate system of etiquette had taken root in
Washington. A lobbyist showed up, made an impassioned pitch to a legislator, and
then left. Later, the lobbyist called the legislator’s office to say how thrilled the
lobbyist would be to hold a fund-raising dinner for the legislator. If the lobbyists
mentioned fund-raising in the middle of a pitch meeting, it would be akin to going
shirtless to aformal dinner. Everyone in the room would be shocked.
When Bingel brought her colleagues from Koch Industries to meet Democratic
politicians, they followed the well-honed lobbyist playbook. They focused on three
factors that could sway the legislator’s thinking. The factors were:
1. The Preferences of a Legislator’s Voters. This was the most important factor
to a lawmaker. A legislator cares, more than anything, about winning the next
election. They seek to stay safely within the zone of voter approval.
2. The Broader Political Impact of the Vote. Because every legislator belongs to a
political party, they also obsess about their standing within the party and their
political future. A good lobbyist points out how any given vote fits into the party’s
goals.
3. The Personal Convictions and Idiosyncrasies of the Legislator. This was the
most frustrating and mostambiguous factor. Legislators are only people, at the end of
the day. Most of them ran for office for deeply personal, and sometimes irrational,
reasons. It could not be overestimated how profoundly these personal motivations
play into a legislator’s votes. Good lobbyists were intimately familiar with a
lawmaker’s personal quirks and convictions.
During a typical meeting with a lawmaker, a Koch Industries lobbyist pulled all
these levers of influence. To pull the first lever, the lobbyist highlighted the deep ties
that Koch Industries held with the legislator’s voters by listing the jobs that Koch
provided in the state or congressional district in question. To pull the second lever,
the lobbyist might talk about legislative issues that were important to the lawmaker’s
party. What was left unsaid, but understood among everyone in the room, was the
sizable volume of Koch’s political donations, which could help any politician’s
standing in their party. Finally, the good lobbyist catered to a lawmaker’s personal
quirks, talking about a given issue in terms of keeping taxes fair in one office, and
talking about the same issue in terms of infrastructure investment in another.
Bingel and the other Democrats for Koch helped the company understand the
intricate power dynamics within the Democratic majority in Congress. It was clear
that most Democrats in the House felt empowered to push the Obama agenda. But
talking with staffers in the cafeterias yielded important insights about it. Obama’s
chief of staff, the former congressman Rahm Emanuel, wanted Obama to push his
agenda in three phases, with three major bills that would pass through the House and
Senate like train cars in a row. First would be health care reform, second would be
financial industry reform, and third would be climate change legislation. This was
useful to Koch Industries, ExxonMobil, and other fossil fuel companies that wanted
to derail the carbon control efforts. If the climate change bill was the caboose of the
legislative train, then the opponents had more time to mountafightagainst it.
As they worked through their long Monday morning meetings and sketched ideas
on the white notepad, Koch Industries’ lobbyists crafted a plan to do just that.
David Hoffmann worked for months on his study that explored how Koch
Industries might adapt its business to a cap-and-trade bill. He was excited by his
findings. Hoffmann’s committee discovered opportunities for Koch to make money
in a market for carbon emissions. Invista released huge amounts of nitrous oxide into
the air, a chemical that trapped heat at a magnitude of 290 times greater than carbon
dioxide. If Invista cut its nitrous oxide emissions, it could reap extremely valuable
carbon emission credits. The future under cap-and-trade might not be entirely bleak.
In spite of these findings, Hoffmann wasn’t sure that anyone at Koch was
interested in his committee’s work. It seemed like his reports and updates were being
ignored. Hoffmann realized why after he was invited to attend a senior-level meeting
of Koch’s lobbying operation. The topics of the meeting were EPA enforcement of
the Clean Air Actand the Waxman-Markey cap-and-trade bill.
The meeting convened in the same conference room where Koch’s lobbyists held
their Monday-morning strategy sessions. Hoffmann didn’t usually attend such
meetings, but was apparently invited to this one because of his role as an
environmental compliance attorney. The first part of the meeting dealt largely with a
new push by the EPA to strengthen air emission rules. Philip Ellender led the
meeting, but the session was attended by some of the most senior people in Koch’s
political operation.
This included Richard Fink, who was second only to Charles Koch in the political
shop. Fink had a hand in virtually all the facets of Koch’s political influence
operations, from the Cato Institute think tank, to the academic studies at George
Mason University, to the registered lobbyists. Only a handful of people knew about
the inner workings of all these groups, and Fink was one of them.
Also at the meeting was Laurie Sahatjian,
II one of Koch’s most senior attorneys,
who specialized in environmental compliance. She was joined by Don Clay, a former
EPA official who had worked for Koch’s lobbying office since the 1990s.
Before he sat down in the conference room, Hoffmann believed that Koch’s
approach to the Waxman-Markey bill might be to mitigate its effects on the
company, as he was trying to do. As the discussion got under way, he realized his
opinion was in the minority.
When the meeting turned to the cap-and-trade bill, the discussion began with
some banter and small talk. Most of the attendees let it be known that they thought
climate change was “a hoax,” Hoffmann recalled. This was difficult for him to
absorb. The people in the room were very intelligent. Many of them had an almost
encyclopedic knowledge of the emissions released from Koch’s factories and refineries
and how those emissions interacted with the Earth’s atmosphere. The science of
global warming was not fundamentally complex: carbon trapped heat in the
atmosphere, more carbon trapped more heat, and humans were releasing
unprecedented amounts of carbon into the sky.
But Hoffmann realized that most of the people in the meeting doubted the
underlying problem that Waxman-Markey sought to address. If global warming
wasn’t real, then there was no justification for the law to exist. The feeling in the
room was that the Waxman-Markey bill posed an existential threat to Koch
Industries. Koch’s lobbying team was particularly aggrieved by the bill because it
seemed as if the law was specifically targeting oil refineries in an effort to replace them
with wind farms and solar panels.
Koch’s lobbyists circulated a pie chart that seemed to prove their case. It
highlighted a complicated provision of the cap-and-trade law that was seemingly
being weaponized against Koch. The provision in question was the so-called carbon
allotment. In essence, when the cap-and-trade law took effect, the government would
instantly distribute allotments to the private sector that allowed companies to release
a certain amount of greenhouse gases into the atmosphere. These allotments were the
starting point of the carbon trading market; after a company used all its allotments, it
would be forced to pay money for all the additional carbon it released.
Under the proposed law, roughly $1 trillion worth of carbon allotments would be
allocated in the beginning. The biggest share of the allotments, totaling about 37
percent, would be handed out to electrical utility companies. The theory behind
giving so many allotments to utilities was that it would ultimately ease the regulatory
burden on most consumers, who didn’t have a choice but to use electricity. The oil
refineries, by contrast, would receive just 1.7 percent of the allotments. This tiny
sliver of allotments was barely visible in the pie chart that Koch’s lobbyists were
circulating. Even Hoffmann was swayed by this graphic presentation.
“It was pretty clear that Congress was targeting the refinery industry,” he said. “It
did seem starkly unfair.”
There was even more for Koch to worry about. The government could ratchet
down the allotments over time, squeezing the refineries even harder. It looked like a
plan to make oil refining athing of the past.
As it happened, the carbon allotment provision of the Waxman-Markey law was
written by Jonathan Phillips, the twenty-nine-year-old congressional aide who was
toiling away in the basement of the Longworth Building. Phillips had no idea that he
had just become Koch Industries’ chief antagonist. He was too busy working.
During the spring of 2009, the long-held liberal dream of passing a cap-and-trade bill
was starting to look like a reality. Henry Waxman was in charge of the House Energy
Committee, Ed Markey was lobbying his fellow Congress members, and President
Obama was speaking in favor of its passage. The Committee on Global Warming
spent years provoking Congress into action, and now that action was here. Phillips
and his coworkers knew that they had one chance to get it right.
Phillips was asked to write a significant portion of the bill that would create a
mandate to spur energy production from renewable sources like wind turbines and
solar panels. Creating an economically transformational law wasn’t nearly so hard in
2009 as it had been in the early 1930s, when Franklin Roosevelt’s administration laid
the groundwork for the New Deal. The basic policy machinery of the New Deal was
still in place, which created a self-propelling momentum to increasing federal power.
As Phillips and his colleagues sought to construct a cap-and-trade system, all they had
to do was tweak the massive legislative structure that was already in place. The entire
Waxman-Markey law, in fact, was really just an amendment of the Clean Air Act, the
Federal Power Act, and other existing laws. It wasn’t even necessary to create a new
federal agency to implement the law. The carbon cap could be imposed and policed
by the EPA, and the renewable-energy mandate could be imposed by the Federal
Energy Regulatory Commission, for example.
This was, in short, Charles Koch’s worst nightmare. As the government became
more powerful, it became easier to expand those powers.
The technical aspects of the bill were mostly settled by early 2009. Phillips and his
colleagues were now working on another aspect of the bill: its politics. They needed
to win support from a majority of Democrats, which was problematic. One
inarguable fact about the cap-and-trade bill is that it would put a price on carbon and
thereby increase energy prices, at least in the near term. Oil prices would go up. Coal
prices would go up. Electricity bills would go up. Congress members knew that
supporting the bill would draw relentless political attacks when higher energy costs
were realized. It was true that stemming carbon emissions might mitigate an eventual
climate disaster, but this wouldn’t help a congressman get reelected in two years’
time.
Phillips and his colleagues needed something more than an argument to persuade
hesitant Democrats. Luckily, they did have something: an immense pot of money
called carbon emission allotments. When a cap was put on carbon, the right to
pollute with greenhouse gases would instantly be worth at least billions of dollars.
And the government would possess a newly invented piggy bank from which it could
disburse the money.
Based in part on observations of carbon trading markets in Europe, most experts
estimated that the price of carbon would float around $13 to $15 a ton in the first
years of the market. The Waxman-Markey bill allowed for roughly $1 trillion in
allotments during the first thirteen years of the law’s enactment. The initial
allotments might become even more valuable over time because the bill called for
total greenhouse gas emissions to fall 17 percent from their levels in 2005 by the year
2020.
“We created a commodity out of nothing,” Phillips said.
The committee invited conservative Democrats to negotiate how the allotments
would be allocated, creating a windfall available to early adopters of the cap-and-trade
system. Phillips and his colleagues held closed-door meetings with staffers for
congressmen like Gene Green of Texas and Virginia’s Rick Boucher, whose home
districts were rich in fossil fuel jobs. The political horse trading gained intensity
through April and May as Waxman-Markey gained support in the House. Phillips
said that the energy-backed Democrats bargained hard for a big share of allotments.
The committee couldn’t help but comply. “The last thing we wanted to do was be
responsible for shutting down US industry,” Phillips said. “So they had a captive
audience.”
The biggest share of allotments—about $378 billion worth—was given to the
electrical utility companies. Just 6 percent of the allotments would be paid to support
renewable-energy sources and energy efficiency plans at the state level. That was less
than the 6.5 percent offered to natural-gas-fired utilities.
Phillips said that the oil refiners pushed hard for more allotments, mostly through
the office of Gene Green, who had multiple oil refineries in his home district in
Texas. Ultimately, they agreed to a price. The bill would pay out $17.8 billion to the
oil refiners. Phillips and his colleagues made this concession over the protests of
environmental groups, who already claimed that the cap-and-trade system favored
polluters. Even with that pressure coming from liberal Democrats, the subsidy to oil
refineries seemed necessary to get the bill passed.
“They gota great deal,” Phillips said.
His view was not shared by Koch Industries’ lobbyists. While Phillips was using
carbon allotments to target conservative lawmakers who were hesitant to support the
bill, Koch’s lobbying shop was employing different tactics.
David Hoffmann heard the strategy laid out during the meeting of Koch
lobbyists. Koch decided to target moderate Republican politicians who might be
tempted to support the measure. There were not enough Republican votes in
Congress to kill the bill, but Republican resistance could help slow its passage and
make conservative Democrats think twice about supporting it. These were the very
same votes that Phillips and his colleagues were trying to secure in the early summer
of 2009. If Koch could peel away support from the Republican side, the effort might
collapse.
“It was all about identifying those representatives who were on the fence,”
Hoffmann recalled. “I just remember them talking about individual representatives
they needed to reach out to.”
There was no better target, in this effort, than a deeply conservative congressman
from South Carolina named Bob Inglis. He was a close ally of Koch Industries, who
had taken the company’s campaign donations and toured its factories. But Inglis
would later admit that he was a “heretic” on one issue: global warming. It would
make him an example to his peers—and destroy his career.
Bob Inglis was a reliably conservative Republican with a solidly conservative voting
record from one of the most conservative congressional districts in the most
conservative state in the country. It went without saying that he didn’t think global
warming was real.
“For six years, I said climate change was nonsense. I didn’t know anything about it
but that Al Gore was for it,” Inglis recalled. “That was the end of the inquiry for me.
Al Gore’s for it. I’m against it. Next.”
Inglis might have remained rooted in this belief if he hadn’t been elected to
Congress and then become a senior member of the House Committee on Science,
Space, and Technology. During his tenure on the committee, Inglis traveled to
Antarctica and toured a laboratory that tested ancient air bubbles trapped in ice cores
from deep inside ancient glaciers. The evidence from these tests astounded Inglis and
seemed simply inarguable. The evidence showed that atmosphere carbon
concentrations were increasing dramatically. Al Gore wasn’t anywhere nearby to
interject his opinion.
The facts just stood alone.
A slow change unfolded in Inglis’s thinking. The change was fed by other trips he
took as a member of the Science Committee. He visited coral reefs that were dying
because of the increased carbon levels in the water, which made oceans more acidic.
He studied the heat-trapping effects of carbon and the enormous levels of carbon
emissions from industrial activity. He came to believe that carbon emissions were a
slow-moving, man-made disaster that might eventually endanger life on Earth.
When he ran for Congress in 2008, Inglis ran on a platform that supported the
renewable-energy industry. He saw it as a way to win jobs for his home district. Inglis
didn’t see any political danger in this position—he had a keen feel for his voters in the
Fourth District of South Carolina, a largely rural area that included the small cities of
Greenville and Spartanburg. He thought that betting on conservation and renewable
energy was betting on the home team. General Electric manufactured wind turbines
in his district, and a Michelin factory there manufactured tires designed to increase
gas mileage in cars. When he ran for office, one of his slogans was “The road to energy
independence starts in South Carolina.”
When Inglis talked about controlling carbon emissions, he talked about it using
the vocabulary of markets, and capitalism, and innovation. Pollution became a
problem if the pollution didn’t carry a price, he believed. This was the classic market
problem of “externalities,” when companies externalized the cost of their production,
like pollution. Carbon emissions were arguably the largest externality in the history of
humankind. The cost of the emissions would be born heavily for future generations,
and companies burning carbon today didn’t have to pay a dime for it.
“Coal-fired technology gets away with belching and burning into the trash dump
of the sky without paying any tipping fee
III for the damage that it’s causing there,”
Inglis said
In spite of this conviction, Inglis couldn’t get behind the Waxman-Markey bill.
He felt like it was too complex and too sprawling to actually work. But Inglis
couldn’t let himself simply vote “no” on Waxman-Markey. “I had this rather Boy
Scout notion that if you’re going to oppose, you better propose,” he said.
In late May, Inglis proposed a law called the Raise Wages, Cut Carbon Act of
2009. The bill was similar to many New Deal laws in that it was severe, far reaching,
and elegant in its simplicity. It proposed putting a tax on carbon but matching it with
a cut to payroll taxes. This meant that any tax increase on consumers could be offset
by a tax cut on their earnings. And if people wanted to avoid the tax on carbon, they
had the freedom to shift away from carbon-intensive fuels. The tax would feature a
“border adjustment,” meaning that it would be levied on imported products from
China and other countries, ensuring that the cost of carbon wouldn’t be unfairly
heaped on US manufacturers.
In spite of this, Inglis was closely aligned with Koch Industries for most of his
political career. After he was elected in 2004, Koch invited Inglis to tour the
company’s Invista factory in his district, which provided about a thousand jobs.
Inglis remembered Koch’s lobbyists flying in from DC to accompany him on the
tour. He shook the hands of employees, learned about Invista’s product line, and had
a delightful time. The affection seemed mutual. Between 2005 and 2006, Koch’s
PAC donated $7,000 to Inglis’s campaign, becoming his fourth-largest contributor.
For the 2008 campaign, Koch’s PAC donated $10,000 to his campaign, becoming his
second-largest contributor.
In 2009, the impending vote on the Waxman-Markey bill put Inglis in a bind. He
had long claimed global warming was a danger, but now his convictions would be put
to the test.
The pressure intensified in late May, when the Waxman-Markey bill was passed by
the Energy and Commerce Committee, which had stifled the effort for so many years
under John Dingell. Henry Waxman, the new chairman, pushed the bill through
committee so quickly that it even surprised the staffers working on it. Phillips had
believed that passing the bill through the committee would be harder than passing it
through the entire House, because the committee was heavily staffed by conservative
Democrats with deep ties to the energy industry.
“I got emotional [during the vote]. I remember looking around on the dais, and
my eyes were welling up,” Phillips recalled. “That really was the day where it was like,
‘Oh, holy shit. This might happen. This is probably going to happen.’”
It looked like the bill would be voted on by the entire House in June. This was
breathtaking speed in the world of legislation. Within a month of the bill passing
committee, every member of the House would have to figure out where they stood
on the cap-and-trade bill. Bob Inglis was no exception. As he tried to figure out if he
would vote for Waxman-Markey, Inglis kept in close contact with his campaign
donors. Like most congressmen, Inglis spent hours, every week, raising cash. He never
had the luxury of focusing entirely on the job of policy making; the midterm election
of 2010 was just over a year away, and Inglis needed to have plenty of money on
hand.
Inglis raised cash in a small office building just a short walk from his office on
Capitol Hill. The office was in a nondescript townhouse that was home to the
National Republican Congressional Committee, the fund-raising arm of House
Republicans. It was illegal for members like Inglis to use their own offices to raise
money, so the NRCC provided them with a small call center for the task. Inglis and a
staffer showed up at the NRCC and walked down the hall to a small, private office,
which Inglis called a “cubby,” that had two chairs and two phones. Inglis’s staffer
worked the phone until she had someone on the line, handed the phone to him so he
could ask for money, and start dialing for the next donor.
Koch Industries was areliable donor, so Inglis made sure to call them early.
Inglis called Koch’s lobbying office to see if he could count on the company’s
support again. Calls like the one to Koch were the easier calls—he was maintaining a
relationship rather than trying to build a new one.
The call went poorly from the beginning. The lobbyist whom Inglis usually spoke
with wasn’t there. He asked if a Koch lobbyist might be able to attend a fund-raising
breakfast. He was told that that would not be possible. The call ended quickly.
“I just remember it being a little bit chilly,” he recalled. He hung up and thought
to himself, They’re not giving me any money this cycle.
The phone call was just the first of many messages that Koch Industries would
send to Inglis.
Jonathan Phillips stood in the gallery of the chamber of the US House of
Representatives, looking down on the wide-open floor area with its concentric half
circles of seats for the members of Congress. It was Friday, June 26, 2009, the day that
the House would vote on the Waxman-Markey bill. Phillips wasn’t at all sure that the
bill was going to pass. Support was narrow, and any defections from the Democrats
could sink it. It appeared that some defections were in the offing. Pelosi seemed to be
working the crowd, making deals, quieting concerns. “Pelosi was doing I don’t know
what sort of horse trading,” Phillips recalled. “Those are the type of tough votes
where she’s making promises, you know?”
Over the next several hours, Republicans and conservative Democrats voiced their
opposition to the bill based on a shared foundation. They didn’t attack the evidence
about climate change or challenge the need to promote renewable sources of energy.
Instead, they attacked the Waxman-Markey bill as an economic disaster; an expensive
tax on everyone that would raise the prices of electricity, gasoline, and energy. The
theory behind the cap-and-trade system, of course, was that market forces would help
solve the price problem over time as companies invented new technologies that were
carbon free and introduced them to the market.
After nearly eight hours of procedural maneuvers and debate, Ed Markey rose to
speak. He didn’t seek to rebut many of the attacks one by one, but answered them
with a call to take part in history. “This bill has the ambition of the moon landing, the
moral imperative of the Civil Rights Act, and the scope of the Clean Air Act all
wrapped up in one,” he said.
After exhausting their arguments, the Republicans prepared to make their closing
statement. They reserved the privilege for a rising star in the House, a former
conservative talk-radio host from Indiana who was first elected to the House in 2001,
named Mike Pence.
Pence walked to the rostrum and looked down for a moment before beginning his
speech. He was a striking figure, a handsome man with a square jaw and stark white
hair. His training in show business was apparent the moment he started to speak.
While other congressmen stumbled through their speeches, reading awkwardly from
ascript, Pence was at ease.
“It’s hard to know where to start,” he said, shaking his head. And then he paused,
a long, dramatic pause that ate up much of his allotted speaking time but had great
effect.
Everyone was listening. “This economy is hurting. American families are
struggling under the weight of the worst recession in a generation,” he said, with great
sadness and great compassion in his voice. “In the midst of the worst recession in a
generation, this administration and this majority in Congress are prepared to pass a
national energy tax that will raise the cost of energy on every American family.”
And then Pence did something that none of his colleagues seemed to have done
during the course of an eight-hour day. He looked directly into the C-Span camera
and talked directly to the viewers there, whoever they might be. He pointed his finger
at them and exhorted them to get up and make a difference. “If you oppose the
national energy tax, call your congressman right now!” he bellowed. “Alexander
Hamilton said it best: ‘Here, sir, the people govern.’ We can stop this bill. We can do
better. And so we must.”
It was an impassioned speech, but Pence’s rallying cry seemed oddly out of place.
There didn’t seem to be some great crowd of voters in the C-Span audience ready to
mount a rebellion against the Obama agenda. Pence finished his speech and stepped
back in the gallery, looking like a pied piper with no one to follow him.
After several hours, the debate was finished, and the roll call vote began. Phillips
and his colleagues watched as the votes were tallied, and their elation grew with every
minute. The margin of victory became insurmountable. A one- or two-vote margin
turned into a seven-point margin. The bill passed 219 to 212. Gene Green, the
conservative Texas Democrat from oil refinery country, voted for the bill, as did Rick
Boucher, from coal country. Remarkably, eight Republicans broke ranks to support
the bill, more than Phillips or anyone on his committee might have expected.
When the vote was tallied, Phillips and his colleagues went to the staff office of the
Energy and Commerce Committee. These were nice offices, a big space that was far
removed from the basement warren where Phillips had worked for years. Bottles of
champagne were popped open, glasses were passed around. Both Waxman and
Markey were in the room, talking with staffers. Both men gave a speech. There was a
tremendous sense of accomplishment in the room. As they drank and laughed and
clapped each other on the back, everyone seemed sure that the bill would pass the
Senate within months, probably by Christmas.
“We did what we set out to do,” Phillips said. “I totally felt like this is what I came
to Congress for.”
Every quarter, Charles Koch held meetings in the company boardroom to evaluate
the progress of each major division in his company. He peppered the business leaders
with questions, probing their presentations for weak points and questioning their
plans for the future. By the middle of 2009, Charles Koch was getting similar
presentations from his political operatives. He sat at the large, polished wood table
and listened as top operatives in his political network walked through the events of
the past months, shared their analysis of the landscape, and laid out their plans for the
future.
In the middle of 2009, the news from the political operation was unrelentingly
bad. The Waxman-Markey bill had passed the House and was fast-tracked toward the
Senate. To make matters worse, Obama’s stimulus bill was doling out billions of
dollars to Koch’s emerging competitors in the wind, solar, and renewable-energy
industries.
As with any business unit, Charles Koch absorbed this information with apparent
dispassion. He asked for data and analyzed it closely. One senior political operative
recalled sending Charles Koch a spreadsheet with polling data on voter attitudes. The
presentation included “top line” figures, showing broad voter attitudes that were
accompanied by several “cross tabs” of detailed data that broke down the results by
demographic group. As the operative was presenting his findings to Charles Koch
and other directors of the company, Koch interrupted to question them about the
data.
Charles Koch asked about figures in the cross tables. He wanted to know why
women in one geographic area felt the way they felt. The operative was shocked at the
level of granular knowledge behind the question. Charles Koch was paying just as
close attention to his political efforts as his corporate endeavors.
It seemed even more surprising that Charles Koch could keep all of these political
operations straight in his own head. The contours of Koch’s political machine were
intentionally obscured and complex. Outside analysts would spend years trying to
piece together all of its various pieces. The political machine consisted of at least
dozens of shell groups funded by anonymous donors, some of them staffed by
current and former employees of Koch Industries. The network included the main
lobbying office in Washington, DC; all of the contract lobbyists it hired; a relatively
obscure activist group called Americans for Prosperity with chapters in several states;
at least several private political consultancies; the Koch Industries corporate PAC;
various think tanks; academic programs and fellowships; and a consortium of wealthy
donors that Charles and David Koch convened twice a year to pool large donations
for Koch’s chosen causes. And these elements were just the most visible pieces of the
Koch political machine.
The entirety of the political apparatus could only be viewed from the top, by a
handful of people with the authority to see the entire operation. These people were
Charles Koch, David Koch, and their top political operative, Richard Fink. Of the
three of them, Charles Koch unquestionably had the most authority. It was Charles
Koch, then, who had the most influence over how this political machine would react
to the surprising momentum behind the Waxman-Markey bill. His reaction might
have been unsurprising to anyone who knew him well. Charles Koch had been
unyielding in his years-long legal battle against his brother Bill. He had been
unyielding in his battles with relatives and shareholders who wanted to take the
company public. He had been unyielding in his battle against labor unions. He was
unyielding now.
Koch’s political machine was deployed, in 2009, in ways that it had never been
deployed before. Millions of new dollars would flow into a new political network at
the state level. Hundreds, possibly thousands, of new activists would be brought on
board. New attack campaigns were launched. New political candidates were chosen
and supported.
In the fight that Charles Koch was about to wage, there would be no compromise.
There would be no effort to amend the Waxman-Markey bill or win subsidies
through the emission allotments. There would be no effort to suggest an alternative
path to lower carbon emissions, such as a carbon tax. There would not even be an
acknowledgment that climate change was real.
The central strategy would remain the same as the one conveyed in Koch’s
lobbying office earlier in the summer. The primary target of Koch’s campaign would
be Republicans who supported the Waxman-Markey bill, and any Republicans who
stood against Koch on the issue of climate change.
These Republicans were the primary targets for a reason. Koch’s long-term plan
was to reshape the Republican party, and these members would be made an example
of. The strategy wasn’t necessarily new, but the means that Koch used to pursue it
were unprecedented.
After the Waxman-Markey bill passed, Phillips and the other members of the Global
Warming Committee handed off most of their work to their colleagues in the Senate.
Congress was called into recess for the Fourth of July break, and members went back
to their districts for the annual tradition of constituent meetings and parades.
During the holiday recess, the Global Warming Committee’s communications
director, Jeff Sharp, kept working, monitoring media reports about the WaxmanMarkey bill. The Senate would pick up debate of the measure in the fall, and Sharp
wanted to stay on top of the story in the meantime. Over the Fourth of July holiday,
Sharp started getting some disturbing phone calls and e-mails. There were protests.
And the protests were remarkable. Protestors were standing along parade routes, on
Independence Day, waving placards and shouting at the members of Congress as they
passed by. Sharp couldn’t remember anything like it happening before.
“At each parade, there is a group of four to six people in the parade screaming and
yelling: ‘No cap and trade! No cap and tax!’ Like, viscerally angry on that issue. In the
parade. This is a parade, right? Most parades, as you go through the parade, at that
time, people were not yelling and screaming about an issue, let alone a very specific
issue like cap and trade.”
The protestors were also showing up at the congressional members’ town hall
meetings, those boring civic obligations that never drew more than a half dozen
people or so. The town halls were crowded now with angry constituents who
hectored the congressional members with shaking anger in their voices. These
protestors didn’t look like typical protestors. They were middle-aged people. Mostly
white. Affluent looking. Not the kind of people that most Congress members were
accustomed to seeing protest in public.
Sharp received a video from the town hall meeting held by a Delaware Republican
named Mike Castle, who’d voted in favor of the Waxman-Markey bill. Protestors
lined the back of his town hall. They hooted and bellowed. They repeatedly brought
up the cap-and-trade plan.
“On this energy thing,” one protestor said, “CO2 emissions have nothing to do—
and the greenhouse effect has nothing to do—with global warming. It’s all a hoax!
Personally, for the life of me, I can’t understand how you could have been one of the
eight Republican traitors.”
At the word traitors, loud applause broke out. Castle, standing at a podium,
dutifully took notes as the protestors made their arguments. After the event, a woman
in the crowd pigeonholed Castle and informed him that the Earth was, in fact,
cooling. She asked if he knew how much the “cap-and-tax” system was going to harm
the poultry industry in Delaware.
Sharp watched these videos over and over. The comments struck him as odd. Cap
and trade and global warming had never elicited such visceral anger from the public.
People didn’t normally show up at parades and yell about one single issue. And he
kept hearing the same phrases, the same talking points, again and again. The
protestors talked about “cap and tax” and a “hoax” and an “energy tax.” It was as if
the protestors had been coached or handed a script. This wouldn’t have been
groundbreaking—Sharp had seen such tactics used up close during his years in the
PR and lobbying businesses.
When he saw these protests, Sharp saw a coordinated campaign. “I remember
watching that and [thinking]: Something is Astroturf–smelling about that event,” he
recalled. “It did not feel organic.”
Sharp kept watching the video of Mike Castle getting berated at the town hall.
And he kept thinking about the protestor in back who called climate change “a
hoax.”
“I remember watching it, and being like, Where did that guy get that from?”
I. This statement is provably untrue. NASA data shows that eighteen of the nineteen hottest years on record
occurred since 2001.
II. Laurie Sahatjian married and changed her name to Laurie McCausland.
III. A tipping fee is the fee a person must pay to dump garbage at a private garbage dump.
CHAPTER 20
Hotter
(2009–2010)
If suf iciently developed and organized, public sentiment, as manifested in Congress, can prevail over
presidential intransigence.
—Jon Meacham, The Soul of America: The Battle for Our Better Angels, 2018.
As hot as it is today, if we keep working this issue, it’s going to get even hotter for Barack Obama and Harry
Reid! Because I think the American people are fed up! Don’t you?
—Tim Phillips, president of Americans for Prosperity, speaking at a rally outside the US Capitol,
August 7, 2010
This was unmanageable. Bob Inglis was standing in an auditorium, in front of a very
large crowd, trying to make himself heard. He was hosting a town hall event and had
a microphone in his hand, but his words were drowned out by heckling and shouting.
He seemed dazed, like he couldn’t quite make sense of what he was seeing.
The first thing that didn’t make sense to Inglis was the sheer size of the crowd.
There were roughly five hundred people in the room, maybe more. This was
incomprehensible. Bob Inglis had been holding town hall events for years and was
lucky to draw fifteen or twenty people to each event. Americans simply didn’t turn
out for civic events, even if you provided free food. But one of his meetings that
summer drew an estimated seven hundred people. The fire marshals arrived at that
one and turned people away.
The second thing that didn’t make sense to Inglis was the rage. The crowd, all of
them, were boiling with anger. At most political events, it was rare for anyone in
attendance to stand up and speak into a microphone; the few people who did were
the same handful of gadflies who spoke at every meeting. This crowd was different.
They weren’t just ready to stand up and speak. They looked ready to charge the stage.
They were shouting. Booing. Cupping their hands around their mouths and
catcalling.
The crowd was shouting, and Inglis was trying to make his voice heard and to
calm things down a little bit. But the acoustics in the auditorium were awful, and the
sound system was crummy. His voice was drowned out.
One of Inglis’s political aides, a young man named Price Atkinson, was out in the
crowd, carrying a microphone to hand to the attendees to let them ask questions.
Atkinson was wearing a suit and tie, and his short, dark hair was neatly combed. At
one point, Atkinson leaned over and held the microphone for a particularly agitated
middle-aged woman with long, dark hair who wore a peach-colored shirt. The
woman was waving a ream of papers in her hand. She said they were copies of the
Affordable Care Act, the proposed law better known as Obamacare. She had spent
hours reading through the entire bill, she said, and was horrified by what she saw
there.
“There are things in this health care bill that people don’t realize are in there!” she
cried out. “They want to put a chip in every one of us! It talks about it right here!” she
said, flipping through the pages. She claimed that if Obamacare passed, every
American would be mandated to have a microchip implanted in their body, allowing
the government to monitor the populace.
I
This proclamation evoked cross-shouting from the rest of the crowd. People raised
their hands for the microphone. More shouting ensued. The woman seemed
determined to read pertinent portions of the bill, and crowd members began to
shout, “Let her read it!” as other crowd members booed and catcalled.
Inglis tried, again, to speak. This was how it went all summer. The crowds who
attended his public meetings were enraged with Washington, DC, enraged with
Barack Obama, and enraged with Inglis himself. They were enraged about
government bailouts, the stimulus, Obamacare, and, very often, about the WaxmanMarkey cap-and-trade bill that Inglis had voted against. Inglis discovered that voting
against Waxman-Markey wasn’t enough. The crowd was aware of Inglis’s views on
climate change and his proposed bill to pass a carbon tax. He tried patiently to
explain the fifteen-page bill he had proposed and explain how the carbon tax would
be balanced by a cut in payroll taxes. But the crowds were not convinced. They called
the Waxman-Markey bill, which was just then being debated in the Senate, the “capand-tax” bill and the “crap-and-tax” bill.
Amid all the shouting, Inglis saw small things that were deeply puzzling.
During the town hall meeting where the woman waved her pages and warned
about being microchipped, Inglis saw something behind her. There, in the back of
the room, a person was filming the event. And they were using a nice video camera,
set on atripod. This stuck in Inglis’s mind. It seemed to signify something.
“It wouldn’t be your average person who comes with a tripod and sets up,” he
said. Somebody was helping.
When heated protests broke out across the country over the Fourth of July weekend
of 2009, one of the larger events was sponsored by a little-known political group
called Americans for Prosperity. Strangely enough, this event was held in the deepblue, liberal state of New Jersey, which had voted overwhelmingly for Barack Obama.
The event was hosted by Steve Lonegan, Americans for Prosperity’s state director in
New Jersey. The protest was held in a large city park, and Lonegan was slated as one
of the main speakers.
It was sunny that day, and Lonegan wore a short-sleeved button-down shirt and a
red necktie when he walked out on the large stage to address the crowd. He stood
near a podium draped with a bright-yellow banner, called the Gadsden flag, that
showed a coiled rattlesnake above the motto “Don’t Tread on Me.” The flag dated
from the Revolutionary War, and it became a common sight that summer.
When Lonegan grasped the microphone, he didn’t look like a revolutionary. He
looked exactly like what he had been for twelve years, which was a small-town mayor.
His shirt was tucked into his slacks, and his necktie seemed to be knotted just a little
too tight. He was slightly portly and wore glasses. But he was a good speaker and he
knew how to rile up a crowd. Lonegan, a Republican, had honed his speaking skills
during the decade that he was mayor of the small, liberal town called Bogota
(pronounced Buh-GO-dah). He sharpened those skills even further after he left
public office, when he became a traveling evangelist for the political vision of Charles
Koch.
Lonegan was hired as one of the first state directors for Americans for Prosperity.
When he joined AFP, as insiders called it, Lonegan was just one of a handful of state
directors. The group was founded in 2003, and within a year, it included state-level
chapters in Kansas, Texas, and North Carolina. AFP was small and quirky and a
marginal force in American politics back then. Its budget was about $3 million in
2003 and just $1 million in 2004. Still, Lonegan felt a close sense of camaraderie with
the early directors and board members of AFP. Lonegan reported directly to the AFP
president, an activist named Tim Phillips, whom Koch had hired in from the
conservative Christian movement. When he joined AFP, Phillips stopped
campaigning against abortion and gay marriage and started campaigning for tax cuts
and regulatory rollbacks. This was a message that Lonegan believed in passionately,
and he took up the cause with gusto. He started raising money for AFP’s New Jersey
chapter—in over six years, he claimed to have boosted the annual fund-raising take in
his state from $150,000 to $1.6 million.
Lonegan invested countless hours of his own time. He drove from town to town
throughout New Jersey and gave speeches at libraries and Rotary club meetings, and
even at Democratic Party gatherings. He hosted a local radio show where he preached
against the creeping reach of state authority in New Jersey. He often drove for hours
to show up at some public library where only four or five people arrived to hear him
speak.
Now people were listening. That Saturday on the Fourth of July, Lonegan was
looking out over a crowd of hundreds. They were mostly older and almost entirely
white. They looked affluent. Someone had brought a large American flag that swayed
in the breeze. Dozens of people brought camping chairs that they’d set up in a rough
semicircle on the grass in front of the stage.
The crowd was united in their outrage but disparate in their complaints. A man
with white hair, sunglasses, and cargo shorts held a placard that simply read: “I
WANT MY COUNTRY BACK.” A middle-aged woman in a straw sun hat held a
yellow, stenciled placard that read: “JUST SAY NO. NO MORE SPENDING. NO
MORE TAX INCREASES. NO GOVT RUN BUSINESS.” Other signs read: “SAY
NO TO SOCIALISM!” And “SILENT NO MORE!”
If the crowd’s grievances were diffuse, then it was Lonegan’s job to focus them.
He united the crowd by giving a stump speech that AFP helped him fashion over
many years.
“You know, we’ve been hearing a lot about global warming, right?” Lonegan said.
“The reason that we’re redistributing our nation’s economy and industry around the
world—it’s under this pretense of global warming. We’ve heard now how we’re
destroying the environment, and we’re destroying the polar bear population.”
At the mention of polar bears, the crowd groaned and booed. Lonegan had them.
He stoked their discontent by claiming the EPA was suppressing a report showing
that the polar bear population was actually increasing, in spite of Al Gore’s hysterical
warnings. To underscore his point, Lonegan introduced his guest speaker, a man
dressed in a polar bear suit, who had been wandering through the crowd carrying a
sign that said, “I am AFP!”
The guy in the polar bear suit, introduced as “Prospero the Polar Bear,” stepped
up to the microphone as the crowd started to chuckle.
“I don’t know—how many of you can hear me?” Prospero asked into the
microphone, as it reverberated with feedback. “There’s too many polar bears!”
This drew sweeping laughter. “When I grew up, there was plenty of space,”
Prospero continued. “Now there’s fifty thousand of us. And we just keep making
more and more. They say it’s getting warm and icebergs are melting. Well, I needed
more space, so I came down here.” The Prospero routine killed. As Prospero stepped
back, Lonegan took the microphone and quoted the founding fathers and the US
Constitution, driving home the importance of liberty and the constraints that must
be placed on government. The rhetoric was elegant and forceful. It equated the capand-trade bill with government tyranny, and the fight against the bill with America’s
primal struggle against oppression.
Lonegan’s rhetoric was strategic. By emphasizing the centrality of climate change
legislation to popular discontent with American politics in 2009, he was carrying
forward the corporate lobbying campaign that Charles Koch had initiated from the
boardroom in Wichita. This strategy was central to AFP’s role in Koch’s political
network. From the earliest days of AFP’s inception, the group operated as something
like a fast-food franchise. AFP was composed of semiautonomous state chapters, but
all of them served products from the same menu. The menu was designed with great
care and specificity by Charles and David Koch and their lieutenants in Koch’s
lobbying operations. This meant that state-level directors had a lot of autonomy.
Lonegan developed his own pool of local donors and had the freedom to hire his own
field directors and to determine where he spoke. But ultimately Lonegan and other
state directors were told by AFP headquarters what they should say and how they
should say it.
“I had to report to the national office,” Lonegan recalled. “They gave guidance on
where our issues would lie. . . . So, I would report regularly to my boss on what issues
were emerging, and then we’d determine how they’d want to address it. Not every
issue that I saw as an issue did they think was an issue.”
This blend of local autonomy with centralized control created a political
organization that was uniquely powerful and effective. AFP could mobilize the type
of popular citizen involvement that most people referred to as grassroots support.
But it coupled this popular support with intelligence and guidance developed inside
one of the most well-funded corporate lobbying operations in America. This meant
that AFP could get people marching in the streets, and it could get them marching in
the exact streets and zip codes of congressional districts where their marching would
most effectively benefit Koch Industries’ strategic interests. The lobbying shop,
under Philip Ellender, attained the kind of real-time, granular political intelligence
that only the largest corporations had the resources to develop. That information was
then shared with a multistate network of ground-level activists of the kind that
Lonegan had built over many years in New Jersey.
Koch’s lobbyists were unique in their ability to closely coordinate with the
network of “third-party” groups that Koch Industries supported and nurtured.
Koch’s lobbying office held conference calls “daily—multiple times every day” with
Koch operatives who coordinated the activities of the third-party groups, according
to one person familiar with Koch’s political operations.
The coordination could also occur at the highest levels. Richard Fink, Charles
Koch’s top political lieutenant, sat on AFP’s board of directors from the beginning.
He also sat in on the lobbying strategy meetings in Washington of the kind that were
attended by Ellender and the compliance lawyer David Hoffmann.
The potency of this tight coordination would not be felt during AFP’s early years.
During the George W. Bush era, AFP wasn’t much more than a political sideshow.
Even by 2008, the organization was doing the political equivalent of cheap stunt
work. The group hired out a hot-air balloon to fly around with a placard claiming
that concern over climate change was nothing more than “hot air.” It hired
cameramen to accost people who showed up for an Al Gore speech on global
warming the summer of 2008, asking them why they drove to the event if driving
meant that they burned fossil-fuels.
AFP’s full power was not mobilized until the Waxman-Markey bill threatened
Koch Industries. As the threat of regulations on carbon emissions increased, Charles
and David Koch dramatically increased the funding and reach of Americans for
Prosperity. In 2007, the group had a budget of $5.7 million. By 2009, that budget was
$10.4 million. In 2010, it was $17.5 million.
In 2009, AFP became a central part of the Koch network’s political influence
operation. The group filed paperwork for chapters in thirty-three states and the
District of Columbia. The state chapters opened pages on Facebook and built e-mail
lists for volunteers. Lonegan had a hard time keeping up with the increases in
funding, staff, and new state chapters.
While the funding increases were important for AFP, something else was
happening that was even more significant for the group. Lonegan and AFP finally
had an audience. After Barack Obama’s election, Lonegan was no longer speaking to
crowds of four or five people at public libraries—he was speaking to hundreds. The
crowd that showed up for the Independence Day rally was just the beginning. There
were people everywhere, even in New Jersey, who were fed up with the direction of
American politics and were becoming activists for the first time in their lives. This
movement would come to call itself the Tea Party.
As it turned out, Charles Koch had laid out a white tablecloth and fine china for
this tea party many years in advance. The causes Charles Koch had been advocating—
cutting the national debt and halting the reach of federal government into private
markets—were causes that Tea Party activists cared about passionately.
Koch Industries and the leaders of Americans for Prosperity did not create the Tea
Party or even orchestrate it. But they were ready for it, and prepared to steer it and
shape its concerns. Lonegan and others at AFP helped make climate change
regulation a central focus of the Tea Party movement. When Lonegan hosted rallies,
he and his team were ready to record the e-mail address of anyone who shared it. They
made phone trees and hosted volunteer training sessions. They passed out the phone
numbers of local congressmen to activists and coached them on the best time to call.
(Late night was sometimes best so that volunteers could leave voicemails, which
would be waiting in big batches when the politician showed up for work the next
day.) They taught volunteers the fine art of calling talk-radio programs and getting on
the air, coaching them to mention the right website address or phone number when
they were on the air.
Lonegan and his colleagues did more than just get Tea Party activists to focus on
the Waxman-Markey bill. Americans for Prosperity also helped direct the activists’
passion toward a very specific group of targets: Republican politicians. Attacking the
Republican party was one of AFP’s central strategies from the earliest days. In 2006,
Lonegan attended a private AFP event hosted by Charles and David Koch, in Aspen,
Colorado. The event was an annual symposium attended by wealthy conservative
political donors, academics, and activists that Charles Koch began to convene in
2003, just as he helped launch Americans for Prosperity. The seminars were another
innovation in Charles Koch’s broader political strategy: rather than fund his political
causes alone, Charles Koch sought to enlist fellow donors. Twice a year, the donors
attended seminars in Aspen, Palm Springs, or other scenic getaways, pledging their
money to Koch’s causes and hearing speeches from politicians who auditioned for
Koch’s political support. When Lonegan heard Charles Koch speak at the seminar in
2006, he was inspired by Koch’s ambitious vision and strategic intelligence. Lonegan
was also impressed by Charles Koch’s strategy of using his donor group’s resources to
attack conservatives rather than liberals. The strategy seemed counterintuitive, but
effective.
“I’m a big fan of Charles Koch. I think he’s a brilliant guy and very well read, and
he gets it,” Lonegan recalled. “He said, ‘The problem we have is not the Democrat
Party. They’re doing what Democrats do. Our problem is the Republican Party.
We’ve got to make Republicans act like Republicans.’”
Koch and Americans for Prosperity pressured the Republican party from the
right, steering itaway from the compromises of neoliberalism and pushing it toward a
vision that was espoused by Austrian economists like Friedrich Hayek. It gained more
volunteers every day, and it steered them toward one target: Republican politicians
like Bob Inglis.
Bob Inglis’s congressional district in South Carolina contained the tiny town of
Boiling Springs, located just a little bit north of Spartanburg. The town was easy to
miss. Its most prominent feature was a strip of stores near Highway 9 and a Walmart
Supercenter on the north end of town. But Boiling Springs became an important
landmark on the political map in 2009, when a woman named Maria Brady had a
vision from God. The vision arrived when she was at work, and it would set her life
on a direct collision course with Bob Inglis.
Brady and her husband, Michael, owned a printing company in Boiling Springs
that published the local newspaper, Boiling Springs Today. Maria was working from
home when she had the epiphany, sitting in front of the computer. She heard a voice
in her head that said very clearly: “Quit complaining. Quit complaining and do
something.”
Brady had been complaining a lot during that winter of 2009. Business at the
printing shop collapsed after the financial crash. The company printed advertising
circulars, and local businesses cut their advertising budgets sharply during the deep
recession. Maria and Michael laid off workers, scaled back production, and worried
about paying the bills. Yet whenever Maria turned on the television news, she saw
that the same Wall Street CEOs who’d caused the crash were getting multibilliondollar rescue packages from the government. They weren’t even losing their bonuses.
After she heard God’s voice, Brady fell down on her knees and prayed, asking what
He meant and what He wanted from her. When Michael returned from the printing
shop later that day, he looked like he’d seen a ghost. He told Maria that God had just
spoken to him and told him that he needed to do something to help his country.
Mariashared her own vision. It was clear: they were being called to do something.
Maria began to scour the Internet. It was April of 2009. She came across mentions
of a new form of revolt by people fed up with the condition of America. She heard
about events that people were calling Tea Parties. The notion of throwing a Tea Party
was romantic. Patriotic. It conjured images of the earliest American revolutionaries
throwing off the yoke of imperial Britain.
Tea Parties first became part of the national conversation in February of that year,
during a broadcast on the financial news network CNBC. The anchors were
discussing the Obama administration’s proposal to modify many consumers’
mortgages after the crash made millions of houses worth less than the debt that was
owed on them. The anchors cut to a commentator named Rick Santelli, who was
reporting live from the trading floor of the CME Group in Chicago. Behind Santelli
were rows of traders at desks, buying and selling futures contracts and other
derivatives. They did not appear happy. Santelli was highly agitated, and expressed his
contempt at the idea that the government might bail out homeowners who found
themselves trapped in expensive mortgage agreements.
“The government is promoting bad behavior!” Santelli shouted into the camera.
He mocked the Obama administration while the traders around him clapped and
cheered him on. Santelli turned and gestured back behind him toward the trading
floor and shouted, “This is America!” And then he yelled to the traders: “How many
of you people want to pay for your neighbor’s mortgage that has an extra bathroom
and can’t pay their bills?”
The traders booed loudly, and Santelli turned to the camera to ask, “President
Obama, are you listening?”
“We’re thinking of having a Chicago Tea Party in July,” Santelli continued. “All
you capitalists that want to show up at Lake Michigan, I’m going to start organizing.
I think we’ll be dumping in some derivatives securities. What do you think about
that?”
The idea of throwing Tea Parties began to spread. The movement was organic and
improvised, driven by people like Maria Brady. Ordinary people who had never been
politically active reached out to friends and formed e-mail chains to stay in touch.
Middle managers, housewives, plumbers, and even commodities traders began to
organize.
Maria and Michael Brady assembled an e-mail list of friends and neighbors and
helped form the Boiling Springs Tea Party. They planned a Tea Party for Tax Day in
mid-April. Maria ordered a costume for Michael, with a tricornered hat and an
elegant jacket with golden lapels. When he wore the outfit, he looked like he’d
stepped straight out of 1776. Hundreds of people showed up for the protest, even
though it had been organized on short notice. Maria was amazed. When she held a
placard in public for the first time, she felt more than happy. She felt a sense of
belonging.
“It was the hardest thing I’ve ever done,” she recalled. “I loved it. It was a trip. It
felt good to realize that ‘Hey, I’m not by myself.’”
In the weeks after the protest, members of the newly formed Tea Party chapter of
Boiling Springs stayed in close contact. They planned a bigger rally, this one to be
held on the Fourth of July.
This time Maria and Michael had help. They connected with the South Carolina
chapter of Americans for Prosperity. Tea Party groups around the nation were doing
the same thing. Maria and Michael Brady were neither directed by Americans for
Prosperity nor even inspired by Americans for Prosperity. But AFP provided its Tea
Party groups and others with concrete means of assistance that amplified their
message and energy in vitally important ways.
Americans for Prosperity’s South Carolina chapter formed a Facebook page and
website that became a central clearing hub for Tea Party activists. When people like
Maria Brady threw up their arms and went to the Internet, they found the Americans
for Prosperity site. It listed ways that they could get involved. It provided a platform
to connect with fellow activists.
The site promoted Maria and Michael’s upcoming Fourth of July protest, and it
included Michael Brady’s name and telephone number for anyone interested in
attending. The page also included a long list of other activists planning to hold
protests on Independence Day. The AFP site also included a nationwide database
listing the times and locations of town hall meetings that Congress members planned
to host, encouraging the activists to attend. Bob Inglis’s town halls were on the list.
The website included a form to fill out that automatically sent letters to member of
the US Senate informing them to “vote no on cap and trade.”
AFP chapters in New Jersey and elsewhere offered free chartered bus rides to
protestors to attend a rally in Washington, DC, that summer. Once in Washington,
protestors were given free box lunches and glossy protest signs. The protestors were
joined by Tim Phillips, AFP’s president, who gave rousing rally speeches.
This close coordination masked key points of disagreement between Tea Party
activists and the political vision of Charles Koch. One of the very few rigorous studies
of the Tea Party found that the political beliefs of the group were far from libertarian.
Tea Party activists strongly supported popular entitlement programs such as
Medicare and Social Security, for example. They weren’t animated by a hatred of big
government but by the belief that entitlement benefits were being unfairly diverted to
people who didn’t work hard and didn’t deserve them. Their grievance was the
exploitation of the middle class, not the existence of robust New Deal–era safety net
programs. The racial tinge to the grievance was unmistakable, but also complicated.
Many Tea Party chapters took great pains to avoid any racist language at their
protests and welcomed minority members. But it was unmistakable that the
unworthy beneficiaries of entitlements, in their eyes, were Hispanic immigrants and
African-American residents of the inner city.
Maria Brady, for one, had no idea who Charles Koch was in 2008. She didn’t
study Hayek or von Mises or read papers from the Cato Institute. Instead, she began
her political education on the Internet. The stories she found there were outrageous.
She read that Nancy Pelosi had ordered two jumbo jet planes for her own use, and
that Congress had approved of the purchase, using taxpayer money. Brady and her
husband were paying for Nancy Pelosi’s private jet, and nobody was talking about it!
II
Brady did find one trusted source for news and education that was recommended
to her by many friends and fellow patriots. She began to watch the television show of
a commentator named Glenn Beck. “I kind of got an education. My start of my
education was Glenn Beck, I guess. Because that’s the only person that was talking
about the issues that I agreed with.”
Glenn Beck was the most prominent voice in the American Tea Party movement,
and understanding Beck’s political philosophy was critical to understanding the Tea
Party and the relationship of the Tea Party to Charles Koch’s political efforts.
Glenn Beck’s television show on Fox News drew close to three million viewers in
2009, beating the combined ratings of all his competitors’ shows. Beck spent many
years honing his skills as a political entertainer on talk radio, where provocation was
the currency of the realm. Debate was better than discussion. Suspense was better
than satisfaction. Outrage was better than understanding. Glenn Beck elevated this
genre to the level of high art. The narratives he spun on his show were terrifying and
purported to reveal the broad contours of chilling global conspiracies. He affected the
persona of a high school teacher, wearing a cheap, ill-fitting coat and tie. He stood in
front of a chalkboard. During one show, the chalkboard displayed three logos: The
United Nations symbol, the Islamic crescent, and the iconic Communist hammer
and sickle. Beck explained that these three logos represented the three global
movements that were currently hard at work to enslave and control his viewers.
“The world is on fire,” Beck said in a remarkably casual and civil tone. “And there
are three groups of people that wanta new world order.”
One of Beck’s favorite targets was the Obama administration’s efforts to promote
alternative fuels, which Beck portrayed as a vast conspiracy to steal wealth from the
middle class and transfer it to an elite group of liberal billionaires. The first phase of
the conspiracy, Beck explained, was to fool everyone into thinking that human
activity and the burning of fossil fuels was changing the world’s climate. Climate
change was alie, Beck said, perpetuated by dishonest scientists who cherry-picked and
fabricated evidence.
Americans for Prosperity helped promote this point of view. Phil Kerpen, AFP’s
national director of policy, joined Glenn Beck on his show during the summer of
2009 to help Beck analyze global warming and the clean energy conspiracy. Kerpen
sat opposite Beck, near the chalkboard that was covered with a spiderweb of
interlocking circles and arrows. The conspiracy outlined there was complex and
involved several think tanks, government officials, nongovernmental organizations,
and government programs. Beck reminded viewers that the clean energy crusade was
meant to steal their liberty.
“This is the head. This is the head. This is at least a main player in what is going on
in America!” Beck exclaimed. Then he looked directly into the camera and said: “I
believe, America, that this is probably the biggest—and correct me if I’m wrong . . .
This is the biggest story in history. It is the hijacking of our republic. Yes or no?”
Kerpen nodded his head in agreement. “I think you’re right,” Kerpen said. “And
the shame, the amazing thing to me is, that they’re so brazen.”
Beck was encouraged by these remarks, and incensed.
“This is gigantic money! And let me tell you something, America. Nobody is
doing this stuff on television,” Beck said. “It is the hijacking of our country.”
Beck’s show informed Maria Brady’s self-education. She researched the
Freemasons, paganism, and the US Senate. “Our government is running everything,”
she said. “They were taking over everything, and they did a lousy job. Everything they
put their little grimy hands on, they messed up. I am one hundred percent sure that
what’s wrong is that the government controls everything.”
This was von Mises on the retail level. Brady, in her way, was coming to the same
conclusions that Charles Koch had come to many decades earlier. But she didn’t hold
the antiseptic free-market views of an Austrian economist. Her Internet research led
her to darker places.
“I am totally convinced that probably seventy percent to seventy-five percent of
our government is being run by Satan worshippers,” Brady said. “That’s what’s
wrong with this country.”
Maria Brady’s point of view did not lend itself to roomy political debate or to
compromise with people of differing beliefs. She became a political activist who was
unyielding and religiously dedicated to saving her country from evil forces.
With the guidance and help of Americans for Prosperity, Brady found her first
political target. It was the congressman from her district, who was running for
reelection, named Bob Inglis.
When Bob Inglis held a town hall meeting in Boiling Springs, Maria Brady and her
compatriots were prepared. Brady sent out an e-mail to her list, informing her fellow
Tea Partyers about the event. When Brady arrived, she had a wad of small slips with
the words “pink slip” written on them. She stood outside the event and passed out
the pink slips to her friends. The idea was to throw these toward the stage at some
point, signifying the fact that voters were ready to send Bob Inglis packing. Brady
found a seat in the front row, so she was ready when Inglis took the stage and started
speaking. She estimated that the crowd was between three hundred and four hundred
people.
For Brady, the pivotal moment came during the question and answer session. She
wanted to know one thing: How could Bob Inglis vote to allow Nancy Pelosi to buy
two luxury jets for her own use on the taxpayer’s dime? She took the microphone,
and she asked this question, and she was horrified by his answer.
“He didn’t know anything about it!” Brady recalled. “He looked at me, and he was
like, ‘What? Whatare you talking about? I don’t know anything about this.’”
This was the moment when Brady realized that she had to do everything in her
power to make sure Inglis lost his seat in Congress. While it was untrue that Nancy
Pelosi had purchased two jets, Brady was correct on one point: Inglis seemed utterly
incapable of dealing with her question. He stood on the stage in a navy blazer and
white button-down shirt, trying to talk in measured tones to a crowd that was
shouting.
One woman interrupted Inglis, shouting: “I’m afraid of Obama!” Inglis stopped
and asked the woman: “Why are you afraid?” At this, the crowd erupted. A man
shouted, “Because he’s a Socialist!”
“Let me ask you something. This is very helpful,” Inglis said. “Where are you
getting that?” He was smiling and waving his hand, acting like he was engaged in a
collegial conversation about politics. Someone shouted that they were “getting that”
from Glenn Beck.
“Glenn Beck,” Inglis said. “Here’s what I’d suggest: turn that television off when
he comes on.” This is when Inglis lost the crowd. They erupted in a wall of boos and
shouts. Once again, he could barely be heard over the cacophony. He tried anyway.
“Let me tell you why. He’s trading on fear. I think that when you trade on fear . . .
you’re not leading. You’re following fearful people,” Inglis said. Brady remembered
that moment because that’s when her friends started throwing their pink slips at
Inglis.
Inglis was not a stupid man or an inept politician. He knew how to work a room.
The reason he failed repeatedly to win over the crowds at these town hall meetings
was that he would not say what they wanted him to say. His campaign slogan for
2010 was “America’s sun is still rising.” This was a horrible slogan, and Inglis knew it.
Nobody felt like the sun was still rising. He knew that he needed to say, “Okay, I hate
Obama as much as you do. Even more than you do.” He knew that needed to be seen
as “trying to bring back the good old days before the black man went into the White
House,” as he phrased it. “I just didn’t want to be that person. I wanted to be the
person who was saying that ‘Yeah, this is about the future of fuels. And I know we’re
in the midst of the Great Recession, but we’re Americans and we can overcome
this.’”
Inglis kept his slogan and stayed the course.
Koch Industries’ activities in South Carolina were just one piece of a broader strategy,
and a central focus of this effort was to defeat the Waxman-Markey bill before it
could be passed by the US Senate. Steve Lonegan, AFP’s director in New Jersey, came
to understand the broader strategy during conference calls and meetings with Koch’s
political operatives. Koch Industries would ramp up its operations outside the Senate
to turn up the heat on the politicians who worked there. The effort would employ all
of Koch’s political assets, from its campaign donations to its lobbyists and even its
think tanks.
One immediate target would be the Republican lawmakers who voted for the
Waxman-Markey bill in June. They would be made an example of, just like Inglis.
There were eight of these Republicans in all, and three of them were from New
Jersey: Congressmen Chris Smith, Leonard Lance, and Frank LoBiondo. Lonegan
immediately setabout making their political lives aliving hell.
LoBiondo’s office was flooded with phone calls criticizing him for his vote on
Waxman-Markey, forcing one of his aides to fax between 100 and 150 summaries of
the calls to LoBiondo each day. Many of the calls came from out of state. It was
exasperating and exhausting to keep up with. Lonegan’s tactics went beyond those
typically associated with political campaigns. He and his growing team taught the
newly energized Tea Party activists how to inflict the maximum amount of pressure
on the “Three Taxateers,” as he dubbed the congressmen.
“You do a rally in his backyard. You get lots of people to call his office and say,
‘What the hell are you doing?’ E-mails, phone calls. You have them confronting him
when he goes out to the diner. Again, this is where teaching people how to be good
activists comes in. Most people don’t know what to do,” Lonegan said. “So, I would
teach people.”
The purpose of Lonegan’s effort was not necessarily to drive the Three Taxateers
out of office. All three of them kept their seats. The goal was to send a message to the
US senators. AFP targeted conservative Democrats such as Senator Max Baucus, who
had a significant fossil fuel industry presence in their states. It also targeted wavering
Republican senators. By tormenting the New Jersey congressmen, AFP showed that
there was asteep price for supporting climate change regulations.
When the bill moved into the Senate, it needed to first pass through one of the
powerful Senate committees. This presented a moment when the entire effort to
regulate carbon emissions might be killed in the crib. Senate committee hearings did
not draw much public attention. The committee hearings were slow and boring and
filled with technical arcana. This delay in the process offered Koch the best chance to
kill cap and trade. Koch Industries seized it.
The Democratic Senate majority leader, Harry Reid of Nevada, was a master of
manipulating the political process. It was telling that he assigned the WaxmanMarkey bill to the Senate Committee on Environment and Public Works. The
committee was chaired by Barbara Boxer, a friend of environmental protections from
California, and a true believer in the cap-and-trade system. The Democrats did not
just control the committee, they held an overwhelming majority of its seats, with
twelve Democratic votes to the Republicans’ seven. Republicans didn’t have much of
a chance to stop the bill from being passed and sent to the entire Senate for a vote.
Still, the leading Republican on the Environment Committee, James Inhofe, from
Oklahoma, was not deterred. He had one advantage. The Senate was built in a way
that maximized the power of the word no. The House of Representatives operated
under the rules of a simple majority rule. The Senate was designed to thwart the idea
of majority rule and prize consensus between the parties. It took sixty votes in the
Senate to end debate on a topic. Bipartisanship wasn’t a virtue in this arena, it was a
necessity.
On the morning of the first Senate hearing, just after the Fourth of July recess,
Inhofe took his seat at the center of the horseshoe-shaped committee dais, just next to
Boxer. She began the hearing by preemptively criticizing Inhofe as an obstructionist.
He didn’t hesitate to respond.
“You have stated that we’re the party of ‘no.’ Well—that’s true. We say ‘no’ to
higher energy costs. ‘No’ to subsidizing the East and West Coasts at the expense of
the heartland. ‘No’ to more bureaucracy and red tape. ‘No’ to the largest tax increase
in American history and ‘no’ to sending our manufacturing jobs to China and India,”
Inhofe said.
Inhofe’s embrace of the word no telegraphed to the Senate that Democrats were
on their own. The Democratic Party held a supermajority of votes in early 2009, but
the supermajority was fragile. Max Baucus, for example, had voted against a cap-andtrade bill in the past. Claire McCaskill of Missouri said in 2009 that she would vote
against the measure. In this environment, getting to sixty votes would be difficult.
During July and August, Inhofe and Americans for Prosperity cleared the playing
field of any Republican participants. By the fall, all the Republicans on Barbara
Boxer’s committee were boycotting the proceedings. One afternoon hearing, Boxer
sat alone at the center of the dais. Arlen Specter of Pennsylvania, a conservative
Republican on the committee who’d switched his affiliation to the Democratic party
in April, told the Pittsburgh Post-Gazette that the boycott was an act of “really
excessive partisanship,” which surpassed what he had seen before in the Senate. “I
have been a party to some very heated disagreements, but they have been
disagreements on the merits, on the substance. . . . But you can’t disagree with an
empty chair,” he said.
The chairs remained empty. Barbara Boxer initially said that her committee would
pass a bill and put it before the entire Senate for a vote by September 8. Then, in late
August, that date was extended to late September. And then it was delayed into
October.
The bill fell under the shadow of larger, more visible legislative fights. The Senate
was simultaneously debating the Affordable Care Act, which drew Tea Party
protestors out in crowds to town hall meetings and parades. Americans for Prosperity
fed these efforts, arranging for bus rides and compiling e-mail lists to inform its
members of the time and location of the public meetings they could attend. The fight
over Obamacare drained the time, attention, and resources of Harry Reid, the Obama
administration, and the rest of the Democratic Party leadership. Everyone knew that
there was only so much momentum, so much political energy to be spent in
Washington. This was the key advantage that was given to Koch Industries. In the
Senate, the advantage always went to the opponent who wanted to stop something
rather than build something.
In October, Barbara Boxer and Harry Reid employed something called the nuclear
option: putting the bill to a vote in the committee over the objections of
Republicans. The bill passed without a single Republican vote. The bill was tainted
now, stained as being partisan. Each passing week made it easier for other senators to
stand aside and let the bill sink.
When the cap-and-trade bill moved to the Senate floor, it set off a frantic race
among senators who sought to shape it, support it, or kill it. During this period, Koch
Industries sought to raise the temperature even higher on any senator who considered
supporting the bill. To do this, Koch employed a tactic known as the “echo
chamber,” of which it had become a master. The echo chamber allowed Koch to
amplify its message while hiding its hand.
The strategy originated from the network of think tanks and academic programs
that Charles Koch had been building for almost forty years. In 1974, when Charles
Koch laid out his strategy for launching a libertarian revolution in the United States,
he listed education as the first of four pillars in his strategy.
III He had pursued this
strategy with great success, building the Cato Institute think tank and academic
centers like the Mercatus Center at George Mason University. These efforts had a
philosophical, almost noble, feel to them. The stated goal was to fund scholars and
big ideas that would slowly move society toward an understanding of Charles Koch’s
political vision. By 2009, the educational enterprise had become a network of shell
enterprises and hidden funding streams that gave immediate tactical support to Koch
Industries’ lobbying goals.
Ideas are the raw material of all legislation. In Washington, DC, there is a
surprisingly small congregation of think tanks, policy shops, media outlets, and
academic institutions that shape the daily political conversation. Over the decades,
Koch Industries became adept at seeding this territory with its own ideas, and its own
thinkers, in a way that hid its influence.
The echo chamber tactic began when Koch’s lobbyists would commission and pay
for an academic study, without claiming credit for it. That study, seemingly
independent of Koch, was then fed into a series of think tanks and foundations that
Koch controlled. Finally, the work of those think tanks was weaponized into the raw
ammunition of political campaigns. Taken together, it had the effect of making the
message from Koch Industries’ lobbying shop seem far louder, and far more popular,
than it really was. This, in turn, had a surprisingly strong effect on senators and other
lawmakers, who paid close attention to public sentiment.
In 2007, for example, Koch Industries quietly funded the work of a Democraticleaning think tank called Third Way. The think tank promoted “New Democrat”
policies such as those embraced by Bill Clinton: neoliberal policies that sought to
combine New Deal goals with free-market methods. Lobbyists at Koch’s office knew
that Third Way’s economic study program supported free-trade policies such as
NAFTA. Such trade policies were under attack in 2007 because they did not deliver
the economic benefits that they had promised to huge swaths of the American
population. The textile industry of South Carolina, for example, was decimated by
trade agreements, such as NAFTA. This was stoking opposition to such trade
agreements among both Democratic and Republican politicians.
Koch Industries supported free-trade agreements and wanted to ensure the
passage of future trade deals, while blocking any reversal of existing deals. The
possibility of any trade war was dangerous for Koch Industries not just because the
company had extensive business holdings around the world. To take one specific but
very high-stakes example: Koch’s Pine Bend refinery, still a major profit center for the
company, was deeply dependent on oil imports from Canada. Any trade disputes
ignited by renegotiating NAFTA could dramatically hurt Koch’s profitability.
Koch’s lobbyists knew that they wouldn’t get much of a hearing from Democratic
politicians. Very few liberals saw an upside in 2007 in carrying water for Koch. That’s
why Koch used Third Way to make its point: liberals listened to Third Way.
The Koch lobbying office directed money to support a Third Way report that was
published in November of 2007, entitled “Why Lou Dobbs Is Winning.” Dobbs was
a cable television personality who carved out a niche railing against free trade deals
that he said harmed the middle class. The Third Way report cast Dobbs as part of a
dangerous “neopopulist” movement that threatened to harm America’s future by
making the country turn inward. The report did not cite the support from Koch
Industries, nor does it appear that Third Way acknowledged Koch’s support
anywhere in its publicity materials. The report’s acknowledgments did give thanks to
Rob Hall, a lobbyist for Koch’s Invista division, thanking him for “his support in
helping us conceive of and design Third Way’s trade project,” without disclosing
Koch or Invista’s funding. Third Way was not obligated to disclose its support from
Koch Industries in its tax filings, and did not. Koch successfully pushed its view on
trade while barely leaving afingerprint.
In 2009, Koch’s use of the echo chamber was more targeted and better amplified.
The operation began at Koch’s lobbying office, where a senior manager directed
lobbyists to pay for a third-party economic report that would undermine support for
the Senate’s cap-and-trade bill, according to a person familiar with Koch’s political
operations.
To produce the report, Koch’s lobbyists selected a reliably conservative economic
think tank called the American Council for Capital Formation. The ACCF didn’t
hide its free-market leanings, and tax filings showed that it was funded by
ExxonMobil and other corporate interests. But Koch Industries took pains to hide its
involvements in the report it commissioned in 2009. Koch enticed another lobbying
group, called the National Association of Manufacturers, to “sponsor” the report,
with the understanding that Koch Industries would pay for it.
The Koch network had funded the ACCF for years, although it disguised its
contributions by using the Claude R. Lambe Charitable Foundation, which the
Koch family controlled. In 2006, the Lambe Foundation gave ACCF $40,000. It gave
$50,000 in 2007. Koch hired the ACCF to produce a study looking at the economic
damage that a cap-and-trade bill would cause the US economy. A person familiar
with the arrangement said that a study of this kind would cost roughly $100,000. In
both 2008 and 2009, the Claude R. Lambe Charitable Foundation gave $100,000 to
the ACCF. Then its contribution dropped back to $50,000 in 2010.
The report was released in August of 2009. It carried the kind of dry academic title
that conveyed a sense of credibility and seriousness in Washington, DC: Analysis of
the Waxman-Markey Bill “The American Clean Energy and Security Act of 2009.”
The report’s lead author was along-time ACCF economist named Margo Thorning.
The study was announced with a press release from the National Association of
Manufacturers. The announcement made no mention of Koch Industries’
involvement. Instead, the study appeared to have the backing of a trade group with
the interests of a wide range of manufacturing companies at heart.
The study was brutal in its assessment of Waxman-Markey. “Unfortunately, this
study confirms that the Waxman-Markey Bill is an ‘anti-jobs, anti-growth’ piece of
legislation,” NAM’s executive vice president, Jay Timmons, said in the press release.
The study’s predictions were dire, in part because the ACCF used a set of
economic assumptions underlying its analysis that most other studies did not use.
The group, for example, predicted that renewable sources of energy would be slower
to come online than many analysts predicted, which would leave the United States in
an energy crunch. The ACCF estimated that the Waxman-Markey bill would destroy
2.4 million jobs between 2012 and 2030 if it was passed. It estimated that electricity
prices would jump 50 percent by 2030, while $3.1 trillion in economic activity would
be lost.
Once the ACCF’s study was published, Koch Industries carried out the next phase
of its echo chamber system. The study was quickly promoted by a think tank called
the Institute for Energy Research, which sent out a press release on August 13 that
highlighted the study’s findings. The IER was an outgrowth of the Institute for
Humane Studies, the libertarian think tank cofounded by Charles Koch.
IV By 2009,
the IER was funded by Koch Industries and other companies, and a former Koch
Industries lobbyist named Wayne Gable sat on IER’s board of directors.
After the study was promoted by the IER, it was then recycled by another Koch
Industries–affiliated think tank. This one was called the American Energy Alliance,
and it was essentially the political action arm of the IER. The AEA was organized
under the tax code in a way that it could be directly involved in politics, while the
IER was organized as an “education” foundation that could not lobby or get involved
in political campaigns. Where the IER was high minded, the AEA was something
more of a street brawler. The AEA was headed by a former Koch Industries lobbyist
named Thomas Pyle, who remained in close contact with his former colleagues at
Koch’s lobbying shop.
The AEA produced a series of political radio advertisements that were based on
the new ACCF findings, along with other statistics that highlighted the potential
economic threat of a cap-and-trade bill. A narrator in one of the radio ads intoned:
“This tax will further cripple our already struggling economy—costing more
American jobs. . . . Higher taxes and more job losses—what could Congress be
thinking?” A corresponding fact sheet for the ad cited the ACCF for this claim. The
AEA political ads were targeted in a way that benefited from keen knowledge of how
the Waxman-Markey bill was then working its way through the Senate. Lindsey
Graham of South Carolina was a particular target. “Why would Senator Lindsey
Graham support a new national energy tax, called cap and trade?” one advertisement
began. Citing the ACCF study, the advertisement claimed that “cap and trade . . .
could significantly increase electricity bills, gas prices, and cost American jobs.”
In all of these statements and advertisements, the same set of numbers were used
again and again: More than two million jobs lost. Electricity prices would be 50
percent higher by 2030. These facts were also carried into Congress in the form of
direct testimony. When the Senate Finance Committee sought to learn more about
the economics of climate change, the committee invited Margo Thorning to testify.
The ACCF study was submitted as evidence beforehand.
“It’s pretty clear the costs outweigh the benefits,” Thorning told the committee.
Chairman Max Baucus, the conservative Democrat from Montana, pointed out that
the ACCF findings were far more negative than most. “You’re a bit of an outlier,”
Baucus said.
“We tried our best to build in realistic assumptions,” Thorning had said earlier.
Inside Koch Industries, the ACCF report was seen as a tremendous victory.
Koch’s point of view had been carried out into the world in real force—in press
releases, Senate testimony, think tank discussions, and political attack ads. And
Koch’s name wasn’tanywhere to be seen.
Koch Industries wasn’t the only company to use these tactics. ExxonMobil also
funded third-party groups that sought to raise doubts about the science behind
climate change and to fight the cap-and-trade bill. But Greenpeace, the
environmental activist group that fought hard to limit air pollution, found that Koch
Industries fought to undermine the scientific consensus around climate change for
longer, and more fiercely, than even Exxon. A 2010 Greenpeace analysis of spending
on climate-denial groups between 2005 and 2008 found that Koch Industries and its
affiliates spent $24.9 million to support such groups, almost triple Exxon’s $8.9
million in spending.V And Koch was more uncompromising than Exxon, whose
lobbyists made it known that Exxon might support some sort of carbon emissions
plan, such as a carbon tax.
The efforts to undermine popular support for a cap-and-trade bill were effective.
In late 2009, 57 percent of Americans believed there was strong evidence that global
warming was real, according to a poll from the Pew Research Center. While this was a
majority, it was a slimmer majority than in 2008, when 71 percent of Americans
believed it. In 2006, 77 percent believed it.
As the Senate debated, Koch Industries applied yet more pressure. While punishing
Congressmen who voted for Waxman-Markey, then tarnishing the bill through its
echo chamber, Koch employed another tactic. This tactic was informed by the
insight that Abel Winn had derived from his study of beating holdouts: When there’s
competition, that completely blew the problem away. . . . Everybody behaved much
better. Koch Industries would intensify competition among lawmakers by promoting
competitors to challenge them.
In 2009 and 2010, Koch Industries’ political network created new Republican
candidates, seemingly out of nowhere, who rose up and challenged sitting
congressmen and senators. Koch’s chosen candidates attacked the incumbents from
the right, claiming that the Republican Party was insufficiently conservative and too
accommodating of the Obama agenda. The overwhelming message was that
compromise with Democrats must end.
Bob Inglis was more surprised than anyone to find himself challenged by one of
Koch’s candidates. Inglis earned an 84 percent rating from the American
Conservative Union, which tracked lawmakers’ votes. He discovered that voting in
line with the union 84 percent of the time was not enough. Inglis was seen as a
holdout against Koch’s agenda because he stubbornly continued to advocate for
controlling greenhouse gas emissions.
Inglis’s competition came in May, and it arrived in the form of a prosecuting
attorney from Spartanburg named Trey Gowdy. Inglis and Gowdy had been
longtime allies and even friends. Inglis heard the news about Gowdy’s candidacy one
morning when afriend called and told him. He collapsed back into bed. Gowdy was a
formidable opponent. Koch Industries gave no money to Inglis during that campaign
cycle, but contributed at least $7,500 to Gowdy. Americans for Prosperity promoted
Inglis’s town hall meetings to Tea Party activists so that they could arrive to protest,
but there is no evidence that AFP directed such actions against Gowdy or questioned
his conservative credentials. Gowdy, in turn, proved that he would support Koch
Industries’ most important policy concern in the summer of 2009.
Inglis and Gowdy met at a candidate forum to debate the issues that summer, held
under a large tent next to a highway. The moderator was a conservative talk-radio
host. There were two other candidates with Inglis and Gowdy, but Inglis considered
Gowdy to be his only true competitor.
The moderator asked all the candidates if they believed climate change was manmade and then added: “Would you supporta bill that taxes carbon emissions?”
This drew a hearty laugh from the crowd. They knew exactly how painful Inglis’s
squirming must be. Inglis took the microphone and proceeded to alienate almost the
entire audience:
“I do believe that humans contribute to climate change. And, actually, let me
strike that. I don’t believe it. It’s not an article of faith for me. My faith tells me to
look at the data. The data says that’s happening. And that’s why I have a proposal
that’s not cap and trade.” He explained the details of a carbon tax bill and how it
would be “revenue neutral” by cutting taxes on wages.
When Gowdy rose to speak, he said succinctly, “No on cap and trade, no on
carbon tax.”
“I’ve been a prosecutor for sixteen years,” Gowdy continued. “I’m used to having
things proven to me and proving it to other people. Global warming has not been
proven to the satisfaction of the constituents that I seek to serve.”
Gowdy was interrupted by loud applause. The crowd kept applauding and
hooting while Gowdy took his seat.
Bob Inglis knew he was losing the campaign. What he didn’t know was that he
wasn’t alone. Koch Industries and Americans for Prosperity were replicating the
strategy in congressional districts across the country. In Washington, sitting
Republican lawmakers started talking nervously about being “primaried” by Kochfunded candidates. One wrong step could expose them to fierce competition. As
Winn might have predicted, everyone started behaving much better.
As it pressured Republican lawmakers from the outside, the Koch network built a
hard wall of “no” votes around the Waxman-Markey bill in the Senate to contain its
support.
Since at least 2008, Americans for Prosperity asked politicians to sign a pledge that
they would “oppose any legislation relating to climate change that includes a net
increase in government revenue.” It was phrased in a way to look like an antitax
measure rather than a promise to kill any effort to control greenhouse gas emissions.
But it achieved the same goal. Putting a price on carbon—through a cap-and-trade
system or a carbon tax—was seen as the most realistic way to control carbon
emissions. Only the federal government had the authority to impose that price, so
Koch’s pledge killed the effort in its tracks.
The “carbon pledge,” as it was called, was signed by 223 state and federal
politicians in 2009. One of them was the Indiana Congressman Mike Pence. Pence,
who had called climate change a “myth,” was the only member of the Indiana
delegation to sign the pledge. In this sense, Pence was a trailblazer. By September of
2010, four members of Indiana’s delegation had signed the pledge and a total of 627
state and federal lawmakers and candidates had done so.
As Koch Industries encircled the Waxman-Markey bill with its carbon pledge, the
Democrats put their energy into passing Obamacare, which was approved in the
Senate on Christmas Eve 2009 and signed into law in the spring of 2010. Then the
Democrats put their energy into the Dodd-Frank financial reform bill, which
imposed new regulations on Wall Street banks. It passed the Senate in May of 2010
and was signed into law in July.
The cap-and-trade bill languished during these months in the Senate, as the group
of senators led by John Kerry tried fruitlessly to find some sort of bargain that could
make the bill palatable to sixty senators. All through the spring and summer of 2010,
the political atmosphere grew hotter, stoked by AFP and other conservative groups,
and the issue of carbon regulation became more toxic.
This was the period when Bob Inglis was fighting in a primary election against
Trey Gowdy, set for June of 2010. Inglis refused to abandon his campaign slogan
“America’s sun is still rising.” Looking back, Bob Inglis said that there was one
moment when he should have realized he was going to lose. It happened to be the one
moment in his political career when he was most worried about being assassinated. It
happened during a town hall meeting in a public school near Inglis’s home in
Travelers Rest. Because the event was so close to his house, he brought his wife and
children. When they arrived, the crowd was so large that the local fire marshal was
turning people away. Even before Inglis started speaking, a crowd outside was getting
furious.
The atmosphere inside was even worse. The auditorium was stuffy and crowded
and full of raw anger. Inglis knew that many of his neighbors around Travelers Rest
carried guns on their person. He was certain there were many guns in the room that
night. When he took the stage, he began to give his stump speech. Under normal
circumstances, he would have pointed out his wife and children in the audience,
which was a standard gesture for a congressional candidate. That night, he didn’t do
it.
“I didn’t introduce my wife and kids because I was concerned about their safety.
You could just tell, in the pulsating anger in the place, that it wouldn’t be good to
introduce your wife and kids,” Inglis said. “If I was going to get shot, it probably was
going to happen there. At that town hall meeting.”
At the end of the night, a woman close to the stage yelled at Inglis: “We don’t trust
you anymore!”
If a congressman lost the trust of his voters, there was no recovering from it. When
the primary vote was held on June 22, Inglis attended a watch party with his
campaign staff in downtown Greenville. The event turned out to be a chance for Bob
Inglis’s close friends and family to witness the most public and humiliating defeat of
his political life. He lost the race with 29 percent of the vote to Gowdy’s 70 percent.
Inglis worried about what this might mean for future politicians. “I was really
quite sad about the rise of this populist fire that can only burn things down. It can’t
build anything up. I continued to be saddened that this fire, which I thought would
burn out, has only gotten hotter.”
It is difficult to identify the exact moment when the cap-and-trade bill died. There
was no vote to declare its final defeat. The measure simply lost momentum and then
died quietly. In late April of 2010, Lindsey Graham dropped out of the gang of
senators who were pushing the bill. No Republicans were willing to step in and
replace him. Harry Reid announced that the Senate would work first to pass
comprehensive immigration reform before addressing climate change.
Jonathan Phillips and the other staffers who’d written the bill knew that Reid’s
decision was a death sentence. The moment of opportunity to pass meaningful
greenhouse gas regulations had passed.
Americans for Prosperity emerged from the summer of 2010 in its strongest
position ever. Steve Lonegan, in New Jersey, had a hard time keeping up with the
organization’s growth. There were more people and more resources pouring in than
ever before. When Lonegan joined AFP, it was a political upstart, a group of outsiders
like a pirate crew, fighting to change government policy from outside the system.
This culture was rapidly disappearing, replaced by astreamlined, corporate model.
“In the early days, we were rambunctious. There were less controls,” Lonegan
recalled. “But as things got bigger and bigger, they had to put in more, like, lawyers
and bureaucracy. Though it was still effective, it did become somewhat more
bureaucratic. But I think that was out of necessity.”
As AFP solidified its position, it also began to entangle itself tightly with the
Republican Party and change it from within. AFP went on a hiring spree and
poached young and aspiring talent from the Republican Party. Two-thirds of all AFP
directors were drawn from it. Perhaps more importantly, roughly one-third of all the
AFP state directors who left AFP went directly from that job to positions in
Republican Party politics, taking with them their contacts and education from
Koch’s political operation.
The deep ties between AFP and the Republican Party were only discovered years
later, when two Harvard political scientists, Theda Skocpol and Alexander HertelFernandez, conducted one of the only rigorous independent studies of the newly
expanded Americans for Prosperity network. “These data show that the AFP
federation has been able to penetrate GOP career ladders,” Skocpol and HertelFernandez wrote. The employees who went back and forth tended to be “young men
in their thirties or forties” who would presumably have long careers in politics ahead
of them.
AFP was reshaping the Republican Party and strengthening it at the same time. In
2010, the Koch network shifted its focus from fighting the Waxman-Markey bill to
electing as many Republicans as possible in the midterm congressional election.
In November, a wave of votes from Republicans and Tea Party activists destroyed
the Democratic majority in the House of Representatives. Republicans also made
strong gains in the Senate, although it didn’t win control. The era of the Democratic
supermajority of sixty votes was firmly buried. The filibuster would once again
become a remarkably powerful tool of opposition. Now, if Harry Reid wanted to
pass a bill, he would need Republicans to join a vote to end a filibuster debate. This
was a possibility of vanishing likelihood.
The magnitude of this victory was immense for Koch Industries. Of the eightyfive newly elected Republicans who arrived in Washington, seventy-six had signed
Americans for Prosperity’s carbon pledge, vowing they would never support a federal
climate bill that added to the government’s tax revenue. Of those seventy-six
members of Congress, fifty-seven of the signees had received campaign contributions
from Koch Industries’ PAC, according to an analysis by the Investigative Reporting
Workshop at American University. Koch Industries had terminally stalled the
Waxman-Markey bill in the Senate, and now it had salted the earth behind it,
ensuring thata new climate change bill would never grow.
One of the earliest acts of the new Republican majority was to halt funding for the
Select Committee on Energy Independence and Global Warming. The team began to
box up their files and personal belongings and emptied out the basement office of the
Longworth Building.
Jonathan Phillips, the young staffer who’d written sections of the bill to promote
renewable energy, left Congress and took a job with the US Agency for International
Development. He traveled to Africa and helped companies there build new clean
energy infrastructure. Two of the legal experts on the team, Michael Goo and Joel
Beauvais, moved to the EPA, where they started working on a plan to regulate carbon
emissions from coal-powered utility plants. The EPA rule, called the Clean Power
Plan, was the closest thing to a carbon control law that officials in the Obama
administration felt they could achieve. Americans for Prosperity quickly caught wind
of this and immediately began recruiting opposition to it through its website.
In the absence of regulation, greenhouse gas emissions continued to soar. In 2011,
humans emitted 32.27 billion tons of carbon into the atmosphere, a rate that was
more than 150 times what it had been before the industrial revolution.
Concentrations of carbon in the atmosphere rose every year after the death of the
Waxman-Markey bill. Scientists had warned that humans should strive to keep
carbon dioxide levels at 350 parts per million to avoid catastrophic environmental
impacts. As the Waxman-Markey bill was debated, carbon levels hovered around 370
parts per million. Within five years of its failure, levels hovered at 400 parts per
million, the highest ever recorded during human existence.
After he left politics, Bob Inglis formed a group that promoted free-market
solutions to the problem of climate change. His view remained unpopular in
Republican circles. And everywhere he went, Inglis had that nagging feeling from
2010, when he had looked at the back of a town hall meeting and seen someone with
a video camera, mounted on a tripod, filming him, someone “that maybe had a little
bit of help, you know what I mean?”
Someone still seemed to be helping.
Inglis attended a debate over climate change policy in Washington, DC, hosted in
part by the Libertarian Reason Foundation. When he arrived, Inglis found something
curious. On each empty seat had been placed a campaign-style button. The buttons
read simply: “70–29.” This was the vote margin by which Inglis had lost to Trey
Gowdy, 70 percent to 29 percent.
The buttons stuck in Inglis’s mind. Someone had to print them, pay for them, and
disperse them over the empty seats. Things like that took money and coordination. A
couple of years after he was kicked out of office, Inglis finally had a strong suspicion
as to who could do that. When he held the button, one thought crossed his mind:
“It seems to me that it has Koch written all over it.”
Charles Koch had reason to be exultant as 2010 came to a close. Koch Industries had
faced an unprecedented economic threat in the form of the Waxman-Markey bill and
had played a vital role in derailing it. His own political ideals had faced an
unprecedented threat in the seemingly permanent Democratic majority in
Washington and the popularity of the Obama agenda. He played a vital role in
destroying it. Koch’s political operations were larger, more influential, and more
powerful than ever.
But Charles Koch still felt threatened. He felt that the fight was still in its early
stages. There was no time to waste with victory parties. On September 24, he sent a
letter to wealthy political donors whom he was hoping to enlist in his cause.
“Everyone benefits from the prosperity that emerges from free societies. But that
prosperity is under attack by the current administration and many of our elected
officials,” Charles Koch wrote. “We must stop—and reverse—this internal assault on
our founding principles.”
The letter was an invitation to Charles Koch’s eighth private gathering for wealthy
conservative donors and the politicians who sought their help. The conference was in
January of 2011 ataresort near Palm Springs, California.
Security around the donor conference was intense. Attendees registered for the
event by contacting the Koch Industries lobbying office in Washington, DC, rather
than the host hotel. When attendees arrived, they were required to wear an
identification badge at all times. They were also warned not to leave materials behind,
or to post on social media while they were at the event. No one from the media was
allowed inside.
Charles Koch had a pithy piece of wisdom that he liked to share with his political
operatives. It was a saying about whales and harpoons. “The whale that comes above
sealevel gets harpooned,” is how one person remembered it.
The allegory was clear. It was safer to remain below the surface. It was better for
Koch’s political operations to remain anonymous. This helped explain the
complexity of Charles Koch’s emerging political organization, the endlessly
complicated interlocking network of shell organizations and secret donations. It also
explained the security and secrecy around the donor meetings that Charles Koch
hosted twice a year.
The events had grown larger and more lavish since 2006, when Steve Lonegan
attended one of the earliest conferences in Aspen. Since that time, the events had
been attended by Supreme Court justices Antonin Scalia and Clarence Thomas;
GOP congressmen Mike Pence, Tom Price, and Paul Ryan; Republican governors
Bobby Jindal and Haley Barbour; and celebrity speakers like Rush Limbaugh,
Charles Krauthammer, and John Stossel. At the summer conference of 2010, one of
the keynote speakers was the Tea Party leader Glenn Beck, whose speech was entitled
“Is America on the Road to Serfdom?”
But secrecy was becoming difficult to maintain. Americans for Prosperity was one
of the most influential political organizations of 2010. A number of investigative
reporting outlets began to dig into Charles and David Koch’s long history of political
involvement, including the Center for Public Integrity and the Investigative
Reporting Workshop at American University. Both groups published deep reports
that outlined the Koch brothers’ extensive political donations. Activist groups took
note as well. In March of 2010, Greenpeace released its forty-three-page report
entitled Koch Industries: Secretly Funding the Climate Denial Machine, which
detailed Koch’s extensive giving to groups like the Mercatus Center, the Cato
Institute, and the Competitive Enterprise Institute.
The publicity culminated in August of 2010 when the New Yorker magazine
published a detailed report of Koch’s political history, with contemporary accounts
of Americans for Prosperity’s coordination with Tea Party activists. The article,
“Covert Operations: The Billionaire Brothers Who Are Waging a War Against
Obama,” was written by Jane Mayer, one of the most prominent investigative
reporters in America. It cemented the Koch brothers’ role as public figures who were
deeply influencing political affairs. A widespread narrative raced through American
politics, a narrative that the Koch brothers hadn’t just assisted the Tea Party but had
created it. The story line was inflamed by the 2010 Supreme Court decision Citizens
United v. Federal Election Commission, which lifted restrictions on campaign
donations to independent political groups. This opened the gates for unlimited cash
to be poured into the third-party groups that Koch became masterful at employing. It
appeared that there were no constraints on the political power that billionaires could
wield. The Koch brothers were seen as the primary beneficiaries of the new landscape.
The whale had breached. The harpoons began to fly. When Charles Koch arrived
in Rancho Mirage for the eighth donor conference, he found that the veil of secrecy
had been lifted for good. Roughly a thousand protestors were gathered outside the
Omni Rancho Las Palmas Resort & Spa. The resort was a collection of low-slung
buildings built in the style of adobe haciendas, encircling a pool and a golf course.
The protestors filled the street just outside, standing between the row of palm trees
that swayed in the placid breeze. Security officers stood on the hacienda roof, looking
down at the crowd, while cordons of local police officers in riot gear squeezed the big
crowd inward from the sides. The police justified their militarized presence based on
the fact that there were several federal judges inside the resortat Koch’s gathering.
The protestors were raucous and wore brightly colored costumes. They carried big
banners that read: “Quarantine Koch,” alongside neon biohazard symbols. They
carried placards that read: “Uncloak the KOCHS!” and “TEA PARTIERS ARE
KOCH SUCKERS!” They chanted and sang songs into loudspeakers.
The din could be heard throughout the resort. But inside the conference rooms,
the seminar proceeded. Charles Koch made it clear to the attendees that the event was
not a junket; not “fun in the sun,” as he put it. The gathering was a work trip, a
chance to press their strategy. He spoke about the political struggle in nearly
apocalyptic terms. At a donor conference in 2011, he told the crowd that America’s
future could literally be endangered if Barack Obama won reelection. “This is the
mother of all wars we’ve got, over the next eighteen months, for the life or death of
this country,” Koch said.
Charles was the star of the seminars, but he was a reticent one. He didn’t like the
business of shaking hands with politicians and getting his photo taken with them.
When given the chance, he passed up opportunities to meet even very senior political
leaders who asked for one-on-one time with him. If anything, he seemed to look
down on them.
“I remember talking to him. I think he viewed the folks in Congress as victims of
the system. I know he did,” said one person familiar with Koch’s political operations.
Charles Koch, who prized long-term thinking and who preached about the
importance of creating incentive systems and bonus payments to reinforce it, looked
at Congress and saw a dysfunctional system that was riven by toxic incentives.
Politicians were just caught up in that system. They almost couldn’t help but do the
wrong thing.
“He understood what the process was. You have members of Congress. They get
elected every two years. And it’s hard to be independent. It’s hard to get things done.
It’s hard not to spend a lot of time being political and raising money. And he just—I
think he saw the system as broken,” the person said.
The political machine that Charles Koch built was immensely successful—not at
fixing this broken system, but at ensuring that it remained hobbled and incapable of
passing the kind of sweeping business regulations that defined the New Deal. He
applied long-term thinking to a system defined by short-term election timetables, and
he won many of the most important fights he cared about.
After the Palm Springs conference wrapped up, Charles Koch traveled back to
Wichita. He reported for work at the Koch Tower and found paperwork waiting for
him in his executive suite on the third floor. While he spoke about politics in terms of
war and destruction, the state of affairs inside Koch Industries told a different story.
One of the surprising truths about life under the Obama presidency was that it was
very good, economically speaking, for Charles Koch and Koch Industries.
During the Obama years, Charles Koch’s net worth doubled. His fortune would
grow larger and faster than during any previous period. One reason for this explosion
in wealth was the death of the cap-and-trade bill. There would be no price on carbon
to constrain the fossil fuel business. Instead, the new drilling technique called
fracking would help enshrine fossil fuels as a central part of American economic life.
Koch Industries stood at center stage during this shift in America’s energy
industry, and it reaped rewards in ways that people on the outside could not see.
When it came to the business side of Charles Koch’s life, the whale was still deep
underwater, growing larger and more powerful than ever before.
I. No version of the Affordable Care Act ever proposed to implant a microchip in every American. The theory
that such a provision was part of the law appears to be based on early draft versions of the bill that were never
passed. The proposal would have allowed the US Department of Health and Human Services to collect data on
medical devices like pacemakers. This data collection would have helped speed recall notices of such devices and
could also help gauge their efficacy.
II. This story was not true. When Pelosi became Speaker of the House, she was afforded the use of a military
aircraft to travel to her home district in California. She did request a plane that was larger than that of her
predecessor, Republican Dennis Hastert. He had used a smaller plane because his home district was in Illinois,and
the smaller plane could not make the trip to California without refueling.
III. The other three pillars were: media outreach, litigation,and political influence (or lobbying).
IV. The connection between IER and the Institute for Humane Studies was first revealed by the journalist Lee
Fang. He reported in 2014 that the IHS temporarily lost its charter,and then reformed as the IER.
V. Greenpeace’s analysis might overstate Koch’s support for so-called climate-denial groups. Greenpeace’s tally
includes the total funding for entities like the Cato Institute, which created doubt about climate-change science
but which also engaged in other antigovernment activities. Still, the difference in funding is so dramatic that it
seems almost certain that Koch invested more than Exxon did during this period.
CHAPTER 21
The War for America’s BTUs
(2010–2014)
In the winter of 2010, while the cap-and-trade bill was languishing in the US Senate,
Koch Industries began to quietly execute a series of business deals. The deals might
have looked strange—maybe even irrational—to outsiders. In March of 2010, for
example, Koch announced that it was expanding its pipeline capacity in southern
Texas by 25 percent. This was akin to building a very large parking garage outside a
shopping mall that no one visited anymore. Southern Texas was a sleepy backwater of
the oil business, an oasis of barren scrub brush and scattered towns with lonely oil
derricks. Oil production in South Texas had stagnated for years. But Koch was
spending millions to increase its pipeline network there.
In the following months, Koch’s series of deals accelerated. In September, Koch
announced a partnership with an obscure company called Arrowhead Pipeline to
move 50,000 barrels a day of crude oil out of southern Texas. This was roughly half
of the entire region’s production at the time. Then, a month later, Koch announced a
partnership with another little-known firm, called NuStar Energy, to reopen sixty
miles of defunct pipeline, to carry 30,000 barrels of oil a day.
In November, Republicans won control of the US House of Representatives. A
month later, Koch announced another deal, this one the largest yet—the company
would build a brand-new sixteen-inch pipeline from remote Karnes County, Texas,
to Koch’s refinery in Corpus Christi, capable of carrying 120,000 barrels of crude oil
a day. The new pipeline had the potential to be expanded to carry up to 200,000
barrels a day. In February of 2011, another deal: Koch bought the Ingleside Pier in
Corpus Christi, an export terminal through which Koch could ship 200,000 barrels
of oil a day on barges. Two months later, Koch announced a new twenty-inch pipe
running from Pettus, Texas, to Corpus Christi, capable of carrying 250,000 barrels a
day.
These deals garnered very little attention. There were a few corporate press releases
and small stories in local media outlets. What outsiders didn’t realize was that Koch
Industries had just built a superhighway for crude oil, carrying hundreds of
thousands of barrels a day from southern Texas to Koch’s refinery in Corpus Christi,
with an off-ramp at the Ingleside Pier that could carry excess supplies to foreign
markets.
The puzzling part about this superhighway was that it was built to carry oil
supplies that didn’t seem to exist. The highway began in a region of Texas called the
Eagle Ford Shale. Production there had been flat. In fact, the one accepted truth
about US oil production was that it had peaked in the early 1970s and would never
again increase. The Eagle Ford region was no exception. In 2007, there were fifty-one
oil-drilling rigs in Eagle Ford, producing about fifty-four thousand barrels of oil a
day. By late 2008, there were sixty-two oil rigs in the region, producing fifty-seven
thousand barrels a day. In 2010, Eagle Ford’s production actually fell to about fiftyfive thousand barrels a day.
Nonetheless, Koch was building a system to move hundreds of thousands of
barrels of crude from the region. These deals were part of a strategy that Koch had
been formulating for over a year. Koch saw something in Eagle Ford. It was
something that others also saw, but that Koch was the first to exploit. While
production was flat until early 2010, the number of drilling rigs had more than
tripled in just over a year, from thirty to 104. This number was a leading indicator.
The wells would start pumping, and new oil would start to flow. Koch Industries was
poised for the change.
The wells being drilled into southern Texas were the face of an energy revolution
that would redefine global oil markets and the American economy. They were part of
a once-in-a-generation transformation that crept up quietly and then changed
everything. In one short decade—from 2005 to 2015—America went from being the
largest importer of refined petroleum products to the largest exporter of refined
petroleum products. A country that was once the poster child for peak oil discovered
that it was home to oil and natural gas deposits that were likely larger than those
found in Saudi Arabia. The entire story about fossil fuels was reversed before many
people even realized what was happening. These changes were every bit as cataclysmic
for oil markets as the OPEC embargo had been in the 1970s. But this time, the
changes accrued to America’s benefit. The cost of oil plummeted, OPEC was
defanged, and America became essentially self-sufficientas an oil consumer.
The revolution was catalyzed by a suite of oil-drilling technologies that were used
together in a drilling process called hydraulic fracturing, or fracking. Fracking had
been around for decades, although it was fatally unprofitable. The method was kept
on life support only by giant and long-lasting government subsidies and tax breaks.
Fracking only became commercially viable thanks to the oil price spikes of 2007 and
2008. When fracking became widely deployed, it opened up massive fossil fuel
reserves in the United States that were long considered unattainable.
This revolution, while far reaching, did not change one important element of the
energy business. The revolution did not change who benefited most from the energy
business (at least during its first decade). The fracking economy was new, but the
primary beneficiaries were old. The companies that benefited most were the longstanding legacy players, like Koch Industries.
The fracking boom played to Koch’s advantages, and one of these key advantages
was Koch’s capacity to thrive in volatile markets. The fracking boom unleashed a
period of almost unprecedented volatility between 2010 and 2014. Koch Industries
was built to respond to volatility, and its expertise was evident in Koch’s hidden effort
to build the oil superhighway out of the Eagle Ford region.
The effort began when Koch’s commodity traders started to receive early signals
that something big was about to happen in oil markets.
The first signals emerged on the natural gas trading desks sometime around 2009.
This is when the advent of the fracking boom was first detected.
The previous two years had been wildly unstable. In 2007 and 2008, crude oil
prices spiked to record highs. Natural gas followed crude oil upward, as it tends to do.
Energy prices crashed during the recession due to weak demand, which was
predictable. But then something strange happened: oil prices started to climb again,
but natural gas prices didn’t follow them upward. Instead, gas prices started to slide.
Then fall. Then collapse.
The reason for this was startling. Natural gas supplies, long thought to be growing
scarcer every year, had suddenly started to increase. In late 2009, the United States
produced 1.65 trillion cubic feet of natural gas a month. In two short years, the
supply skyrocketed by 23 percent, reaching 2.03 trillion cubic feet a month in 2011.
And this wasn’tafluke. By 2015, the supply would reach 2.3 trillion cubic feet.
This was the start of the fracking revolution. Fracking is a shorthand term that
refers to a group of three technologies that, when used together, make it possible to
extract natural gas deposits that were once unreachable. The first technology is called
microseismic imaging, a system used to map underground gas deposits trapped in
dense shale rock. Shale gas deposits were previously considered unattainable because
of their weird formation: the deposits are composed of broadly diffused gas droplets
trapped in rock. The deposits are shaped like a giant dinner plate—wide and shallow.
Drilling into them is like punching a nail through the plate, which allows the drill to
tap atiny portion of the gas.
This is where the second technology comes in: horizontal drilling. With horizontal
drilling, the nail could penetrate the dinner plate and then make a sharp right turn,
traveling through the heart of the entire deposit. The final technology was a group of
chemicals, known as proppants, that could be injected into the shale rock along with
sand, dislodging gas and allowing it to be sucked to the surface. When gas became
expensive in 2007, it finally justified the expensive process of extracting it through
fracking.
The earliest waves of the fracking boom came as a surprise to Koch’s leadership
team. The boom was catastrophic for gas prices, which fell roughly 85 percent
between 2008 and 2012, from a peak of $12.69 per million BTUs (or British thermal
units, a metric that’s widely used as the basic measurement of energy use) to a mere
$1.95. As it turned out, this catastrophe played to Koch’s advantage because natural
gas is the primary ingredient for nitrogen fertilizer. When prices fell, Koch was
suddenly able to make its fertilizer for a fraction of the cost. It was a breathtakingly
lucky break. Retail prices for fertilizer stayed high because of strong demand from
farmers, who needed fertilizer more than ever to keep production high. When gas
prices and production costs collapsed, Koch’s profit margins swelled. Koch was the
fourth-largest fertilizer maker in the United States thanks to its purchase of
Farmland’s fertilizer plants in 2003, for pennies on the dollar. Now those plants were
printing cash.
Still, Koch’s senior management was uneasy. They hadn’t seen it coming.
“You look back and go, ‘Yeah that was obvious! How’d I miss it?’” said Steve
Feilmeier, Koch Industries’ chief financial officer. “We started reflecting on ‘How did
we miss that?’”
This reflection occurred largely in the offices of Koch’s crude oil and refinery
division, Flint Hills Resources. Once they began looking into the fracking business,
Koch’s managers began to anticipate where it might go next. They missed the advent
of new gas supplies, but it helped them see the next step. Brad Razook, who was CEO
of Flint Hills, had reason to believe that the fracking revolution wouldn’t stop with
natural gas deposits.
Brad Razook and other senior executives at Flint Hills worked in windowed offices
that ring the top story of the Tower, offering them views of downtown Wichita to
the south and flat grasslands and suburban subdivisions to the north. The middle of
the top floor is filled by a sprawling maze of cubicles. This is where Flint Hills’ traders
work.
The trading pit could easily pass for a branch office of any insurance company in
central Kansas. No one was shouting orders or waving their hands in the air. There
was just the quiet murmur of people on the phone. The beige dividing walls between
desks were decorated with drab attempts to individualize each cubicle, like cardboard
cutouts of the Wichita State University mascot—a scarecrow-like figure called
WuShock—and family photos. The only signs of the global reach of the young
traders were the multiple computer monitors at the desks, flashing with numbers and
charts. A set of clocks along one wall display the local times at trading hubs around
the world.
Koch’s young traders observed odd occurrences in oil markets during 2011. The
traders who bought oil supplies for Koch’s Pine Bend refinery observed chaos in local
midwestern markets. New supplies were coming into the market from North Dakota,
of all places, causing supply gluts, bottlenecks, and transportation problems. And all
of this was happening in a region where the oil industry had been dead for decades.
The new oil coming out of North Dakota was similar to the new natural gas supplies:
they were drilled by frackers in a region called the Bakken Formation. A fountain of
crude oil sprang up in the Northern Plains, and no one knew how to deal with it. “It
was almost comical how much crude was coming online,” said Tony Sementelli, Flint
Hills’ chief financial officer. “It was very curious to us because it was almost
unthinkable.”
Razook and Sementelli started holding meetings to figure out what was going on.
The signals from the marketplace were confusing. Fracking had already opened new
pools of natural gas. But the big question was whether the process could be repeated
with crude oil. The oil glut in North Dakota was an uncontrolled experiment to
answer this question. But the results from that experiment raised only more
questions. If fracking could work in North Dakota, could it work elsewhere? If it did
work, how large were the oil reserves that might be tapped for drilling?
When faced with this uncertainty, Razook responded in a way that reflected
twenty years of training. Razook had joined Koch Industries in 1985, after graduating
from Kansas State University with an undergraduate degree in business
administration. His real education came at Koch University. His education included
the lessons of Charles Koch’s mentor, Sterling Varner, who told his rank-and-file
employees to keep their eyes open for opportunities at all times. By 2010, Sterling
Varner’s wisdom had been formalized into a routine process. Koch’s traders reported
what they saw, then Razook and Sementelli shared what they were learning, and
Koch Industries moved fast to exploit the opportunity.
Razook reassigned one of his most important employees, Brad Urban, to study
fracking full-time. Eventually Urban’s team grew to include more than a dozen
people. They studied the North Dakota market and explored where the fracking
boom might lead next. They wanted to discover the next Bakken Formation before
anyone else.
One reason why the fracking boom caught everyone by surprise was that fracking had
been around since the 1970s. The technology failed to deliver any meaningful results
for forty years. It was simply too expensive to be economically viable. Fracking, in
fact, was only kept alive thanks to repeated government intervention. The fracking
industry was essentially a ward of the state for decades, kept alive by lavish
government subsidies, tax breaks, and government-funded research.
In 1980, a federal law called the Crude Oil Windfall Profits Tax Act included a tax
break for natural gas supplies produced in unconventional ways, like fracking. The
purpose of the tax break was to nurture new energy sources. The tax break was
stupendously generous, providing 50 cents for every thousand cubic feet of gas. The
so-called Section 29 tax break remained in place for decades. The National Bureau of
Economic Research estimated in 2007 that the tax break would cost the federal
government $3.4 billion between 2007 and 2011 alone.
The federal government also stepped in to support the frackers with long-term,
expensive, experimental research. It was the kind of research that private companies
were reluctant to provide for risky technologies. The government-run Sandia
National Laboratories developed the three-dimensional microseismic imaging that
made fracking possible. A federal project called the Morgantown Energy Research
Center, or MERC, partnered with companies to set up experimental drilling
operations to put fracking to the test. It was two engineers with MERC who
patented the vital technology to drill horizontally—or directional drilling, as the
industry called it. In 1986, a Department of Energy program, partnered with private
companies, was the first to demonstrate a multistage, horizontal fracture in the
Devonian Shale.
In spite of all this help, fracking never turned a profit. It was a marginal industry
populated by dreamers and wildcatters who were promising big returns, kept alive by
welfare benefits.
This changed quickly in 2009. Business and government partnerships figured out
how to make the fracking process ever cheaper. Then, the price spike of 2008 made
fracking competitive. After that, the industry gained steam and a self-reinforcing
momentum. Banks started to give loans to frackers, from Pennsylvania to North
Dakota, and these frackers turned their eye to new reservoirs of fossil fuel.
Brad Urban and his team canvassed the industry. Koch’s traders bought oil
supplies and quizzed the drillers. By doing so, they discovered the next horizon for
the fracking business. It was something called tight oil. This was crude oil trapped in
porous rock. Tight oil tended to be extremely “light” crude, meaning that it had low
sulfur content, which differentiated it from heavy-sulfur oil of the kind that was
imported from overseas.
As it happened, Koch’s refinery in Corpus Christi specialized in refining light
crude. It also happened to be that one of the biggest deposits of light, tight oil was in
located in southern Texas, near Corpus Christi’s backyard. Oil drillers told Koch
about an area called the Eagle Ford Shale, a crescent of land that curved from
southwest Texas up through the big empty space between San Antonio and Corpus
Christi.
Koch started to gather estimates of how much oil might be retrievable through
fracking in Eagle Ford. The region produced about fifty-five thousand barrels a day
before the frackers arrived. It might produce as much as a hundred thousand barrels a
day—maybe two hundred thousand—when new wells were installed. Before long,
people were talking about five hundred thousand barrels a day.
I Urban’s team hired
an outside geologist to study the land and try to triangulate the truth between the
boasts of various wildcat drillers. The team at Flint Hills came to believe thataflow of
at least two hundred thousand barrels a day was realistic.
The Koch team began to formulate a plan. Koch planned to capture and ship as
much of the tight oil as it could get from Eagle Ford, and send it to Corpus Christi. It
seemed likely that a sudden glut of supplies from Eagle Ford would create a surplus,
just the kind of bottleneck that Koch had seen in the Bakken. That meant that the oil
would be cheap. If that happened, Koch’s Corpus Christi refinery might suddenly
turn into a second Pine Bend refinery—a facility that could buy unusually cheap
supplies thanks to a local oversupply and then sell gasoline into expensive retail
markets.
Koch had an advantage over other refineries in Corpus Christi due to an accident
of history. A majority of the refineries around Corpus Christi processed mostly
imported oil, which was heavy in sulfur. Over the years, these refineries invested
millions to install equipment specialized for refining the heavy, sulfur-rich crude.
Koch was an outlier in this respect. The Corpus Christi refinery processed more light
oil because that’s what it used as a feedstock for its chemical plant that made
paraxylene. In other words, Koch was perfectly poised to accept a new surge of light
oil. Its competitors wouldn’t be able to process the new supplies.
There was a risk, however. The frackers were just starting to move into Eagle Ford,
and the market was up for grabs. There was a good chance that the frackers would sell
their crude to refineries in the Houston area. If Koch Industries wanted the oil to
flow to Corpus Christi, the company had to move fast. Razook and Sementelli
started talking to engineers to figure out how much it would cost to build a new
network of pipelines between Eagle Ford and Koch’s refineries. All of the estimates
came back at “plus or minus 100 percent,” meaning the cost was either going to be
the estimated price or about double the estimated price. Koch, and other companies,
liked to fund projects with a plus or minus 10 percent risk factor.
After months of study, Razook, Sementelli, and Urban had a plan. They wanted
to build pipelines to a region where they didn’t know how much oil there might be,
for a cost they couldn’t estimate. Corporate planners were accustomed to having
some variables in their plan. But this was different. “Everything in this project was a
variable,” Sementelli said. Nonetheless, they were ready to take the project to Charles
Koch.
Koch Industries’ boardroom was still located across the hall from Charles Koch’s
office. Visitors walked into a spacious lobby on the third floor of the Tower, passed
by a bust of Fred Koch that sat on a pedestal, and turned left to walk into the
chamber. The room had no windows and dark wood paneling that created an almost
claustrophobic feel, as if the attendees inside were in a diving bell. Recessed lighting
in the ceiling shined down on a large, wooden table that dominated the center of the
room. The table was shaped like a ring, with a hollow center in the middle, and it was
surrounded by wheeled office chairs. This is where Koch’s business leaders presented
their ideas.
Razook and Sementelli pitched their plan to Charles Koch, David Robertson, and
Steve Feilmeier. They explained how the Eagle Ford Shale would likely surge with
new tight oil production in the coming years, and how Corpus Christi was poised to
refine the cheap supplies. The parallel to Pine Bend—Koch’s cash cow for so many
decades—didn’t even need to be emphasized. “They certainly understand a feedstock
advantage,” as Sementelli put it.
Razook and Sementelli’s plan was uncertain, risky, and carried a dangerously
vague price tag. The pipelines alone would cost hundreds of millions of dollars. Or
maybe double that.
Charles Koch and his team seemed to understand the play instantly. They
encouraged it. “We didn’t have to sell,” Razook recalled.
“They were just wanting to make sure we were thinking big enough,” Sementelli
remembered.
They went big on the plan. They formed the partnerships, expanded the pipeline
network, and they bought the export pier. Then they reached out to the oil drillers
they knew in Eagle Ford and started signing contracts to buy all the oil these drillers
could provide. Koch’s pitch to these drillers was enticing. Koch would provide the
pipelines for transport. The company would provide the refinery to process the
crude. And if the drillers didn’t want to sell the oil to Koch, Koch could provide the
export terminal for drillers to sell their crude for export.
By 2011, Koch had invested hundreds of millions in pipelines and signed contracts
to ship hundreds of thousands of barrels a day. This investment was entirely a
gamble. If Eagle Ford was a failure, the investment would be a total loss. Koch would
own miles of worthless pipeline traversing miles of desolate scrub brush.
“It was hundreds of millions [of dollars] in the logistics phase,” Sementelli said.
“That was all risk. I mean, we didn’t really know alot of the variables.”
Then the oil started to flow.
The Eagle Ford region produced 82,000 barrels of oil a day in July of 2010. At the
end of the year, it was producing 139,000 barrels a day.
At the end of 2011, Eagle Ford produced 424,000 barrels a day. This turned out to
be nothing.
In late 2012, Eagle Ford produced 811,000 barrels a day. This was more than
fourteen times what it yielded before the frackers arrived.
At the end of 2013, production hit 1.2 million barrels a day.
At the end of 2014, it hit 1.68 million barrels a day. The oil that flowed out of
Eagle Ford each day was equal to almost 20 percent of all the oil produced in the
United States, even back at the peak of production in 1970. Eagle Ford’s production
was equal to roughly one-third of all US production in 2008.
The fracking revolution was shocking, overwhelming, and transformative to oil
markets. It created an entirely new energy economy. It wasn’t just the size of the new
oil reserves that changed everything—it was the structure of the new fracking
industry. Since at least the 1960s, the oil business had been controlled by large,
centralized cartels, from the group of companies known as the Seven Sisters to the
national oil producers in OPEC. Cartels like OPEC could more or less change oil
output on command. Saudi Arabia, in particular, had the ability to turn off the
spigots or ramp up production, depending on the Saudi monarchy’s wishes. But the
American reserves were tapped by thousands of independent drillers. Nobody was in
control. When it looked like the world was oversupplied with oil, the frackers weren’t
willing to shut off their wells and wait for prices to climb. Instead, each driller hung
on as long as possible and sold whatever they could into the market. A fracking well
only shut down when there was no other alternative. This feature of the fracking
business would depress oil prices for years. Even when the oil prices fell by half during
a crash in 2014, many frackers kept pumping. And those who stopped were only
waiting in the wings to get back in business. The world oil markets, once
characterized by terrifying scarcity, were now dominated by stubbornly high supplies
coming out of the United States.
While this was transformative, not everything in the oil business changed so
dramatically. When the tidal wave of new US oil supplies finally arrived, the wave
crashed into a refinery system that had not changed in fundamental ways, in more
than forty years. The refinery system was a narrow bottleneck that choked off the
flow of oil in unpredictable ways, delivering profits for refinery owners that beat the
world average by an order of magnitude. This bottleneck was the segment of the
energy industry where Koch Industries excelled, and it was critical to Koch’s play in
Eagle Ford.
Along the Gulf Coast of Texas, the most pristine skylines were the white towers of
the oil refineries. The refinery town of Port Arthur, for example, was a humble
collection of crumbling stone buildings, bandaged with sheets of plywood over
broken windows. The sidewalks were jagged with weeds and cracked cement. Many
of the houses needed paint jobs and new roofs. But when one left town and drove
along the coast, the vast, white towers of the oil refineries appeared like a mythical
city. These self-contained cities behind tall fences and barbed wire were active around
the clock, steam pouring from the towers during the day and lights twinkling on their
crowns throughout the night. It seemed impossible to imagine how much money was
made inside their perimeters.
Nobody had built a major new oil refinery in the United States since 1977. In that
year, when Jimmy Carter was president, a new refinery in Garyville, Louisiana, went
into production. This marked the last time a major new competitor entered the
refining market.
The primary obstacle to building a new refinery was the Clean Air Act, which
required new facilities to comply with pollution standards that existing refineries
were allowed to avoid. As outlined earlier, the existing refineries exploited a provision
of the Clean Air Act called the New Source Review, which allowed them to expand
their old refineries in ways that skirted the onerous pollution controls applied to new
refineries. The Department of Justice came close to charging the refineries with
violating the Clean Air Act but instead allowed them to stay in business with more
stringent controls. The legacy refineries, including Koch’s, have operated under that
consent decree ever since. While the consent decree might have helped curb
pollution, it did nothing to foster competition in the refinery business. The Clean Air
Act froze the game board of refining competition, leaving only the incumbent players
in place. They were left to divvy up the business among themselves.
During the 1980s, ownership of the nation’s refineries consolidated into fewer
and fewer hands. After the Reagan administration loosened antitrust enforcement, a
wave of mergers swept through the industry. The mergers accelerated during the
Clinton administration. Between 1991 and 2000, there were 338 mergers among oil
refiners. The consolidation continued through the Bush administration.
In 2002, there were 158 refineries in the United States. By 2012, there were only
115 producing fuel.
II From administration to administration, Democratic to
Republican, it seemed like the federal government did all it could to ensure that no
new refineries entered the market. A company called Arizona Clean Fuels attempted
to build a multibillion-dollar refinery, starting in 1998, to help ease tight supplies in
the Southwest. The project was hindered by years of permit disputes. Even by 2009,
the company was still promising to break ground. In 2011, the project seemed dead,
but it was revived. By 2018, there was talk that the refinery might be built, but
regulatory hurdles still remained.
Fewer and fewer companies refined oil, and they did it at larger and larger
facilities. Even without new refineries, US refining capacity increased between 2002
and 2012 from 16.5 million barrels a day to 18 million barrels a day.
While the refiners were processing more oil, however, there was evidence that they
increased production just enough to keep up with rising demand, and no more.
There was no incentive to increase capacity to the point where it might bring gasoline
prices lower.
By 2004, the refining industry was already “imperfectly competitive,” according to
a report from the US Government Accountability Office. The report found that
refiners had tremendous market power and that “refiners essentially control gasoline
sales at the wholesale level.” The GAO investigation found that the consolidation
made gasoline more expensive for consumers. The increased market concentration
“generally led to higher prices for conventional gasoline and for boutique fuels,” the
report concluded.
By the time the Eagle Ford tsunami arrived, US oil refineries were running full tilt,
processing just enough oil to keep up with demand for gasoline. By 2016, US
refineries ran at an average of 90 percent of their total capacity, compared to the
global average of 83 percent. Only India ran its oil refineries at a tighter capacity.
There was simply no excess capacity in the system, and no new companies willing to
enter the business and pick up the slack.
The bottleneck was severe. By 2015, even ordinary refinery outages caused
catastrophic price increases for gasoline. That summer, BP partially shut down its
refinery in Whiting, Indiana, to repair aset of leaky pipes. The closure caused gasoline
prices in Chicago to spike by 60 cents a gallon, while gasoline prices rose throughout
the surrounding region. It was the biggest such price hike since Hurricane Katrina
decimated the Gulf Coast in 2005. Capacity was so tight that even routine repairs had
hurricane-like effects.
In this environment, the profitability of US refiners was breathtaking. In 2010, the
average profit margin to refine a barrel of crude oil in the United States was roughly
$6 a barrel, by far the highest in the world. The next-highest profit margin was in
Europe, where it was about $4 a barrel. One year later, US refining profit margins had
swelled to over $16 per barrel—nearly triple the next-highest rate of almost $6 a barrel
in Europe. These profit margins were partly the gift of fracking, which delivered
copious amounts of cheap oil to refine. In a double stroke of good luck, fracking also
cut the cost of natural gas, which refiners used to power their plants. US refinery
profits pulled far and above those found elsewhere in the world.
If Koch Industries reaped the average level of profit on refining oil at Corpus
Christi that year (and the company claims to be above average in this regard), and
operated the refinery for 350 days of the year at 280,000 barrels per day (both
conservative estimates), then the company would have earned $1.2 billion in profits
from that refinery alone.
The profit margins fell sharply after 2011, sinking to around $13 per barrel in
2012 and then $12 in 2014. But the profit margins never fell close to zero, and were
always well above margins for refineries around the world.
Koch enhanced the profitability of its Corpus Christi refinery complex
III by using its
trading desks in Houston. From their vantage point, Koch’s traders could see the
reality of the US fossil fuel system, which was a fragmented network held together by
aging infrastructure. There was no national, let alone global, price for oil and
gasoline. There was only the constellation of opaque nodes where real oil and gasoline
were bought and sold, and the tanker farms, gasoline terminals, and import piers
where barges were loaded and unloaded. It wasn’t easy to get fossil fuels from one
region of the country to another. Markets in California were hemmed in by the
state’s clean-fuels standards, locking in high prices there. Markets on the East Coast
were dependent on a single, aging pipeline called the Colonial Pipeline, which carried
gasoline from the Gulf Coast all the way to New Jersey. (Koch Industries was the
majority owner of the Colonial.) This fractured market provided abundant
opportunities for trading, and Koch excelled in executing on them.
Corpus Christi became the hub for a number of trades that were, in the eyes of
traders, simply elegant and beautiful. Koch bought the cheap oil that was piling up in
terminals around the Eagle Ford Shale, the superlight crude that only a limited
number of refineries could process. Then the traders sold refined gasoline products
into markets of thriving metropolitan areas where gasoline supplies were tight, such
as San Antonio and Austin, Texas. Both of those cities were growing, thanks in part
to the fracking boom in Texas, and the growth locked in strong demand for gasoline.
Neither city had a robust public transportation system and both of them were
defined by sprawling networks of highways that conveyed motorists from far-flung
suburbs to work every day.
In this environment, the Corpus Christi refinery became a second Pine Bend, an
asset that was located right in the center of a massive market dysfunction that
produced supranormal profits. In the understated words of Koch’s former oil trader
Wes Osbourn: “They have an asset that’s advantaged on alot of their competitors.”
Koch traded around Corpus Christi in other ways, maximizing the advantage that
it had earned by being the first to build pipelines deep into the Eagle Ford. The wave
of ultralight oil was too much even for Koch to handle. It exported what it could.
Then it spent hundreds of millions of dollars to upgrade the Corpus Christi refinery
with machines that processed even higher amounts of sweet crude, raising its capacity
to roughly 305,000 barrels a day. In July of 2014, Koch Industries paid $2.1 billion to
buy a newly built chemical plant in Houston that processed light crude oil into a
chemical called propylene, used to make industrial chemicals and plastic products
such as films, packages and caps. The propylene plant was another reservoir to
capture the influx of light crude and provide another market in which Koch
Industries could grow.
The trades that could be built around Corpus Christi and Eagle Ford Shale
seemed impervious to loss, and they returned enormous profits even as oil prices fell
and the economy moved sideways from 2011 through 2015.
There was, however, one growing threat to Koch’s oil refining operations. Oil
industry analysts started to worry about something that seemed incomprehensible in
2008 when oil was scarce. The fracking boom raised the prospect that the era of “peak
oil” might be replaced by an era of “peak demand.” Even though it was cheap,
demand might fall. Consumers, for the first time in memory, had an alternative
choice in energy markets: fuels like wind power and solar energy.
The Obama administration failed to pass a carbon regulation bill. But it had been far
more successful in stoking the rise of alternative energy sources. The primary vehicle
for this effort was the stimulus bill, which provided an unprecedented $90 billion in
subsidies for renewable-energy sources. The bill also incentivized an additional $100
billion in private-sector funding. Just as the government nurtured fracking
technology for many years, its renewable-energy subsidies helped make wind and
solar power more affordable. And the subsidies were once again transforming the
energy industry.
In 2007, renewable-energy sources provided only 6.5 percent of all the BTUs
consumed in America, while fossil fuels provided 85 percent. By 2013, renewables
provided 9.5 percent of the total energy, while fossil fuels provided 81.8 percent.
(The biggest loser in the energy sector shift was coal, which was displaced by natural
gas as a fuel for power plants.) This might seem like a small shift, but in commodities
markets, even small changes can have broad ripple effects.
The Obama administration further compounded this effect by pushing for new
fuel efficiency standards for vehicles, pressuring automakers to make a fleet that
consumed less gasoline even as electric-powered cars became more affordable.
Even as Koch refined the Eagle Ford crude oil, signs of peak demand for gasoline
were emerging across America. The energy industry consulting firm Turner, Mason
& Co., which counted Koch Industries as a client, estimated that the rise of
renewables would cause demand for finished petroleum products in the United
States to fall by 0.1 percent on an average annual basis between 2016 and 2025. This
low-growth environment posed a threat to Koch’s Eagle Ford play. If demand for
gasoline weakened, prices would fall and profit margins would shrink, perhaps
permanently.
Koch Industries employees saw this threat plainly. It was evident in Koch’s own
backyard. Giant windmill farms were erected across the flat and windy state of
Kansas, their development spurred along by state lawmakers. In Kansas, the political
support for wind energy was bipartisan. Even the Republican governor, Sam
Brownback, was enthusiastic about helping the wind industry expand in the state.
Building wind farms and a new utility grid created jobs. The wind industry was a rare
beacon of future growth in the state. Fracking hadn’t taken hold in Kansas, cattle
feedlots were struggling, and farming could only support so many families.
Like twenty-nine states across the country, Kansas legislators passed a law
requiring state utility companies to buy 10 percent of their power from renewable
sources in 2011, increasing that level to 20 percent by 2020. As a result, wind farms
were becoming more plentiful, and the cost of building them was steadily falling as
the young wind industry improved its techniques. Renewable energy was on track to
steadily displace fossil fuels in Charles Koch’s home state and elsewhere.
Charles Koch knew that such developments were not inevitable. If government
policy was responsible for supporting renewable energy, then government policy
could be changed.
One of Charles Koch’s primary skills was identifying undervalued commodities. By
2013, it became evident that political power in the state of Kansas was an
undervalued commodity.
The state was deeply Republican and still largely rural. This meant that most
Kansas state officials—the occupants of the state house and the state senate—were
elected during primary contests in their home districts. A state politician in Kansas
might be elected by no more than a thousand voters during a primary race. Such
elections drew a turnout level near zero and generated almost no media attention. It
was common for a campaign to cost $10,000, on the upside.
Many Kansas state lawmakers were like Tom Moxley, a rancher from the tiny
town of Council Grove, about a hundred miles northeast of Wichita. Moxley was in
his midsixties when he ran for a seat in the statehouse in Kansas’s Sixty-Eighth
District. He figured it was his time to do some public service after decades of running
asmall business.
Serving in the Kansas statehouse was a little more serious than joining the local
volunteer fire department, but not by much. The 125 members of the Kansas House
convened every January for a legislative session that usually ended in May. When they
were in session, they met in the state capitol building in Topeka, a sleepy city about
an hour west of Kansas City.
Moxley joined the legislature in 2007. Over the next few years, he learned how
things worked. Then, starting around 2011, he watched Koch Industries transform
everything. A central focus of Koch’s efforts was beating back the mandates to
support renewable energy. Because Moxley sat on the House Energy and
Environment Committee, he had the chance to see Koch’s strategy play out
firsthand. In 2013, a string of experts descended on the capitol in Topeka to testify
about renewable energy. Moxley called these scholars “heavy hitters”—the kind of
high-profile people who rarely showed up for a statehouse hearing. The scholars came
from think tanks like the Cato Institute in Washington, and they testified about the
deeply damaging economic effects of wind power and government mandates.
Renewable-energy mandates were passed in Kansas in 2009 as a bipartisan
compromise. The state was about to approve construction of a new coal-fired plant,
and the mandates to buy renewable energy were included in the approval. The
concerns were economic as much as environmental—Kansas generated the vast
majority of its power from coal and was being hurt by high coal prices, even as
neighboring states were getting cheaper energy from natural gas. Wind power was
getting cheaper by the year, thanks to state mandates across the country and stimulus
money from Washington. Kansas wanted an alternative to coal.
In 2013, a Kansas statehouse member from Wichita pushed a bill to remove the
renewable-energy mandates. He was Republican Dennis Hedke, the chairman of
Moxley’s Energy Committee. Hedke was a geophysicist who did consulting work for
regional oil and gas companies, and his fixation on repealing the renewable-energy
mandates seemed odd to Moxley, who supported the new coal plant in 2009 but also
saw the benefits of wind and solar power. “Wind power has turned out to be less
expensive than about any other source for Kansas,” Moxley said. “I think the
renewable [energy mandates]—that part has been generally good for everybody.”
The Kansas statehouse held a number of hearings on global warming. The heavy
hitters lined up to testify. Moxley broke these experts into two groups: the “true
believers,” who thought man-made climate change was an impending environmental
crisis, and the “naysayers,” who said that the science was in doubt and the problem of
climate change was being promoted by hysterical liberals. The true believers were
brought in by the wind industry lobbyists, who were just starting to get a foothold in
Topeka. The naysayers were brought in by Koch-funded groups, including
Americans for Prosperity, the Heartland Institute, the Beacon Hill Institute, the
Kansas Policy Institute, and the Kansas Chamber of Commerce.
The hearings transfixed Moxley because he didn’t know if he was a naysayer or a
true believer. He was a staunch Republican, and therefore inclined to distrust Al
Gore and the EPA. But just like Bob Inglis, Moxley got a scientific schooling in
carbon emissions, and it changed his thinking. He gradually came to believe that the
naysayers did not have a serious case. “I’m open to good science, but those guys were
just throwing dust in the air and not making a case,” Moxley recalled. He turned
against them completely when it was proved that one of the climate skeptics had
shown legislators a chart on the Earth’s climate that conveniently omitted the last
hundred years, when temperatures began to escalate.
While the arguments over global warming were unconvincing to Moxley, Koch
Industries was using other tools to help legislators come around to its point of view.
Moxley started to hear stories from his colleagues about a changing political
landscape.
During primary elections in rural districts, Koch Industries and its various
political arms were dropping $50,000 into local primary races. This was a pittance by
national political standards, but it amounted to a shock-and-awe campaign in towns
like Larned, Kanapolis, and Great Bend. Koch Industries was expert at coordinating
with other conservative groups, Moxley said, such as the National Rifle Association,
the pro-life group Kansans for Life, the state Chamber of Commerce, and, of course,
Americans for Prosperity.
Moxley observed a recurrent strategy. He said that Koch handpicked a candidate
in a primary election, told that candidate to stay home, and then scorched the earth
beneath their opponent with negative messages in the form of postcard mailings,
advertisements, and door-knocking campaigns. Such efforts intensified in 2012 and
wiped out incumbents who seemed resistant to Charles Koch’s political vision.
“The bottom line is, they flipped the [Kansas] senate from pretty traditional
Republican kind of thinking to ‘Koch’ kind of thinking. And it’s pretty dramatic.
We’re still living with it,” Moxley said. He grew disdainful of a new breed of state
legislators who showed up in Topeka and seemed more concerned with toeing a line
set out by Koch Industries than they did with thinking for themselves.
“They’re like numbskulls. All they’re going to do is take orders from the Chamber
and Koch and so on,” Moxley said. “They’re not thoughtful. They’re not people that
read the newspaper or have a history background. They just do what Koch wants
done.”
Koch’s efforts in Kansas were part of a multistate campaign to push back
renewable-energy subsidies. Koch’s primary targets were so-called renewable energy
standards that required states to buy wind and solar power. Koch characterized these
mandates as a form of crony capitalism. The Heartland Institute, which Koch
funded, helped write a bill to repeal such standards. The bill was then taken up by
ALEC, the Koch-funded conference of state legislators, and then introduced in more
than a dozen states between 2013 and 2014.
ALEC’s efforts bore fruit. Ohio repealed its renewable standard, as did West
Virginia. In Kansas, the fight lasted for years. Moxley repeatedly voted against the bill
to repeal the renewable-energy mandates, as did a handful of other Republicans and
many Democrats. But the financial power behind the bill was too strong to resist. In
2015, a version of the bill finally passed, removing the mandates and making the
renewable-energy standards voluntary. This was only a partial victory for Koch. Wind
power continued to gain ground in Kansas in part because it was so cheap. The utility
companies were already meeting their renewable standards whether they were
mandatory or not. Still, Koch had managed to achieve an effect in Kansas and other
states that was similar to what it had done in Washington. It politicized the issue of
renewable energy. It had stained the efforts to stoke competition in the energy
industry as a form of government corruption, and it drew a red line that Republican
politicians could not cross.
Moxley ended up leaving the Kansas legislature in 2016, when he decided not to
seek reelection. “I kind of aged out,” he said. But his time in the conservative Kansas
statehouse changed his thinking about human-induced climate change. He was more
worried about it than before. He went back to his ranch in Council Grove, installed a
large set of solar panels, and now only pays for electricity off the grid for about five
months in the winter. About a year after he left politics, Moxley began to recover
from the experience.
“I was just walking across the yard, and broke out in a whistle,” he said.
By 2014, a sense of mastery infused the corporate culture at Koch Industries. The
company was thriving, even during an era of almost unprecedented volatility in the
global energy business and weak economic growth in the United States. A geyser of
cash flowed from Koch’s oil refineries, thanks to the Eagle Ford Shale play and the
continued profitability at Pine Bend. Profits were soaring in Koch’s massive network
of nitrogen fertilizer plants, thanks to the collapse of natural gas prices. Business was
strong and profits were rising at Georgia-Pacific, thanks to a recovery in the housing
market. The company’s success seemed like the proof of concept for Market-Based
Management. Koch Industries seemed to have its hand in everything—paper towels,
gasoline, clothing, corn, derivatives trading—and somehow it succeeded even as
different markets rose and fell.
Charles Koch and his team had also proven that they could master the art of
politics. The Obama revolution was crippled. The days of a permanent liberal
majority and a new New Deal were in the past. It was true that Obama had been
reelected in 2012, but his governing power was hemmed in by a Congress that slid
further into Republican control with each election. Koch’s chosen congressional
candidates gained more seats in the midterms of 2014. Across the states, Koch’s
political network was more powerful than ever. The greatest legislative threat to
Koch’s business—greenhouse gas regulation—was relegated to the fringes of
American political life. Charles Koch had faced a political movement that he
considered to be dangerous to America’s future, and he had largely prevailed.
As always, Charles Koch had his eye on the far future. The vast majority of profits
that flowed from Koch’s operations were recycled right back into the company. Koch
Industries initiated an acquisition spree that was only paralleled by the wild growth
strategies of the 1990s. During 2013 and 2014, Koch Industries spent billions of
dollars to amass new assets and enter new lines of business. It acquired companies in
an impossibly diverse array of industries: from steel, to glass, to greeting cards.
In late 2012, Koch bought a stake in the privately held glassmaker Guardian
Industries, making Koch the largest shareholder. Koch placed an executive on
Guardian’s board and monitored the company’s performance, eventually purchasing
the rest of Guardian’s shares. In 2013, Koch paid $7.2 billion to buy the technology
company Molex, which made electronic sensors and chips. This acquisition gave
Koch its first major presence in the technology sector and it also played to Koch’s
strength as a commodity company; Molex made its products by using huge quantities
of rare earth materials and metals.
Also in 2013, Koch invested $1 billion to help build a high-tech steel mill in
Arkansas, anticipating that the specialty steel it produced would be in high demand as
America’s economy improved and replaced its aging electricity grid. Somewhat
strangely, in April of 2013, Koch financed a deal to buy the greeting card company
American Greetings and take it private in a deal worth $878 million. Outsiders
wondered if that wasn’t some sort of add-on to Koch’s paper business, but it seems
that Charles Koch just thought the card company was a good buy. In August, Koch
paid $1.45 billion to purchase Buckeye Technologies, a company that made specialty
fabrics and materials out of wood and cotton, which was then tucked into the
Georgia-Pacific division.
The sense of mastery within Koch Industries only intensified in 2014 when
Charles Koch and his team expanded and renovated company headquarters. The
corporate campus had not grown significantly since the Tower was built in the
1990s, and now Koch needed more room to accommodate its growing workforce.
The only hindrance to this expansion was Thirty-Seventh Street, the busy two-lane
road that ran through the north side of the headquarters campus. Many employees
had to park on the north side of Thirty-Seventh Street and use an underground
pedestrian tunnel to get safely into the Tower. To alleviate this problem, Koch
Industries paid to have Thirty-Seventh Street torn out and rerouted in a large
semicircle that arced around the headquarters. The newly laid Thirty-Seventh Street
created a giant horseshoe shape. Inside the horseshoe, Koch built a new office
building with 210,000 square feet of space and enough room for 745 employees.
The most noticeable renovation, however, was the wall.
Koch Industries erected an earthen wall that encircled the north end of the
complex, running in a curve along the newly rerouted Thirty-Seventh Street. The
wall was tall and sloped, with trees planted along its length. Before the wall was
erected, visitors could turn from Thirty-Seventh and steer directly into Koch’s
visitors’ lot. Uninvited guests could walk directly from the lot into the Tower’s lobby.
Now the only means of entrance were a series of checkpoints. Two of the
checkpoints were located on the north side, where metal gates had been installed into
the side of the wall. To gain access, a visitor had to first receive an e-mail from the
address DoNotReply-SAFE@kochind.com that included a bar code in the message.
A security guard inside a squat building next to the gate scanned the bar code with a
red light. If accepted, a yellow guardrail rose up and allowed the visitor to pass inside.
The wall around Koch Industries reflected the cost that came with Charles Koch’s
political victories. For decades, Charles Koch had fiercely guarded his privacy. In just
a few short years, he had become a public figure and a walking political cartoon. The
“Koch brothers,” meaning Charles and David, had become fodder for countless
political ads and exposés. Their image became a shorthand illustration for the
influence of big money on politics. Charles Koch began receiving death threats in
steady volume. The earthen wall helped keep such threats at bay. Now packages
delivered to Koch Industries were received first in a bomb-proof room at the Tower
where packages ran through X-ray machines to scan for bombs. When Charles
parked in a special lot with indoor access to the building, Koch Industries became
more fortresslike and more culturally insular, even as it extended its reach further
each day into industries that underpinned modern life.
Charles Koch could spend his long working days surrounded entirely by people
who were beholden to him for a paycheck. His office was the epicenter of a corporate
empire over which he had almost unchallenged control. But for all this power, there
was one thing that Charles Koch could not control, and that was the passage of time.
He turned eighty years old in 2015. But it didn’t seem that anyone expected him to
retire.
“They’ll take Charles out of there on a stretcher. And I think he’ll be the happiest
that way,” quipped Leslie Rudd, one of Charles Koch’s longtime friends in Wichita.
But even if he never retired, Charles Koch could not lead the company forever.
And this raised a troubling question: Could Koch Industries thrive without him?
The politically correct answer among Koch employees was that Market-Based
Management would be able to carry on without the charismatic CEO who created it.
Charles Koch’s wisdom had been codified into a machine, this thinking went, and the
machine could thrive without his personal intervention. But history was replete with
examples of companies that had stagnated once their founders left. Koch Industries
seemed like a prime candidate for this fate. Charles Koch insisted on maintaining
control over the company since he became CEO in 1967. No one knew how the
corporation would operate without him.
Charles Koch had a contingency plan. He had placed a hedge bet against mortality
and the passage of time. There was a possibility that Koch Industries might be passed
down to an heir, a young man who could carry on the Koch name and the tradition
of family ownership.
Charles Koch was raised in a household with four sons, four potential heirs to the
family business. Charles, on the other hand, had only one son. He had vested many
hopes, and many years of work, in him and by 2015, Charles Koch’s son was seen as
the heir apparent.
His name was Chase Koch, and everyone who met him thought that he might be
CEO of Koch Industries one day. But what people didn’t know was if he’d be ready
to do it. Or, more importantly, whether he wanted to.
I. Even the most optimistic of these forecasts profoundly underestimated how much oil would come gushing
from the ground.
II. There were an additional thirteen refineries that produced lubricating oils and asphalt in 2012.
III. Koch’s complex in Corpus Christi includes two refineries. For the sake of simplicity, the complex is referred to
here as simply Corpus Christi, or the Corpus Christi refinery.
CHAPTER 22
The Education of Chase Koch
(1977–2016)
When he was a young boy, Chase Koch might have seemed unteachable. But that
didn’t mean that his father didn’t try. On Sunday afternoons, Chase Koch and his
older sister, Elizabeth, got personal lessons from their father.
It was common for families in Wichita to attend church on Sunday, sending the
kids to Sunday school while their parents listened to sermons from the altar. This was
not the tradition in Charles Koch’s household. Charles Koch developed his own
curriculum to teach his children, a curriculum that taught them about his systematic
view of human behavior and how best to organize human society. On Sundays,
Charles Koch gathered Elizabeth and Chase in the family library.
The library was alarge, imposing chamber in the back of the house, with walls that
were lined by thousands of books. The books on philosophy, history, and science
were the raw material of Charles Koch’s worldview, which he had encoded in
Market-Based Management. When they sat down for their lessons in the library,
Elizabeth and Chase Koch were likely the only people on earth to get such deep, oneon-one lessons in MBM from the creator himself.
Charles Koch played taped lectures from economists like Walter E. Williams and
Milton Friedman. As the economists and philosophers droned on, Charles Koch
periodically stopped the tape and quizzed his children.
“He’d pause it and then say, ‘Okay, well, what did you kids learn from that?’”
Chase recalled. Chase was maybe eight years old at the time; certainly “in the single
digits,” as he remembered it.
Elizabeth, the oldest child who always seemed eager to please, was attentive to the
lessons and earnestly answered her father. Chase struggled to stay awake. “Literally
half the time, I’d get caught, like, with a baseball hat over my eyes, because I would be
sleeping through it,” he said. “And my sister, being the good first child . . . she was
valedictorian in her class or second in her class. And so she was, at a very early age, just
gobbling this stuff up.”
Charles Koch tried to teach his son, but it appeared that his son did not want to
learn. Chase’s obstinance, or apathy, posed an obstacle to Charles Koch and his
future plans.
Those plans seemed clear to everyone from the first day Chase Koch was born, in
June of 1977. At that time, a group of employees at Koch Industries took it upon
themselves to print a banner and hang it up above their desks, where Charles Koch
would see it when he returned to the office.
The banner read: “WELCOME CROWN PRINCE.”
If the birth of Charles Koch’s daughter had not been greeted the same way, it
might have had something to do with the conservative culture of Wichita at the time.
“In those days, it was logical that your son followed you,” said Leslie Rudd. “A lot of
people around the area—the kids followed their fathers.” This was the Koch family
tradition. Charles Koch had followed his father, Fred, who had pushed him,
disciplined him, taught him to fight, and then pressured him to return to the family
company and run it. It seemed natural that Chase would, in turn, follow Charles.
“Charles was preparing Chase for success. But it’s damn near impossible to do, to
build the drive and all of those things into a person,” said Rudd, who went on
vacation with Charles Koch and attended many Koch family events.
Charles and his wife, Liz, worked hard to instill a competitive drive in their
children. They informed Chase and Elizabeth that the children must find a sport
outside of school at which they could excel. When Chase was about ten, his parents
enrolled him in alocal basketball league, which was sponsored by the Salvation Army.
One of the league coaches was Brad Hall, who later became CFO of Koch Supply &
Trading. Hall often watched Chase Koch play and saw a gangly, mediocre player. But
Hall was impressed with the kid’s values. Chase worked hard. He wasn’t arrogant. He
didn’t advertise his last name to anyone. Hall remembered seeing Charles Koch at the
games, watching closely.
When it was clear that Chase had no future in basketball, the family focused on a
different sport: tennis. Chase showed aptitude here. If Charles Koch was born with a
brain for math, Chase Koch was born with a body for tennis. Chase was tall and lean,
with powerful legs. He could get to the far corners of the court before his opponent.
He had a strong swing. Unfortunately, playing tennis required that Chase Koch
spend large amounts of his free time—weekends, nights, and summers—at the
Wichita Country Club.
Just like his father, Fred, Charles Koch vowed that he would never raise any
“country club bums.” But Chase Koch seemed to want very much to be a country
club bum. It turned out that he was quite sociable and liked having friends.
Eventually, Chase’s natural talent for tennis won the day. He was allowed to spend
long hours each day, and whole days in the summer, with his friends, as long as he was
on the tennis court.
Things weren’t as easy for Elizabeth. She never found her equivalent of the tennis
court. Outside the confines of sports, social interactions were fraught and
complicated for the Koch children. Elizabeth Koch wrote later about the difficulties
of growing up as the daughter of the richest man in town. She could go wherever she
wanted, but could never escape the family name. “I want people to like me, and as a
small child growing up in a small town, I learned that having money makes people
sort of hate you on the spot,” Elizabeth Koch wrote.
Every year, a portrait of the Koch family was printed and sent out as a Christmas
card to Koch Industries’ employees. The family posed in that awkward manner all
professional photographers seem determined to create: Elizabeth Koch sitting on the
floor, with her father kneeling behind her, his arm around her shoulder. Chase and
his mother hovering behind them, with frozen smiles. Elizabeth never seems to have
escaped the feeling of awkwardly posing as Charles Koch’s daughter. As a young
adult, she was filled with anger, and it strained her relationship with her parents.
“I am such a terror,” Elizabeth Koch wrote in an online essay in 2007. “I’m angry
that those girls on the playground in sixth grade called me a rich bitch when they
knew nothing about me except my last name. I’m angry that I have everything in the
world I could possibly wantand yet I’m still angry.”
Spending time on the tennis courts removed some of these pressures from Chase
Koch’s life. Things were uncomplicated and straightforward on a tennis court. There
was often very little talking. Everyone focused on the ball. Chase Koch was on a
tennis court in the mornings, afternoons, and weekends. He practiced hard and drove
himself. Soon, Chase was playing in regional tournaments and winning. He became
recognized as one of the best young players in Wichita, and then was recognized as
one of the best players in Kansas. He became one of the top players in the Missouri
Valley Conference, which covered several states. On the tennis court, Chase Koch’s
last name didn’t matter. And if Chase Koch was winning, his father didn’t express
dissatisfaction.
By the time he was in middle school, Chase Koch’s tennis regimen became difficult to
sustain. All of his free time became dominated by tennis. When he spent time with
his mother, it was so they could drive to regional tennis tournaments. Chase began to
burn out. He started to hate the game. And he rebelled.
“I got exposed to new groups of friends and got to hang out with them, and just
enjoyed that part of life instead of tennis,” Chase recalled. “In some of these regional
matches, I intentionally started throwing matches, and, like, tanking, because I
wanted to get home and party with my friends, basically.”
Chase’s mother, Elizabeth, couldn’t understand what was happening. He was
losing now in the early rounds, when he used to win easily. It vexed her, and brought
her to tears.
“So she reported this back to my father,” Chase said.
After hearing about Chase Koch’s failure on the court, Charles Koch invited his
son to come down to Koch Industries headquarters for a talk. Chase expected that
they might have lunch. When he arrived, there was no lunch.
Charles Koch gave his son a choice. Summer was about to begin, and Chase could
do one of two things. He could spend his summer working for Koch Industries, or he
could reapply himself to tennis and play competitively again.
Chase would be fifteen years old that summer. It was his last summer before high
school. He chose to work for the family company. He thought that he would get an
office job, learn some things, and have the evenings to spend time with his friends.
Plus, he’d earn some money. The decision was easy.
“I said, ‘Fine, you get me a job. I’m so sick of this. I’m tired. I’m burned out. I
want to do something else,’” Chase said.
The next day, Chase Koch woke up to discover that his father had packed his bags
for him. Chase would be leaving for the summer. A driver arrived to give Chase a
ride. They would travel four and a half hours due east of Wichita, to a tiny town
called Syracuse.
Within thirty minutes of leaving Wichita, the land flattened out and grew
desolate. There was very little to interrupt the landscape of open grassland except for
the occasional oil derrick. Two hours outside of Wichita, a person can feel totally
marooned in the center of a prairie. Two hours after that, Chase Koch arrived at his
destination.
Syracuse was home to one of Koch Beef Company’s largest cattle feedlots, a
centerpiece of the doomed company’s effort during the 1990s to reinvent the
agribusiness sector. Chase could smell the place from miles away. Roughly fifty
thousand cattle milled around in muddy pens beneath a grain silo, which was one of
the tallest structures in the Syracuse skyline. Chase Koch was dropped off and shown
to his quarters. He would live in the single-wide trailer of a guy named Kelly Fink, the
feedlot’s manager. Fink told Chase that he’d be sleeping on the couch for the
summer. Chase set down his things, and tried to settle in. Fink slept down the
hallway, in the trailer’s single bed.
Chase suspected that his father had given Kelly Fink specific orders to break
Chase’s spirit. Chase was assigned to shovel shitand pick weeds. “The first two weeks,
I was just bitter, because they handed me a shovel and said, ‘Go shovel out that stall
and then go pick all these weeds.’ And it was just a lot of busywork just to get my
head right.”
Chase worked at least ten hours a day, seven days a week. He got one day off, the
Fourth of July. On that day, his parents called him from Vail, Colorado, where they
were vacationing. They told him that it was snowing there. Wasn’t that remarkable?
Chase kept working and slowly got to know Fink. Then he started to like him.
Then, strangely, he started to like the work. Toward the end of the summer, Chase
felt something he’d never really felt before. He felt like he had endured an ordeal, and
had really earned something.
When Chase was in sixth grade, his father had helped him write a paper. Chase’s
assignment was to pick a philosopher and write about the philosopher’s ideas.
Charles Koch told his son to pick Aristotle, and they read Aristotle’s work together.
Charles Koch wrote notes on Aristotle in his neat, engineer’s script, listing page
numbers from Aristotle’s significant work for Chase to pursue. When Chase turned
in the paper, he summarized what he believed was one of Aristotle’s most important
ideas.
“Aristotle taught that the goal in life is to be happy and to be happy you need to
use your natural ability,” Chase Koch had written.
Now, at the end of the summer, before his freshman year of high school, Chase
was starting to understand what Aristotle had meant. And what his father had meant.
Chase Koch was feeling happy. He was feeling asense of accomplishment.
Chase enrolled for his freshman year of high school at the Wichita Collegiate School,
a private academy located on a spacious, grassy campus less than two blocks from the
Koch family compound. To get to school each morning, Chase could leave the front
gate of the Koch estate and take a left turn on Thirteenth Street, heading due east,
passing the front gates of the Wichita Country Club, and then taking a right turn
into the parking lot of his high school. This is the small geographic circuit in which he
spent the majority of his adolescence.
The Wichita Collegiate classrooms were located in a group of modest, beige-brick
buildings, set back from the street behind a screen of leafy trees. On the east side of
campus there was the football field and the track, and then, farther back, a cluster of
tennis courts. This is where Chase Koch spent an inordinate amount of his free time
as ateenager. The tennis courts were the domain of a tall, imposing man named Dave
Hawley, one of the winningest tennis coaches in Kansas history.
I On a typical spring
afternoon, Hawley walked from court to court in the tennis complex, calling out to
his players in a booming voice. Hawley was uncompromising in his discipline and
demands. If he felt that students weren’t practicing hard enough, he sent them home.
If he felt they were falling short of their own ability, he let them know in unvarnished
critiques. Still, Hawley could be friendly and gregarious. He gave lessons to little kids
when things were quiet. While coaching a small girl, Hawley reminded her that tennis
wasn’t like bowling; you couldn’t take your time to set up a shot. The game was an
intimate competition against an opponent who didn’t want to give you time to think,
and who wanted to be unpredictable. As he lobbed balls toward the little girl, Hawley
called out to her, “You never know what’s coming! You never know what’s coming!”
Chase Koch thrived in this world. Over the course of his high school career, Chase
faced more than a hundred competitors, and beat all of them except for one. The one
student who beat Chase was Matthew Wright, a classmate and fellow player on
Hawley’s team.
Chase Koch was one of the best players that Hawley ever worked with during his
decades-long career. “If I had a Mount Rushmore of players that I’ve coached, he’d
be on it,” he said of Chase. “He’d be one of the four—at the very outside, one of the
six—best players I’ve ever coached on the boys’ side.”
Chase Koch’s style of play reflected his personality. His game relied on two
primary strengths: his ability to quiet his mind and react in real time to his
opponents, and his willingness to work harder than nearly everyone else in the state.
Hawley noticed Chase Koch’s quiet demeanor almost immediately. The tennis team
spent a lot of time together, and Hawley had hours to observe Chase interact with his
classmates. What Hawley saw was a kid who defied expectations. Everyone in Wichita
knew who Chase was the moment he walked into a room. The aura of power and
wealth around the Koch name was inescapable. Yet somehow Chase Koch made this
aura invisible. He didn’t act superior. He didn’t act like he was better than anyone
else. He did drop stories about private jets and the fact that he could attend the US
Open in New York every year with his family. Chase seemed happiest on the court,
where he competed in silent exertion. “If you had no idea who he was, you never
would have known who he was,” Hawley said.
Chase approached tennis as if it were a seven-day-a-week job. Hawley never saw
Chase take it easy during practice. Chase developed a game that Coach Hawley called
an “all-court game.” Chase’s primary skill was the ability to be anywhere on the court
before his opponent could get a ball there. Chase’s strategy relied in part on wearing
his opponents down, volley after volley, until they made too many mistakes and
crumbled. It was a strategy that relied on hard work, long practice, and physical
conditioning. There wasn’t some secret genius in Chase Koch’s serve. He just
outworked the competition.
Still, Chase Koch could never beat Matt Wright. If Chase was impressive, Wright
was slightly more so. Their close proximity in talent drove a friendly competition
between the teammates. During those intense hours of practice, it was often Chase
Koch and Matt Wright who fought the hardestagainst each other.
Chase won more freedom as he excelled in school and tennis. He got a Ford
Explorer and, during his sophomore year, he got his driver’s license.
On the evening of Saturday, September 18, 1993, Chase took the car out for the
evening. He planned to take a group of his friends to a shopping mall. Chase was in
the driver’s seat, and, like so many teenage boys, he must have luxuriated in the
freedom it gave him. He accelerated, and felt the speed and power of the Explorer.
Chase Koch was in charge, and he was going fast.
That evening, a woman named Nola Foulston was out for a walk. She happened to be
the prosecuting attorney for Sedgwick County, which encompassed Wichita. As she
strolled along, Foulston saw a Ford Explorer driving through the neighborhood. She
would later say that the Explorer was going so fast that she took notice of the car and
remembered what it looked like. The car was barreling through residential streets. It is
unclear if she saw the teenaged boy who was driving.
At that moment, a twelve-year-old boy named Zachary Seibert was out for a jog.
Zac, as he was known to his parents and two siblings, ran a three-mile loop from his
home, about three times a week. His father, Walter, had helped him trace out the
route. Walt himself had been an accomplished runner; he met Zac’s mother while he
was training in Boulder, Colorado, to run in the Olympics. Zac was the couple’s
oldest child and, in September of 1993, Zac was almost thirteen years old and
becoming an enthusiastic runner. He often woke up before five in the morning to get
in arun before school started.
Walt taught his son to be mindful of cars. That evening, while Zac was running
south through the neighborhoods near his family’s home, he stopped at the
intersection on East Douglas Avenue, a four-lane road that was a major thoroughfare
for crosstown traffic. He stopped at a pedestrian crosswalk beneath a traffic light, and
pressed the button to activate the crossing signal. Zac had his headphones on and was
listening to Kris Kross, an upbeat hip-hop group with a driving beat.
The traffic light on Douglas turned yellow, and then red. A big van slowed down
and stopped in the lane closest to Zac. The van would have obscured Zac’s view when
he looked left to scan for traffic heading west on Douglas Avenue. Walt had coached
Zac on looking both ways when he entered a crosswalk, so presumably Zac did so.
Then he jumped into action, running out into the street.
Chase Koch was driving the Explorer on Douglas with at least one friend in the
car. They were going to a shopping mall called Towne East Square, presumably to
waste away the hours of a Saturday night in the tradition of teenagers everywhere,
hitting the food court, meeting up with other friends, browsing the windows.
Chase was going fast. He was about a block away from the mall, and driving in the
left lane. As he approached the crosswalk, the traffic light was red and the big van was
stopped in the right-hand lane.
Just as Chase passed the van, Zac lurched out in front of his car. There must have
been less than a second for Chase to respond. The front right corner of Chase’s car
struck Zac, and Chase kept driving. He went about two hundred yards until he came
to a parking lot, where he turned his car around. He called 911 to report the accident
from his car phone.
Zachary Seibert was still alive when the ambulance arrived and transported him to
HCA Wesley Medical Center. Someone called his father, Walt, who rushed to the
hospital to be at his son’s side. When he arrived, Walt was told that Zac was still alive.
Details were sparse, but it appears that everyone involved already knew that the driver
of the car was the son of the richest man in town. This created an awkward, painful
dynamic. Walt Seibert didn’t think much about it because he was desperate for news
about his son, but he couldn’t ignore the dynamic for long.
“At the hospital, there was a cop . . . from the Wichita Police Department that
actually told me not to ‘seek a pound of gold.’ At that moment, when I don’t know if
my son is living or not,” Seibert recalled. He assumed the police officer was referring
to the notion that the Seiberts might sue the Koch family in order to profit from the
tragedy. Seibert said such an action was inconceivable to him.
Zac died roughly an hour after arriving at the hospital.
Charles Koch was more than a prominent citizen of Wichita—his company was one
of the city’s economic engines. On Tuesday, September 21, 1993, subscribers of the
Wichita Eagle learned that Charles Koch’s son, Chase, was driving the car involved
in a horrific tragedy.
Charles and Liz Koch took swift action to protect their son. But they also took
action, just as swiftly, to expose Chase Koch to the dire consequences of his mistake.
They did so in a way that was severe and that ensured Chase could never deny the
reality of what he had done.
To protect Chase, the Kochs employed Don Cordes, the bulldog attorney who
was general counsel for Koch Industries at the time. Cordes became the Koch
family’s spokesman, and he conveyed a narrative that minimized Chase Koch’s
culpability in the accident.
Cordes told the Wichita Eagle that Chase Koch thought the traffic light over the
crosswalk was yellow as he approached it, an account that Chase had provided to
authorities after the accident. Cordes said it seemed unlikely that Chase Koch was
speeding, in part because there were no skid marks at the scene of the accident. “We
are going on the theory that, when he swerved to the left, if he would have been going
at a high rate of speed, he would have spun out of control. This is just one of those
tragic things,” Cordes told the paper. “There was no drinking, no drugs. This was a
straight-arrow kid. Good grades, athlete.”
It might have been easy for Charles and Liz Koch to shield Chase behind their
company lawyer. It might have even been pragmatic. They didn’t know the Seibert
family, and didn’t know if the family might seek to extract its “pound of gold.”
But the Kochs chose a different strategy. Shortly after Zachary Seibert died,
Charles and Liz Koch told their son to visit Zac’s parents in their home; to be
accountable for what he had done. At the time, Walter Seibert was still trying to
process what happened. Elizabeth Koch accompanied Chase to the Seiberts’ home.
Walt Seibert said that he wanted to talk to Chase privately and suggested that he and
Chase could sit in the front seats of the Seibert family’s van. Chase agreed to it. When
they closed the doors, Chase and Walt were encased together in silence. Walt Seibert
could see that the sixteen-year-old next to him was distraught, and maybe terrified.
“I just wanted him to tell me his version of what happened. He was extremely,
extremely nervous. Maybe I don’t blame him, for what he went through,” Seibert
said. Chase apologized, and his deep remorse seemed utterly sincere. Seibert pressed
the boy for details about the accident.
“He basically just said he didn’t know what was happening. He thought the light
was yellow, and didn’t say anything about speeding,” Seibert recalled. This fact would
gnaw at Seibert later, because he felt like he hadn’t gotten the whole story. County
prosecutor Nola Foulston later told him that she had seen Chase’s vehicle speeding
through neighborhoods before the accident. But while Chase might have fumbled his
words with Seibert that day, he later admitted in open court to running the red light
and accepted blame for what he had done.
Charles, Liz, and Chase Koch attended Zachary Seibert’s funeral. A friend of the
Seibert family would later tell the Wichita Eagle that it was “emotionally wrenching
to watch [the Koch family] at the funeral . . . It took a lot of courage to walk in that
group of people. And every eye in that church was on them.”
Chase Koch must have felt those eyes on him. This was the kind of experience that
burns into a person’s mind. Chase Koch had been careless and reckless in a way that is
common among teenage boys. But in an instant, the carelessness reaped consequences
that could never be erased, for anyone involved.
Nola Foulston recused herself as prosecutor because she was a potential witness in the
case. A special prosecutor named Stephen Joseph was appointed to the case, and he
charged Chase Koch with misdemeanor vehicular homicide. This was a lesser charge
than involuntary manslaughter, a felony that could be applied to traffic accidents
where drivers acted with conscious knowledge that they were threatening human life,
or acted with a total lack of concern for other people’s safety. Joseph didn’t think that
the facts of the case warranted such aserious charge.
Chase Koch plead guilty to vehicular homicide in December. In January, just as he
was beginning the second half of his sophomore year in high school, Chase was
sentenced to a year and a half of probation, one hundred hours of community service
work, and a nightly curfew that would last ten months. He was also required to pay
for Zachary Seibert’s funeral expenses and to take a defensive driving course.
Walter Seibert said he was satisfied with the sentence and believed that justice had
been served. But decades later, Seibert was still bothered by his conversation with
Chase Koch in the van. He felt that Chase tried to evade responsibility. “He was with
three other teenagers in the car. So they were screwing off. They were fucking
around, driving at too high a speed,” Seibert said. “He didn’t tell me about going
through a red light. He didn’t tell me about not seeing the light. The thing is, he was
so, so obviously nervous. I can’t honestly totally blame him. But the bottom line is, he
still killed my son. And he didn’t own up to anything he did.”
Seibert was notaware of it, but Chase Koch would never be able to escape what he
had done. As he grew older and rose through the ranks of Koch Industries, Chase
Koch rarely mentioned the accident. But he lived with it every day of his life. “I wish I
could take it all back,” Chase Koch said about the accident. “I can’t forgive myself for
what I did. And I don’t expectanyone else to.”
The accident permanently removed an element of innocence from Chase Koch’s
life. There was before the accident, and there was after. In the time after, the memory
of what happened never went away. “I take full responsibility for what happened,”
Chase said. “And I think the reality is that I’m going to live with this the rest of my
life.”
During the second half of his high school career, Chase Koch once again found his
place on the tennis court. His high school career record was 110 wins and 14 losses.
All of those losses were against his teammate Matt Wright.
When Chase Koch was a senior, Coach Hawley suggested that he play doubles
with Matthew Wright at the state championship. Hawley believed that Chase richly
deserved a state title, and he could get it by playing with Wright. Chase told Hawley
he’d think about it over a weekend. When he came back on Monday, Chase said that
he didn’t want to do it. Winning a state title didn’t seem as important as being
measured on his own merits.
After Chase Koch’s senior year of high school, an emergency meeting was called
among managers at Koch Industries’ oil refinery in Corpus Christi. A manager had
just been informed that Charles Koch’s son would be coming to work there for the
summer. This set off something close to a panic. One of the employees at the meeting
that day was Brenden O’Neill, the engineer who would later earn millions trading
derivatives for Koch.
“It was kind of funny,” O’Neill recalled of the meeting about Chase’s arrival. “It
was like. ‘What are we going to do?’ ‘We’re going to take care of him and keep him
busy and give him some stuff to do.’”
O’Neill didn’t find the situation funny for long. He was informed that Chase
Koch would work directly under him. This required a painfully tense balancing act.
Managers felt that Chase had to be pushed, but also had to be treated well. The job
had to be hard, but not grueling. O’Neill was in charge of managing this
contradiction day to day. O’Neill was given one key warning from his boss: “Don’t
let him get hurt.”
When Chase arrived, he wasn’t what O’Neill had expected. He was tall, quiet, and
completely unpretentious. “He wasn’t a workaholic at eighteen, I’ll put it that way,”
O’Neill recalled. “He didn’t act like, ‘Hey, I’m going to take over the company
someday.’”
Early in the summer, Chase told a story that put O’Neill at ease. Chase said that
before he came to Corpus Christi, his father had called him into his office and then
called the plant manager on the phone while Chase was listening: “Charles calls up
the plant manager and says, ‘If Chase screws up, I want you to fire him on the spot.
And if you don’t have the balls to do it, I’ll do it myself,’” O’Neill said. “Chase told
me that. The plant manager didn’t tell me that.”
O’Neill found Chase Koch to be a surprisingly normal teenager. Chase wanted to
make friends and spent a lot of time working on his car, installing a souped-up stereo
and speaker system during his free time. O’Neill gave Chase jobs that kept him away
from the cracking units and refinery towers, where flammable chemicals flowed at
high pressure. Chase analyzed spreadsheets of data from the refinery operations and
helped O’Neill and his colleagues analyze the units’ performance. It was the
Goldilocks job—just educational enough without exposing Chase to too much
danger.
O’Neill very rarely saw Chase get agitated, let alone lose his temper. One of the
few instances this happened remained vivid in O’Neill’s mind decades later. As they
were working in the office one day, an employee from the payroll department came
in looking for “Charles Koch,” probably referring to a directory that listed Chase’s
full name: Charles Chase Koch.
Chase knew that the payroll employee was referring to him. “I could tell that he
was, like, visibly offended that he called him Charles,” O’Neill observed. Chase’s
response was swiftand terse. “My name’s not Charles. It’s Chase.”
Fred Koch went to MIT. Charles Koch followed in his footsteps and attended MIT
for both his undergraduate and multiple graduate degrees. David Koch went to MIT.
Bill Koch went to MIT.
Chase Koch went to Texas A&M. Chase majored in marketing. He didn’t play
tennis, and he lived, for the first time, outside the small circuit of the Koch family
compound, the Wichita Country Club, and the Wichita Collegiate School campus.
When he moved to College Station, Texas, Chase lived in a place where the Koch
name didn’t mean anything. For the first time in his life, he could be Chase, rather
than Chase Koch.
After graduation, Chase Koch decided not to move home. He wanted to cut his
own path and work for a company where his family name wasn’t written on the front
door. He moved to Austin, Texas, and got hired at a small consulting firm, doing
marketing work. During his off hours, Chase started playing music and joined a band
that played gigs around Austin. They played covers of Led Zeppelin, Pink Floyd, and
Widespread Panic songs, alongside some original material. It was “jam-band stuff,” as
he called it, played for an audience heavily lubricated with beer.
This was a happy life for a while, but a sense of uneasiness began to creep in. He
was living like an ordinary, workaday white-collar guy. But in his world, this life
could be considered a failure. The mythology of his father hung over him. His dad
earned multiple degrees from MIT and became CEO of Koch Industries in his early
thirties. Compared to this, it looked like Chase Koch was stagnating, even failing.
In 2003, Chase Koch traveled to New York to watch the US Open with his family.
When the game was rained out, Chase joined his father and their family friend Leslie
Rudd for lunch. When they sat down, Rudd started asking Chase how he was
enjoying Austin. How was the marketing gig? How was life? Was Chase happy?
Charles Koch sat silently and watched. Chase tried to act disinterested and dodge the
questions. Things were fine. The job was good. Austin was great.
Rudd did not relent. He pressed Chase—why didn’t Chase come back to Wichita
and work for the family business? Why was he wasting time down in Texas playing in
a band? Then Rudd put on the hard sell. Chase should give a hard look at coming
back to the family company.
“What I said to him was: ‘Chase, it’s a fabulous company. Your dad’s a great
CEO,’” Rudd said. “‘It’s fine if you want to turn it down, but you’ve got to earn the
right to turn it down. You’ve got to go—find out what it’s about, work there, and
then decide. You can’t just say no hypothetically.’”
Chase looked over at his father, who seemed to be acting studiously disinterested
in Rudd’s line of questioning. Rudd insisted later that Charles Koch didn’t put him
up to the job of convincing Chase to return. Rudd said he cared about Chase and
gave him advice that he would have given to his own son.
The conversation changed Chase Koch’s life. He quit his job in Austin, quit the
band, and came back home to Wichita. Soon after he returned, Chase Koch attended
a meeting with his father and Steve Feilmeier, Koch Industries’ chief financial officer.
Charles Koch and Feilmeier explained that Chase Koch would take a series of jobs
that were something like a training course. He would receive the equivalent of an
MBA degree during his first years at the company. But the MBA degree was
specifically tailored to Koch’s way of doing business. Chase Koch’s real education
about the family company had begun.
Chase Koch began a rotation of high-level jobs that exposed him to the strategic
pillars of Koch Industries’ modern business. It was telling what Chase Koch did not
learn. He was not sent to the oil refineries, or to a pipeline farm, or to a natural gas
processing plant. Charles Koch didn’t necessarily want to teach his son about the
energy industry. Instead, Charles Koch selected a series of jobs that reflected what
Koch Industries had become over the last decade and how it planned to carry on into
the future.
The rotation of jobs was set forth, roughly, as follows:
Class 1. Private equity acquisitions and mergers.
Class 2. Accounting and taxes.
Class 3. Market-Based Management training.
Class 4. Trading.
One of Chase’s first assignments was to Koch’s development group, the internal
committee that looked for new companies to acquire. He joined a division called
Koch Equity Development, which bought shares of publicly traded firms. Chase
worked in this office when Koch’s acquisition spree was at its peak, shortly after the
Invista and Koch Fertilizer deals and during the $21 billion purchase of GeorgiaPacific.
Chase assembled spreadsheets and did other analysis to figure out the best ways to
value a company. This was critical to Koch Industries’ overall strategy of developing a
sharper, more accurate view of the marketplace than its competitors. Koch was
looking for gaps in the market, small dysfunctions that presented opportunities for
Koch to seize.
Chase also worked in a group of tax and accounting analysts. This might sound
arcane and boring. Nobody grows up dreaming that they’ll become a tax analyst. But
Chase would have discovered that these skills were just as critical to Koch’s success as
was the company’s expertise in managing complex pipeline and refinery systems.
There was virtually no terrain in the American economy that was more complex,
more prone to manipulation, and more financially valuable than the American tax
code.
Managing Koch Industries’ massive tax liability—measured in the billions of
dollars each year—created a deep tension between two of Charles Koch’s primary
philosophical principles.
The first principle was that government taxation was little more than statesanctioned theft. Murray Rothbard, who cofounded the Cato Institute with Charles
Koch and Ed Crane, called taxes “state robbery,” to take one of many examples.
Taxation forcibly took money from a successful group of people and spent it in ways
that those people couldn’t control. It seemed morally justified to avoid paying taxes
however possible. But the second principle Charles Koch believed in was that of
10,000 percent compliance. Charles Koch espoused obeying the letter of every law,
every day. When the law required a company to pay taxes, it must pay taxes.
These two competing ideas led Koch to approach its tax bill in a way that became
standard for large corporations in America, from Apple to General Electric. Koch
used the US tax code’s own complexity as a tool to avoid paying as much in taxes as
possible. The company created numerous companies, limited liability corporations
(called LLCs, for short), and subsidiaries around the globe. Many of them seemed to
be little more than a name on a post office box. Charles Koch, for example, is listed as
an employee or director of such companies as KCM Advisors/GP, LLC; EKLP,
LLC;and FHR Alaska Guarantor, LLC.
It took massive amounts of time and effort to scatter these legal entities in a
network around the globe, but the payout for doing so was enormous. By 2016, the
US federal government was losing about $128.5 billion a year in tax revenue from
corporations due to the use of tax havens like the Cayman Islands or the small
European nation of Luxembourg. Such tax havens were only available to bigger
companies that could afford to employ teams of tax analysts, attorneys, and traders to
carry out the plans.
Koch Industries, like many US companies, had an office on Grand Cayman, the
biggest island in the small Caribbean nation. Koch’s office was nondescript and easy
to miss. It was located at 802 West Bay Road, a palm-tree-lined street that ran down
the west side of the narrow island, just a few minutes south of the Ritz-Carlton Golf
Club.
Grand Cayman is an island nation with no income tax and a permissive set of
corporate laws that have only basic requirements for a company to register there. A
company need only have a nameplate on a door, and perhaps an employee or two, to
set up shop on Grand Cayman. The tax-free zone of the Cayman Islands drew some
of the largest financial firms in the world to Grand Cayman, the largest of the islands.
There was a private school system on Grand Cayman that compared in quality to
those of the United States, along with high-end shopping, nightclubs, golf courses,
and seemingly endless miles of beach on which to spend the weekends.
Koch Industries had a surprisingly diverse array of holdings in the Caymans,
considering that the nation had few natural resources and very little in the way of
industrial infrastructure. A liberal activist group called American Bridge combed
through business registries in the Caymans and found more than two hundred
companies it suspected were tied to Koch, with names like Koch Minerals Cayman,
Ltd., Koch NGL Cayman, Ltd., and Koch Nitrogen Shipping, Ltd.
The ways in which Koch could employ such companies to avoid tax payments was
revealed in 2014, when a batch of tax documents was leaked to a watchdog group
called the International Consortium of Investigative Journalists. The documents,
prepared for Koch Industries by the tax consulting firm Ernst & Young, laid a
roadmap for shifting money from Koch’s operations to tax havens in Europe. The
arrangement, called “Project Snow,” created a complex web of obscure companies
that shuttled hundreds of millions of dollars between them. Koch used its Invista
division as a key component of Project Snow. It created an internal bank, called
Arteva Europe Sárl, that coordinated cash flows between the various companies. The
bank established a Swiss division that seemed designed to benefit from Switzerland’s
low tax rates. Money was passed back and forth, shares were converted into debt, and
companies were dissolved along the way. Some of the strategies seemed like financial
alchemy—in one case, a loan for $736 million was shifted between companies until it
eventually landed with a US subsidiary that was “both the debtor and the creditor of
the same debt,” effectively cancelling the loan. The Center for Public Integrity
reported that Arteva paid just $6.4 million in taxes on $269 million in profit between
2010 and 2013, and never had an annual tax rate higher than 4.15 percent. When the
tax documents were leaked, Koch’s public relations team said that the company
followed applicable tax laws.
Chase Koch’s education as a tax analyst at Koch would have taught him that
paying a tax bill was no simple thing. It was an arena of complex strategy and
potentially immense profits. In this way, tax analysis was similar to the next set of
skills that Chase Koch would acquire. After working in acquisitions and taxes, he
wanted to move to the part of Koch Industries that he knew was vitally important. “I
said, ‘Send me to Houston. I want to be in the pit with the traders,’” Chase recalled.
When Chase Koch was first given the chance to trade commodities, it was akin to the
first time he gripped a tennis racket. He discovered an arena in which he could excel
and in which he very much enjoyed spending time.
On the tennis court, Chase didn’t have to talk or explain himself. He only had to
face his opponent. On a trading desk, something similar happened. Here, the market
rendered a clear-cut verdict on whether Chase had made a good or a bad decision.
The market didn’t care about Chase Koch’s last name. It only cared about what he
did. Chase didn’t have to worry if anyone was pulling strings for him. The market
numbers were clear and inarguable.
“That was the first time . . . my blood started to move in my body,” Chase recalled
with a laugh. “You know what I mean? I got really excited about something. Because
I liked that feedback of trading—the market feedback—and just the energy on the
trading floor.”
Chase got a view of the trading operations that even most traders never got to see.
He spent weeks shadowing Brad Hall, the CFO of Koch Supply & Trading, who gave
Chase Koch a detailed overview of Koch’s entire trading group. Hall taught Chase
about the intricate accounting and tax systems that supported Koch’s trading
operations and gave Chase a view into forging large energy deals with Arab princes in
the Persian Gulf, executives of Asian oil refineries, and CEOs of American companies
like United Airlines.
It was clear to Hall and other leaders that Chase Koch was being groomed for a
senior leadership position in the company. Chase worked like he wanted to earn it.
“He was just full of questions and wanting to understand. He was the opposite of just
going through the motions,” Hall recalled.
Chase only sat on the trading desk in Houston for about a year before he was
rotated back to Wichita to work on the Koch Equity Development team. Around
this time, in 2006, Chase started feeling restless. His rotation through different jobs at
Koch gave him a perspective on the company that very few people could attain. But
he felt that his education was wide and shallow. He hadn’t mastered anything.
The chance to settle down and master one part of Koch’s business came when a
job opened up in Koch Fertilizer. Steve Packebush was still president of Koch
Fertilizer, and he offered Chase a job that put Chase in the middle rungs of the
division’s hierarchy. Chase became a regional salesman, traveling around the northern
central United States and selling fertilizer to farmer co-ops.
Early in his tenure, Chase Koch tagged along with a more senior salesman on a call
to a customer in Iowa. The customer was irate about an earlier deal and complained
for along time before he even noticed that Chase was in the room.
“Finally he looks at me, and he’s like, ‘And who are you?’ I was like, ‘Well, my
name is Chase,’” Chase recalled.
“And he goes, ‘You don’t know shitabout fertilizer!’” Chase said.
Chase replied“You’re right, sir. But I’m hoping you can help me with that.”
Chase grinded it out as a salesman and learned about the nitrogen fertilizer business
in an up-close and granular way. Then he shifted to the part of the business that he
loved the most: he joined the small group that traded fertilizer for Koch and was
given a small portfolio to trade a nitrogen-based product called UAN fertilizer.
II His
trading record was successful enough that he was given a larger and larger portfolio.
He estimated that he was eventually trading roughly half of the entire trading book.
This was a time when Chase’s career accelerated, based solely on the money he was
earning in the markets. No one could accuse him of getting ahead on his name alone,
and coworkers said that Chase seemed happy.
Wes Osbourn, who traded oil in Koch’s Wichita office, arrived at work early. But
he never seemed to arrive early enough to beat Chase Koch in the door. No matter
how early Osbourn arrived, Chase Koch’s car was always already parked in the lot.
One evening, when a group of traders went out to dinner, they invited Chase
Koch to come alone. Osbourn thought this was a mistake. He didn’t want to hang
out with the CEO’s son.
“I was like, ‘Ugh. I don’t want to go to dinner with this guy because he’s going to
be so arrogant. I’m not going to be able to take it,’” Osbourn said. As it happened,
Chase Koch arrived at Osbourn’s house early, and the two of them sat around talking
before dinner. Osbourn was shocked. Chase Koch was actually a nice guy, and he
seemed genuine. Over the course of the evening, the façade never cracked. It seemed
like he wasn’t faking it.
“If I hadn’t have known any better, I wouldn’t have known who he was,”
Osbourn said. “I remember at the end of dinner, we’re sitting there having a cocktail,
and I remember telling him how much I was not looking forward to that night. And I
couldn’t believe how down to earth he was. And [Chase] was like, ‘Well, I appreciate
that very much,’” Osbourn recalled.
The compliment was genuine, and Chase Koch must have appreciated it. But the
compliment was also a sharp reminder. No matter how he acted or what he
accomplished, he was still Chase Koch. The boss’s son.
Chase Koch’s sister, Elizabeth, followed in the footsteps of her uncle Freddie. She left
Wichita, moved to New York, and appears to have had no significant operational role
with the family company. Elizabeth became a writer, producing essays, short stories, a
book review, and other works of fiction that she published under a pseudonym.
Elizabeth founded a publishing company in Brooklyn, called Catapult Press, that
specialized in experimental fiction and other niche books. She retained a seat on the
board of the Charles G. Koch Foundation and sometimes attended the foundation’s
meetings in Washington, DC. One Koch lobbyist recalled Elizabeth’s visit to the
public affairs office. She arrived hours early, and the lobbyist was given the job of
entertaining her. They sat in his office and made small talk. She commented
approvingly on the office’s feng shui, and the lobbyist found her to be pleasant
company.
It seems that Elizabeth’s contact with Charles Koch was both limited and strained.
In 2008, she wrote an essay for the literary magazine Guernica that was a first-person
account of a woman having an unpleasant reunion with her father after not seeing
him in years.
Elizabeth wrote:
Last week my father came into town. I hadn’t seen him in six years. I got
drunk. He watched me eat dinner, his eyes wide, mouth open. My boyfriend
said the chicken bone cracked between my teeth like a candy cane.
The next morning, my father said good-bye. He kissed my cheek. “You
have a considerable hunger.”
“You don’t say,” my boyfriend replied.
As a child, Elizabeth had been an eager pupil of Market-Based Management. As an
adult, she left the burden of working at Koch Industries to her brother.
After his successes on the fertilizer trading desk, Chase Koch got a promotion. Steve
Packebush moved Chase into a new role in international development. Chase began
traveling the world, helping Koch Fertilizer expand its reach. During this time, Koch
Fertilizer built a network of terminals in Brazil, Mexico, Australia, the United
Kingdom, and France.
Pleased with these results, Packebush promoted Chase Koch again, in 2012, to
lead a division that made specialty products, called Koch Agronomic Services. This
job put Chase into contact with venture capitalists, inventors, and the heads of startup companies. They made high-end chemicals that were designed to counteract
nitrogen fertilizer’s extravagant inefficiency. Most nitrogen fertilizer leached straight
into the air and local streams after farmers sprayed it on their soil. Nitrogen runoff
from midwestern farms coursed into the Mississippi River and down into the Gulf of
Mexico, where the high nitrogen levels stoked algae growth that sucked oxygen out of
the water and created enormous “dead zones” that decimated aquatic ecosystems.
Koch bought a company called Agrotain that made additives to slow the process and
keep nitrogen in the soil.
Chase loved his work at Koch Agronomic Services as much as he loved trading. It
was thrilling to meet with inventors and get pitched on their new products. Chase
was more than just Charles Koch’s son now. He had a track record of his own in the
fertilizer business. He had done sales calls in Iowa. He had traded UAN supplies from
Wichita. He’d helped build terminals around the world. He knew what he was
talking about.
Packebush called Chase Koch into his office one day and offered Chase the biggest
break of his career. Koch Fertilizer was going to spin off its energy business, which
bought natural gas, and create a stand-alone fertilizer unit. Packebush wanted Chase
to become president of the new Koch fertilizer division.
“Packebush said, ‘You’re ready to take the keys to the beast,’” Chase recalled.
Chase became CEO of his own company with three thousand employees and
operations around the world that earned several billion in revenue each year. The
business owned multibillion-dollar fertilizer plants that required around-the-clock
supervision and vigilance to prevent lethal accidents. It was easily one of the most
important divisions of Koch Industries, ranking in size only behind Georgia-Pacific
and Flint Hills Resources.
Packebush was offering control over all of this to Chase Koch, if he wanted the
job.
“What I was thinking at the time,” Chase recalled, “was, Oh, shit.”
For the first time, Chase would be the public face of Koch Industries. The occasion
was a groundbreaking ceremony in October of 2013 at the company’s fertilizer plant
in Enid, Oklahoma. The company erected a small tent outside the plant for the event,
and Chase arrived in a suit and tie, a level of formality that was rare for senior Koch
executives. This was one of the first big public speeches of his career.
Koch Fertilizer was investing $1.3 billion in the Enid plant to expand its footprint
and ramp up production. There was a gold rush in the fertilizer business at this time,
thanks to the crash in natural gas prices, which boosted profits. Koch was pressing its
advantage, expanding its plant before competitors could enter the field and steal its
market share. This was the kind of announcement that companies liked to publicize
with ribbon cuttings and other ceremonies that drew local civic leaders. Under the
small tent, the folding chairs were filled by Enid’s civic leaders, plant employees, and
local law enforcement officers.
It was an awful day to make a speech. Strong, gusting winds forced everyone to
cling to their papers, and Chase’s hair was blowing into a mess when he stepped onto
the small wooden stage and walked to the podium. He delivered his remarks gamely,
however, speaking over the wind, and then turned to watch the earth mover perform
its ceremonial role. Chase also delivered remarks to a ballroom filled with more of
Enid’s business leaders. This time the sound was better. Chase read from a script,
which had the oratorical verve of a press release:
“Going forward, we are very, very excited about the future of Koch Fertilizer,”
Chase said. “We see positive trends in global demand as the population grows from
seven billion to nine billion over the next thirty to forty years, driving the need for
more efficient products, more services, and more innovation as we keep up with this
trend.”
Chase Koch didn’t come across as trying to impress anybody. He acted like the
same guy whom so many people had encountered over the years: quiet, low-key, and
humble. As he took over Koch Fertilizer, Chase revealed his leadership style, one that
was developed over decades of hard work, often in solitary spaces like the tennis court
or trading desks—he was quiet, focused on the matter at hand, and driven. If he came
across as subdued, he also seemed like someone who was increasingly comfortable in
his own skin. He could never escape the Koch name, but he was starting to wear it
with asense of ease.
Chase Koch’s confidence might have come, in part, to changes in his personal life.
On November 1, 2010, Chase married a Wichita girl named Annie Breitenbach, a
registered nurse who had gone to college at the University of Kansas. Leslie Rudd
noticed a change come over Chase after the wedding. Annie Koch clearly had a mind
of her own. She made her own decisions. Her independence seemed to give Chase his
own foundation as an adult. “I think that [Annie] was an ideal wife for Chase,” Rudd
said. “She’s smart. She’s got resolve, and she’s got her own opinion; it’s not influenced
by Charles or Liz. I think Chase feels that. He feels he’s got support beyond his
family.”
Chase and Annie Koch spent $3 million to buy a seventy-acre parcel of land in
Wichita for their home. Much of the property remained undeveloped. Chase Koch
now had his own family estate. He became a father when he and Annie had their son.
A second son followed.
In the small circle of Wichita business leaders, a lot of people were talking about
Chase Koch. His rise to the highest levels in Koch Industries seemed assured. Ever
since Chase was a kid, the specter had hung over his head—“WELCOME CROWN
PRINCE”—and now he was on his way to filling the job. The pathway to Koch’s
senior executive suite seemed to be short, straightforward, and predictable.
The only thing standing in Chase Koch’s way was the fact that he was miserable.
Being Koch Fertilizer’s president wasn’t what most people might think it would be.
The job was an exhausting, never-ending cycle of meetings. Chase Koch often arrived
at Koch headquarters around five or five thirty in the morning, well before dawn, and
was at his desk at an hour when many fathers had breakfast with their kids. Chase got
there early to prepare for the meetings, which started around six thirty and proceeded
—“wall to wall”—until six or seven at night. The meetings didn’t leave time for
Chase to develop much of a strategic vision for Koch Fertilizer. He was too busy on
the treadmill of supervising asprawling, complex, and dangerous industrial system.
Chase wasn’t willing to let details slide. He knew that small oversights could
cascade into a catastrophe. He didn’t let decision-making slip into other people’s
hands. And this turned out to be astrategic mistake.
“I let it overwhelm me,” he said. He began taking his misery and stress home with
him. His family life suffered.
Chase paid a visit to David Robertson, a longtime Koch executive who became
president of the company in 2005. Robertson was a taciturn executive who spoke
forcefully with carefully chosen words. He was a strict adherent of Market-Based
Management. He was also seen as a potential future CEO of Koch Industries. If he
got the job, Robertson would be the first CEO without the last name Koch. This
made him a competitor, in some people’s eyes, to Chase Koch. No one knew which
way the future might break.
If Chase Koch and David Robertson were both vying for the CEO position, they
didn’t act like adversaries. Chase turned to Robertson for help when he needed it the
most, and Robertson offered him wise advice.
“I walked into Dave’s office. I was like, ‘I need help. I’m really struggling in this,’”
Chase recalled.
Robertson asked Chase to walk him through a typical day. Chase talked about the
meetings, the bottomless needs of the organization. The strain it was taking on him.
Robertson told Chase that he had fallen prey to a classic mistake of leadership. He
was carrying too much on his shoulders.
Robertson said, “You control your calendar. You’re the only one that can say ‘No’
to things. . . . Take accountability for your own role and actually work on things
where you can add value,” Chase recalled.
Chase tried to learn how to delegate. He made sure he had the right people
working for him and trusted them to do their jobs. But still, it didn’t feel right. Chase
realized he was much happier before he’d been promoted, when he ran Koch
Agronomic Services. He loved the innovation of the job, meeting with investors and
inventors. Chase recalled a piece of advice that David Robertson had given him.
Robertson said the most important thing a leader can do is develop a vision. Now
Chase had a clear vision. It just wasn’t the vision that everyone else in Wichita seemed
to have for him.
Chase Koch called a meeting with Steve Packebush and told him the news.
“Steve, I’m not the right guy for this role,” Chase said. He wanted to quit.
Packebush tried to talk Chase out of it. “He said, ‘Just give it some time. This takes
time to really learn the stuff,’” Chase recalled.
Chase wouldn’t bend. He wanted Packebush to spin Koch Agronomic Services
into an independent company, and Chase wanted to run it. The job was less
prestigious, and it would look like a step backward, if not a permanent step away
from the path to becoming CEO. But this is exactly what Chase Koch insisted that he
do.
“I was like, ‘I need to be over here. This is where my passion is,’” Chase said.
In late 2015, Chase Koch demoted himself. He stepped away from the straight,
upward path to succeed his father. His reasoning was simple: “Life’s too short.”
When asked, years later, about his most important strategic decision as head of
Koch Fertilizer, Chase Koch thought for a while. Then he mentioned his decision to
quit.
“That was a big strategic decision, I think, for the overall business and for me
personally,” he said. The education of Chase Koch taught him that it was more
important to follow his own path, regardless of the expectations of others. It does not
appear that he ever regretted it.
Chase Koch’s decision disrupted what appeared to Koch employees as a clearly laid
plan of succession. When Chase stepped aside, an unspoken competition began
among senior Koch executives to become the first CEO after Charles Koch left the
company. This wasn’t the only source of uncertainty for Charles Koch in 2015. Even
for someone who embraced volatility, the events of 2015 and 2016 were unsettling.
The American public, it seemed, wanted to go its own way, regardless of the
consequences. There were murmurs of rebellion everywhere, which culminated in a
crisis of American governance that threatened to upend the political project that
Charles Koch had labored over for forty years.
There were rebellions and problems within the company as well. A stubborn,
deadly set of problems emerged inside Georgia-Pacific, one of Koch’s largest and
most important divisions. Perhaps most frustratingly, these problems refused to be
tamed by the tenets of Market-Based Management. People were dying, and the best
efforts of management didn’t seem to be working.
The anger among American workers was bubbling up, burning particularly hot in
Georgia-Pacific’s warehouse operations in Portland, Oregon. That’s where Steve
Hammond was about to make his final stand as an official with the IBU labor union.
I. During Hawley’s career at Wichita Collegiate, his players won fifty state titles by 2018 and he was inducted into
the National High School Tennis Coaches Association Hall of Fame.
II. UAN stands for urea-ammonium nitrate.
CHAPTER 23
Make the IBU Great Again
(2015–2017)
Steve Hammond volunteered to become a union official because he wanted to make
things better. He wanted to improve life at the Georgia-Pacific warehouse. He
wanted to curb the power of the Labor Management System and win pay raises for
the employees. He wanted to restore the Inlandboatmen’s Union to its former
greatness. Instead, he spent a remarkably large portion of his time tangled up in long,
complicated disputes with Koch Industries.
The IBU had hundreds of members in Portland, who worked for several
companies. But Hammond estimated that he spent 75 percent of his time handling
complaints from the hundred or so employees at the Georgia-Pacific warehouse. The
Labor Management System was grinding them down. They were forced to work
overtime, and were disciplined or fired for small infractions and absences. The
employees came into Hammond’s office constantly with their complaints,
demanding that he help them and file grievances. They begged him to win a better
labor contract when negotiations reopened. Every day, when he went into the office,
Hammond walked past the big stone plaque outside the union hall with the motto
“An injury to one is an injury to all.” The motto felt like an open challenge to
Hammond. It was an open question whether the motto, and the solidarity that it
expressed, was a museum piece, or whether it was an animating force that might be
employed for the benefit of workers.
This question was at the heart of Hammond’s last battle with Koch Industries in
2016. And this question was at the heart of a troubling trend inside Georgia-Pacific.
Confidential data from inside the company showed that the number of worker
injuries at Georgia-Pacific was rising steadily each year, as Koch pushed workers to
maximize profits and increase production. The rate of both small injuries and serious
injuries was on the rise. Burns, amputations, and deaths on the job were increasing
year over year, even if the public wasn’t aware of it. Hammond did not have access to
this data and was unaware of what was happening. But he saw firsthand that the
pressure on workers was intensifying. It was his job to put into practice the theory
that an injury to one was an injury to all, and to show that workers might still have
power to determine the conditions of their workplace.
In 2015, Hammond still worked in the little IBU office on the second floor of the
Longshoremen’s union hall, but he had a new boss. Gary Bucknum had stepped
down as regional director and was replaced by a man named Brian Dodge, who went
by the nickname Dodger.
Dodger was short and wiry, but he had the aura of an imposing union boss. He
spoke in loud, staccato bursts, and his blue eyes gleamed with intensity. He had
striking features, with a square jaw, spiky white hair, and commanding, deep-set eyes.
He made it clear in passing conversation that he carried a knife on his person at all
times. Shortly after he took the job, Dodge gave Hammond his own nickname, “the
Hammer,” which didn’t fit Hammond’s owlish presence but seemed fitting for a
union man.
The Dodger and the Hammer sat side by side in the cramped office. Hammond
often remained silent while Dodge took phone calls from IBU members up and
down the Columbia River. “Hey, brotherman,” Dodge said when answering the
phone. Then he bellowed: “You just fucked me!” before breaking into near-maniacal
laughter. He launched into the disputatious patter of a union boss: “Yeah. Ouch. Pay
ten more an hour. Tankerman—not a lead tankerman—makes forty dollars and forty
cents. Okay—so that’s okay. Thirty-four dollars. That gives me something to push at
them.”
In 2015, the Dodger and the Hammer were going to take on the biggest challenge
of their new partnership. It was time to renegotiate the labor contract with GeorgiaPacific. The brutal negotiations of 2010, which lasted eighteen months, had left the
union scarred and nearly broken. When that contract was about to expire in 2013,
the IBU didn’t negotiate but chose to preemptively surrender. With the backing of
the union members, the Hammer and the Dodger told Koch that they wanted to
“roll over” the 2010 contract, meaning that they would accept all its terms and keep it
in place for two years. This cemented the defeats of 2010—including the low annual
pay raises—but it allowed the union members to keep their pension and spared them
another draining battle.
In 2015, the union members made it clear that they didn’t want to roll over again.
They wanted the Dodger and the Hammer to fight for something better. It was
around this time that Steve Hammond started drinking every day. Drinking had
always been a part of life at the warehouse. Guys would share beers in the parking lot
after a shift. Hammond used to drink Scotch on special occasions, sipping a glass of
expensive Glenlivet now and then. After starting his full-time job at the IBU, he
started drinking Scotch weekly, then nightly, then switched to the cheaper stuff, like
Dewar’s and Johnnie Walker Red.
“Pretty soon I was drinking a half to three-quarters of a bottle a day,” Hammond
said. “I’d just sit [at home] every night and get blasted. Then I’d fall into bed, wake
up, feel like shit, and go in and go to work.”
If Hammond’s drinking had become toxic, so had life inside the IBU. A weird
dynamic had developed between the union officials and the employees. It was sort of
like the dynamic between a parent and an angry teenager, an intimate bond that was
woven with threads of resentment and dependence. Back in the 1980s, union
members considered the IBU officials to be like spokesmen—the union members
decided what they wanted, and the union delivered the message. Now the union
members seemed to consider the IBU officials to be like a second layer of
management. They thought the IBU officials were somehow in charge, somehow
capable of bargaining for a better deal with Koch, and somehow in the position to
resolve disputes with Koch management at the warehouse. Hammond believed that
this modern view was exactly backward. The real strength of a union came from its
members, and their willingness to stick together and strike. It didn’t come from the
union office. And yet, all the union members kept turning to the union office,
seeking solutions.
The Dodger got an early lesson in this dynamic after he became regional director
and negotiated the contract rollover in 2013. The IBU members agreed to the
rollover, but only grudgingly. Dodge felt the rollover was their only choice. After just
a few contacts with Koch, Dodge quickly learned the limits of bravado as a
negotiating tactic. Koch was unmovable. “Guys in California get thirty dollars an
hour. These [IBU] guys get forty! How the fuck can I go in there and try to get them
big raises? You tell me—please! I have no idea,” Dodge said.
When Hammond had joined the union, the members met every week. Now they
met once a month (excluding July and August). The meetings used to draw two
hundred people. Now they drew about fourteen. Most members who attended were
on the union executive board, meaning that one or two members showed up who
weren’t required to be there. When large numbers of union members did show up, it
was to complain. And when they complained, they wanted Hammond and Dodge to
solve their problem.
“You almost feel like you’re Mom and Dad in there,” Hammond said. Life in the
warehouse seemed to get worse by the day, and the union should have made things
better. Disengagementand cynicism were contagious.
The discontent throughout Georgia-Pacific went beyond economic concerns. As
productivity and profits increased, serious injuries had increased in tandem. There
was something broken with the system, and the problem was intractable. Senior
leadership at Georgia-Pacific was aware of the problem, from CEO James Hannan
down to the managers on the factory floor. But nothing they did seemed to slow the
injury rate between 2010 and 2018. In 2014, the number of worker deaths spiked to a
level that hadn’t been seen since the early 2000s. Concerns were mounting at the
highest levels. “What we do is kill people at Georgia-Pacific,” said one longtime
employee at Georgia-Pacific.
When Koch Industries purchased Georgia-Pacific in 2005, it inherited a new
monitoring system at the company, called TRAX, that recorded a wide variety of
metrics about the company’s operations. This information was collected in a
centralized database for analysis, allowing Koch to improve safety and increase
productivity throughout the company. Analyzing data in the TRAX played a vital
role in helping Koch boost profits and helping Georgia-Pacific pay down the billions
of dollars loaded on its balance sheet after the acquisition. A key metric recorded by
the TRAX system was workplace injuries and accidents.
Between 2005 and roughly 2009, the TRAX data set was spotty. The company
was still engineering the system, figuring out what to record and training employees
to enter data into it. By 2010, TRAX was fully operational. That year, the system
recorded a total of 579 “OSHA recordable injuries” across Georgia-Pacific, meaning
injuries that were significant enough that they must be reported to the US
Department of Labor’s Occupational Safety and Health Administration. That year,
one worker was killed at Georgia-Pacific.
Managers at Koch Industries had reason to be satisfied with these results. They
marked a significant improvement over Georgia-Pacific’s performance before Koch
purchased the company. Throughout the 1960s and 1980s, worker safety standards
were abysmal. “It was like ‘Welcome to [Georgia-Pacific]. Watch your ass,’” one
employee recalled.
Even by the early 1990s, Georgia-Pacific was reporting six worker deaths a year
across the country. Things improved that decade but worsened during the early
2000s. This was the period when Wesley Jones, the Georgia-Pacific executive in
Georgia, said the company dramatically cut back investment in its factories because it
was loaded with debt. In 2000, seven workers were killed at the company. Six were
killed each year in both 2001 and 2002. Things improved once again, and in 2004 no
employees were killed.
Koch Industries was delivered something of a reprieve beginning in 2008, when
the housing market crashed. Orders for building materials slowed dramatically, and
during the recession that followed, orders for paper and tissue plummeted as well.
During this down cycle, Koch Industries did what it does best: it invested against the
economic cycle, pouring billions of dollars into Georgia-Pacific. A lot of this
investment went toward improving safety measures.
This was no simple matter. Workplace safety is an engineering problem from hell.
It involves an almost limitless number of factors that interact with one another in
impossibly complex ways. A plant manager must consider the dangers of each giant
machine, and the multiple ways that each machine might take someone’s life. Then
they must consider how each machine interacts with one another in a complex
production cycle that, in many cases, runs twenty-four hours a day.
Finally, there is the human element. People are maddeningly unpredictable. They
improvise on the job, they break rules, they put themselves in unexpected places and
create unforeseen hazards. Koch fought against these factors in two ways: by
updating the equipment and updating the thinking and behavior of its workforce. At
a large gypsum factory outside Savannah, Georgia, for example, Koch installed new
fencing around dangerous machines and changed long-standing practices that put
employees in harm’s way. Bright yellow barriers were erected throughout the factory
to keep workers away from spinning parts and other barriers.
Koch’s largest transformational efforts to improve safety were cultural. Across the
company, employees learned about Market-Based Management and how it could be
used to prevent accidents. They learned about the Ten Guiding Principles and the
five dimensions of MBM, and were told that this belief system would help them
simultaneously ramp up production while remaining safer. Maybe more importantly,
workers were bombarded with the message of 10,000 percent compliance and
repeatedly encouraged to shut down machines if they considered conditions to be
unsafe.
During the lull in production after the housing crash, worker injuries declined. An
internal Koch report showed that there were 730 reportable injuries at GeorgiaPacific in 2005, before the acquisition. Koch had cut that number by 20 percent.
Still, one worker was killed every year at Georgia-Pacific, except for 2007, when four
workers were killed on the job.
By 2010, Koch Industries managers believed that they had put systems and
practices in place that would lock in these safety gains. Between 2010 and 2011, the
number of recordable injuries fell from 579 to 545.
In 2011, the housing market and the economy began to recover. The number of
new homes being built rose about 21 percent over the year, until there were 697,000
new home starts in December. This upward march in home construction would
continue for years, and it increased demand for plywood, gypsum board, insulation,
and other building materials. Orders started pouring in to Georgia-Pacific.
Koch’s newly renovated operations at Georgia-Pacific were put to the test. The
system was an unmitigated success in one respect: the factories and mills were more
efficient and more productive. Profit margins increased, revenue increased, and Koch
Industries began aggressively paying down Georgia-Pacific’s debt. Before Koch
bought the company, Georgia-Pacific’s debt was rated as being junk bonds, meaning
there was a high risk it would not be repaid. But the debt ratings increased steadily as
Georgia-Pacific’s factory hummed with new precision. In 2016, Georgia-Pacific’s
debt was rated A+ by Standard & Poor’s, meaning that it was high-investment grade.
Profits roughly doubled. The year before Koch bought Georgia-Pacific, the company
earned $623 million in net profit. By 2016, Koch had increased that to an average of
more than $1 billion.
This improvement made Georgia-Pacific’s CEO, Jim Hannan, a rising star within
the company. Hannan had been on the scouting team that first inspected GeorgiaPacific in the early 2000s. After taking the helm of the company, he behaved as the
quintessential Koch man. He was relentless, focused, projected humility, and
delivered positive results. He spoke fluent MBM, and attributed the company’s
success to its operating philosophy rather than to his personal attributes.
But one stubborn problem emerged in the shadow of the rising profits. Between
2011 and 2012, workplace injuries jumped from 545 to 584. This would have been
displeasing to Charles Koch, who prided himself on running clean operations that
were both safe and profitable. But the small gain could have been easily dismissed as a
fluke. The number of injuries fell slightly from 2012 to 2013.
Then, after 2012, housing starts rose more sharply, and working conditions
became more unsafe year after year at Georgia-Pacific. Deaths began to rise, and the
number of injuries rose in almost perfect tandem with the numbers of orders that
came through the door between 2012 and 2014.
Injuries jumped sharply between 2013 and 2014, from 527 to 644. Nine
employees that year lost limbs or body parts. One hundred and fifty-four employees
suffered heat burns, up from 134 the year before and 126 the year before that. The
number of electrical shocks jumped to nineteen in 2014 from one the year before. In
2013, two workers were killed on the job.
In many ways, the increasing harm to workers made no sense. Koch was
continuing to reinvest in the factories. Managers were told to hammer home the
message of 10,000 percent compliance and “safety first.” The rhetoric was
unambiguous. But more people were hurtall the time.
Most alarmingly, it wasn’t just the number of injuries that rose. The rate of
injuries also increased. This destroyed the argument that perhaps more people were
getting hurt just because more people were working more hours, increasing the odds
of an accident. The accident rate, as measured by OSHA, climbed steadily each year
from 2013 to 2017, rising 44 percent during that period. It was increasingly
dangerous for employees to show up for work.
Between March 17 and 18, 2014, Hannan joined a group of senior executives for a
team meeting in Atlantato discuss the safety concerns.
“The last six months is unacceptable,” Hannan said, according to notes of the
meeting that were taken by someone who observed it. Hannan referred to accidents
and deaths at Georgia-Pacific as “learning events,” the idea being that each accident
taught the company better ways to be safe. But the company was failing to learn.
Hannan emphasized that the corporate culture would play a critical role in solving
the problem. “We need to have a culture of values and not tolerate individual or
organizational risk. We must learn from one another. Work on the items with the
most risk.”
“Build on an MBM®-basedI culture,” the notes read. Hannan suggested that the
future of the company was on the line. “If we can’t keep safe, why invest?” Hannan
asked. Market-Based Management should be solving this problem. But it was not.
During this period, Koch Industries changed the way people worked on factory
floors across Georgia-Pacific. The company managed to cut the number of unionized
workers in half, from 22,000 in 2005 to roughly 11,800 in 2016. This gave Koch
flexibility and allowed it to avoid the type of onerous work rules that Charles Koch
opposed since he took over the Pine Bend refinery in 1972. These changes were
evident at Georgia-Pacific’s sprawling mill outside Savannah, one of the largest tissue
and paper towel mills in the United States.
The mill was highly mechanized, and its cavernous interior was clean and pleasant
to walk through. The space resembled an industrial Santa’s workshop; a complicated
maze of automatic machines that rolled, spun, and packed countless rolls of toilet
paper. Automated forklifts drove between the machines, guided by lasers beams
aimed at the floor in front of them. Employees monitored the machines and fixed
them when there was a problem. One of those employees was Dana Blocker, a
muscular and intense man who had worked at Georgia-Pacific since the 1990s.
Until Koch bought the company, employees like Blocker had worked with specific
job descriptions and were assigned to oversee specific machines. A person was a
winder operator, for example, or a wrap operator, or a case pack operator. After Koch
took over, those distinctions were dissolved. Blocker’s job title became “reliability
technician,” meaning that he oversaw a wide variety of machines and processes.
“Now you’re a technician, expected to go out and run all the equipment on the
line. So, no one is tied to one piece of equipment. You have to run the entire process,”
Blocker said. “When people ask me now, what’s my job, what do I do? I run the
entire line. I don’t have one specific job. Whatever needs to be done, that’s what
you’re going to do.”
Blocker’s coworker, Mark Caldwell, said this created a new flexibility in the
workforce. “You probably couldn’t tell who the manufacturing engineer is, or the
mechanic, or the technician. You wouldn’t be able to distinguish who does what role,
because we all flow to the work. We all do what needs to be done.”
Both men praised the new system. Blocker said that it helped foster teamwork and
galvanized him to think like an entrepreneur rather than a simple factory hand. “That
seemed to help everybody out. There’s no blaming or finger-pointing at anyone for
running something a certain way. You’re all trying to help each other out to get the
best product,” he said. Both men also emphasized that their managers encouraged
them to shut machines down in the event of hazards. Safety came first.
While unions seemed stubborn in clinging to work rules and job designations, the
tradition of doing so traced its roots back to unsafe working conditions in the early
1900s. Being confined to a certain job helped workers reinforce their expertise not
just on a specific process but also on a specific machine. The equipment inside
Georgia-Pacific was of a scale that demanded such intimate expertise. Some machines
were the size of a small house and ran giant, spinning roles of paper that weighed two
thousand pounds. Knowing the quirks and dangers of such machines was vital. But
Georgia-Pacific employees were increasingly put into situations where they were
learning on the job.
Koch Industries tried to mitigate these safety risks by imposing a complex set of
rules and regulations on the daily life of workers. The regulations and standards were
codified in a series of papers accessible through the company’s internal computer
network. Employees were told to learn the rules, but this was not easy. One “work
standard” paper dictated how employees should conduct themselves when taking on
“nonroutine” work outside their typical operating procedure, and the document was
more than twenty pages long. Another work standard, dictating how employees
should shut down machines to repair them, was about twenty-five pages long. One
employee estimated that the total number of work standards reports were a thousand
pages combined. Workers were expected to follow these standards, and could be cited
for violations if they did not.
In 2014, this was the system in place when a wave of deaths swept across GeorgiaPacific.
On August 11, 2014, a forty-one-year-old man named Robert Wesson was working
at Georgia-Pacific’s paper mill in Crossett, Arkansas. He lived in the nearby town of
Hamburg with his wife, Lisa. Wesson had a thin and angular face, short-cropped
black hair, and a finely trimmed beard that traced his sharp jawline. He was working
with a large paper winder that day: a machine that spun industrial-sized rolls of paper
weighing thousands of pounds.
As the big rolls went down the conveyor line, Wesson applied tape to the “tails” so
that the rolls would remain tightly coiled when they were shipped.
II For reasons that
remained unclear, Wesson left the area where he was supposed to stand and walked
farther down the line to apply more tape to the rolls, perhaps because the first
application wasn’t working. His movements could be described as “nonroutine” by
Georgia-Pacific’s standards. If Wesson was trying to compensate for a problem with
the taping process, then Koch’s voluminous work standards might have
recommended that he follow a procedure that employees called LOTO or “Lock-out,
Tag-out.” The LOTO would have required Wesson to lock the machine down by
stopping it, and then record the reasons for doing so before verifying again that the
machine was in fact turned off. Georgia-Pacific’s LOTO work standard paper was
roughly twenty-five pages long. Wesson did not follow the LOTO procedure, and he
approached the rolls instead to apply the tape. Production ran smoothly.
As Wesson approached a paper roll, he failed to take into account the movements
of alarge piece of machinery called a “kicker,” a giant metal arm that shoved the heavy
rolls down the assembly line. As Wesson stood near the roll, the kicker engaged and
smashed his skull, killing him. His coworkers later discovered his body.
Wesson’s death was the fifth fatality at Georgia-Pacific in 2014.
A few months earlier, in March, when Hannan attended the safety meeting in
Atlanta, no workers had yet died that year. Hannan had reported this piece of good
news to the team, but it turned out to be an anomaly. Accidents and the injury rate
were sharply higher by the end of the year.
Roughly a month after Hannan’s presentation, a contractor named Sam
Southerland was working at Georgia-Pacific’s plant in Pennington, Alabama. He was
not intimately familiar with the facility. Southerland, who went by the name Sambo,
was twenty-nine years old and married to his childhood sweetheart, Michele. He had
a son named Carson, and a newborn daughter named Caylin. Southerland was
something of a country boy, with a broad smile, who loved to hunt and play baseball
with his son. On April 15, Southerland was inside the Georgia-Pacific factory,
holding the bottom of a twenty-eight-foot extension ladder. He stepped backward,
perhaps trying to find a better place for the ladder, when he fell into a hole in the
floor. He plunged thirty feet into a cauldron of noxious chemicals that is called a
“digester,” an apparatus that processes raw materials for the paper-making process.
Southerland sustained multiple bone fractures from the fall, along with chemical and
thermal burns on his body from the digester, and was killed.
Less than two weeks later, at Georgia-Pacific’s plant in Corrigan, Texas, a fire
broke out in a tall silo that captured wood dust. Employees rushed to the location to
put the fire out, many of them apparently floor workers who were not trained
firefighters. Some bags inside the silo were blocking a group of vents designed to
release flames and pressure inside the silo in case of emergency. Pressure built up, and
then the silo vents released, engulfing the employees in flames. Different news
accounts said between seven and nine employees were burned and transported to
local hospitals. Some of them languished in burn wards for weeks. On May 30, afiftysix-year-old Georgia-Pacific employee named Charles Kovar died from his wounds.
About one week later, fifty-eight-year-old Kenny Morris died in the hospital. Both
men left behind wives and children. Kovar’s obituary suggested that he had lived a
full life that was enriched by his Christian faith: “He had just experienced his best
Easter ever where he cleaned out the bowl of Aunt Diane’s famous banana pudding,”
the obituary said.
On July 24, asixty-three-year-old Georgia-Pacific employee named Lydia Faircloth
was leaving her shift at the company’s mill in Cedar Springs, Georgia. Just two years
earlier, Faircloth had been featured in an internal Georgia-Pacific safety bulletin. She
had coined a phrase to promote safety awareness: “LET OTHERS SEE SAFETY IN
YOU,” according to the bulletin. It was close to midnight when Faircloth was leaving.
She cut through an area where industrial loader trucks were transporting big loads of
product. She crossed the floor in a crosswalk marked for pedestrians, but was hit by a
truck driven by her coworker and died from severe internal injuries.
It was less than a month after this that Wesson was killed at the mill in Crossett.
Roughly ninety days after that, a contractor named Bobby Creech at the Crossett
mill was performing lawn maintenance at the mill while riding an off-road four-wheel
vehicle. When Creech traveled over a hill, the vehicle rolled over and killed him. This
contractor’s name was spelled variously in internal Koch documents as Bobby Creech
and Bobby Creach, but there is scant documentary evidence of his death.
By Christmas 2014, six workers had been killed in Georgia-Pacific. And the injury
rate and total number of injuries continued to climb. The accident rate jumped 18
percent from the year before. The total number of reportable injuries jumped by 22
percent.
Between 2015 and 2017, accidents and injuries continued to climb each year, along
with the rate of injuries. The increasing danger at work seemed tightly linked to
increasing production: the upward trend of injuries still mirrored the upward trend
in new home construction and economic growth.
The chart below documents recordable injuries, drawn from Koch’s own internal
tracking system, TRAX. The total number of accidents increased by 30 percent
between 2010 and 2017:
The injury rates rose even more sharply during this period. Koch’s TRAX system
recorded two injury rates: the “OSHA Rate,” which tracked injuries, and the “DART
Rate,” which basically tracks lost work time due to injuries. The OSHA rate increased
by 45 percent, and the DART rate increased by 57 percent:
Koch Industries needed to change the way it did business at Georgia-Pacific. But it
wasn’t clear how it would do so. In the past, Koch changed dangerous procedures
after strict government enforcement, coupled with publicity of the company’s
wrongdoing. In the 1990s, the raft of criminal charges and civil fines for
environmental violations prompted Charles Koch to develop the 10,000 percent
compliance doctrine. The crisis of workplace injuries appeared to follow a different
path. Federal regulators ruled that Koch Industries had violated dozens of federal
worker-safety regulations at its Georgia-Pacific facilities, but the fines for doing so
were relatively paltry.
Georgia-Pacific was fined $5,000 for violations related to the death of Robert
Wesson, according to OSHA records. The company was fined $14,000 for violations
related to the burn-related deaths of Charles Kovar and Kenny Morris. It was fined
$35,050 for a series of violations dubbed “serious” by OSHA related to Lydia
Faircloth’s death. These deaths were scattered around the country and garnered little
mention outside of local media accounts, which often characterized the deaths as
accidents and provided little information beyond that. By contrast, the EPA and the
Department of Justice fined Koch $30 million for a series of pipeline leaks and other
violations in 2000, grabbing national media attention because it was the largest such
fine in history.
In the absence of headlines and fines, Koch Industries responded to the GeorgiaPacific safety crisis by reemphasizing the need of employees to follow the guidelines
of Market-Based Management. An internal Koch Industries presentation prepared in
2017 referred to the crisis in terms that military commanders might use to describe a
large-scale insurgency. The “Headline Discussion” of the presentation said that Koch
needed to “Engage Hearts & Minds” of employees to reverse the increasingly
dangerous conditions. “Are we putting too much emphasis on ‘we are improving’
versus we are not satisfied with where we are and our rate of improvement?” the
presentation asked. The presentation noticed that serious injuries were “flat to
increasing” between 2016 and 2017, in spite of the company’s efforts.
The presentation noted that Georgia-Pacific was more unsafe than Koch’s
competitors. One internal chart showed that Georgia-Pacific’s safety metrics ranked
in the bottom half of paper and pulp companies in the United Statets. Significantly,
Georgia-Pacific ranked below its three major US competitors: Weyerhaeuser,
International Paper, and Pratt Industries. The only companies that ranked below
Georgia-Pacific were relatively obscure and sometimes small firms, such as Deltic
Timber Corporation, Flambeau River Papers, and Turners Falls Paper.
This chart was a challenge to Koch’s senior leadership. None of the companies
that ranked ahead of Koch subscribed to Market-Based Management, yet they all did
better than Koch. The numbers challenged the company’s orthodoxy.
Koch’s response was to renew its commitment to Charles Koch’s philosophy and
to reduce risk by “applying 5 MBM® dimensions throughout the organization.” The
leadership team set out an ambitious goal. It sought to achieve “zero significant
incidents” at Georgia-Pacific in the future. One chart showed a “Georgia-Pacific
Safety Risk Glide Path” that would gradually reduce accidents to a level near zero by
the year 2035. A different chart noted that every 10 percent decrease in serious
incidents would yield between $5 million and $25 million for the company.
Another chart, entitled “Georgia-Pacific 20 Year Bet,” was written in the classic
style of Market-Based Management materials. It featured colored boxes connected by
dark lines in a wheel-and-spoke formation. The box in the center said, “Critical Risk
Focus Areas,” and the connected boxes listed various Georgia-Pacific operations and
risk hazards like “Combustible Dust” and “Electrical Safe Work Practices.” (Electrical
shocks had skyrocketed at Georgia Pacific, rising from one in 2010, to twenty-three in
2015, and to thirty-one in 2017.) The chart said that risk could be reduced by
changing “hearts and minds” in the workforce. It said the company workers must
change their mind-set and “Go from Have To—To Want To” in terms of staying
safe. In spite of this approach, workplace accident rates continued to accelerate that
year.
In past decades, worker safety was a top priority for labor union negotiators.
Industrial accidents were a driving force behind unionization in the early years of the
New Deal. By 2016, however, unions were so marginalized and overpowered that
they were playing a defensive game, simply trying to hold on to what benefits they
had left.
This was the reality faced by the Dodger and the Hammer as they prepared to
negotiate a new contract with Koch in 2016. Hammond knew that this would likely
be the last contract he negotiated on behalf of the IBU, his last chance after nearly a
decade to make things better.
Before negotiations even began, Georgia-Pacific sent powerful and ominous
signals to the IBU. In 2015, Koch Industries told the IBU that it was pulling GeorgiaPacific’s representatives off the board of trustees that oversaw both the IBU’s pension
and the health care trust. It was common for companies to help oversee the funds,
and Koch’s withdrawal seemed like the first step toward ending all support for the
pension and health care plans.
The Dodger was alarmed. “All the sudden, I’m thinking, Are they going to pull out
of the health trust completely and shove this up our ass?” he said.
The IBU team reached out to Jackie Steele, a labor relations expert at GeorgiaPacific who was their new negotiating partner. Steele sent a message: Georgia-Pacific
might be able to let the workers keep their pension and health care, or it might be able
to give them araise. But it seemed impossible that the company could do both.
Dodge and Hammond conveyed this message to the rank-and-file union members.
The union members weren’t having it. They wanted to keep their benefits, and they
needed to get a raise on top of it. The raises hadn’t been keeping up with the cost of
living for years. “The guys want more, more, more, more,” Dodge said in
exasperation. “They don’t know what you’ve got to go through!”
The IBU members were not inclined to listen to Hammond and Dodge. In fact,
they were not inclined to the listen to the union at all. This became painfully clear in
early 2016, a presidential election year. The IBU and the Longshoremen unions
endorsed the Democratic candidate Bernie Sanders. When Sanders lost his primary
battle, unions across the country asked their members to switch their support to what
they considered the next best thing: the Democratic nominee, Hillary Clinton. Many
IBU warehouse workers, for the first time that anybody could remember, said they
planned to vote against the wishes of union leadership. They wanted to vote for a
Republican. And their grievances were about to be further enflamed.
Once again, the Dodger and the Hammer arrived at the Red Lion hotel to negotiate
with Koch’s team. The IBU members took their assumed seats in the familiar
conference room with the view of the river, just next door to the lavishly catered
room where Koch’s team of negotiators sat staring at their laptops. It was like
watching the same movie for the third time. At least this time around, the process was
mercifully short.
On the second day, they discussed the money. Dodge said that the IBU workers
wanted to keep their IBU health care and their IBU pension. They also wanted
annual raises to compensate them for roughly six years of stagnant pay.
“I said, ‘Is there any chance on that, and what do you think?’” Dodge recalled.
“Steele says: ‘Yeah, we may be able to work something out.’”
Steele left the room. He returned with bad news. The company wasn’t going for
it. If the IBU wanted to keep its pension and health care, then Georgia-Pacific would
not offer them annual raises. The company would offer an annual bonus payment
instead.
Bonuses were anathema to workers because a bonus didn’t compound in value
every year the same way thata wage hike did. Raises had been aladder for middle-class
prosperity for decades. But since the economic crash of 2008, US employers started
to abandon annual wage increases. Even as recently as 1991, bonuses and temporary
awards accounted for only 3.1 percent of all compensation paid by US companies.
Annual wage hikes, by contrast, accounted for 5 percent of all compensation that
year. This ratio had flipped by 2017, when bonuses accounted for 12.7 percent of
compensation spending, and raises accounted for just 2.9 percent.
The Dodger said he wasn’t having it. If he didn’t walk out of the Red Lion with a
contract that promised annual raises, then his union members would vote down the
contract.
“Work with me, Jackie!” Dodge recalled saying.
By the end of that day, the Dodger and the Hammer had relented. They agreed to
the 2 percent raises for two of the years and $1,000 annual bonuses for the other two
years of the contract. “The worst contracts I’ve ever negotiated—all of my G-P
contracts,” Dodge said bitterly. “There’s no leverage. There’s no fucking leverage.”
In all, the contract negotiation took less than a week of bargaining. Dodge told
Jackie Steele that if Georgia-Pacific wanted the contract passed, then they should help
him hold the vote as soon as possible. The company agreed to release its employees
from work hours early so they could drive down to the union hall for the vote. “The
only way I’m gonna pass this piece of shit is to have them all here,” Dodge said.
The IBU members filed into the big Longshoremen’s union hall, just downstairs
from Hammond and Dodge’s office. Ballot boxes had also been prepared for the
day’s vote. The workers gathered around a stage at the far end of the big room, a
slightly elevated platform with an American flag and a podium that was emblazoned
with the Longshoremen’s crest.
Steve Hammond looked out over the crowd of workers, who were already
grumbling. As he looked around the room, he saw symbols that reflected the power
of organized labor. There was the big mural showing the labor strife and the solidarity
of the old days. On another wall hung the banner of the Jack London poem “The
Scab.” And next to that was a big glass display case full of old handheld cargo hooks.
The place looked like a museum of union power. The totems, the banners, the mural.
All of it had atainted, aging quality. Like paper that was yellowing.
Word had spread through the crowd that they would not get annual raises. It was
inconceivable, to many members, how something like this could have happened.
Why were they paying union dues, if the contracts just seemed to get worse? Why
were they constantly told that their warehouse performed far better than most
warehouses in the Georgia-Pacific system, yet none of the improvements translated
into asignificant pay raise?
Why hadn’t Hammond bargained harder? Why hadn’t Dodge bargained harder?
Why couldn’t they ever seem to win?
“Guys were pissed off. Guys in the warehouse were screaming bloody murder.
And: ‘No way!’” Dodge said. “They got loud and vocal.”
Steve Hammond took the stage. And, for the first time that anybody could ever
recall, he completely lost his shit.
Hammond upbraided the gathered union members. He scolded them. He
insulted them. He told them, in so many words, that they had expected him and
Dodge to do exactly the one thing that labor negotiators could not do: win a deal
with their silver tongues.
Union power came down to bargaining leverage, and the IBU had no leverage.
The warehouse employees couldn’t afford to strike, and everybody knew it, including
Koch Industries.
David Franzen listened to the speech, slightly awed to see Hammond lose his
temper. “He’s saying, ‘This is it guys. This is your best offer. You’re not going to
strike anyway,’” Franzen recalled. “‘If you didn’t do it last time, what makes you
think you’re going to do it this time? None of you guys did anything about it. We
told you to get ready in four years, and you didn’t get ready.’”
Then Hammond made the comment that everyone remembered for years: “You
guys are nothing but a bunch of Trump lovers. Go ahead—vote for him,” Franzen
recalled Hammond saying.
Hammond was finished, and he got off the stage. Dodge didn’t quite know what
to think. Hammond had actually turned into the Hammer, but against his own
union members. “He basically told them off and told them: ‘Vote no on the fucking
thing. Dodger and I will sit back down and talk some fucking more with them.’”
The union members cast their vote in an election that felt like a foregone
conclusion. The contract passed with over 65 percent of the vote. And that’s how
Steve Hammond retired from the IBU.
Hammond sobered up after he retired in March of 2016. He spent months just
sitting in his home, trying to process what had happened.
Hammond didn’t have much to complain about, personally. He retired with his
full pension—$3,000 a month—plus Social Security. His two daughters were grown
and happy, and he visited with them frequently. He was remarried and happy. What
made him sad was thinking of the IBU members he’d left behind. He had joined a
raucous, militant union, and he had left a splintered, moribund union. And what he
saw at the IBU seemed to be happening across the country.
“I think that we kind of fucked ourselves, to tell you the truth,” Hammond said in
his living room, near a big window that let in soft lightand offered a view of imposing
cedar trees and rolling green grass. “I think that our forefathers—just using that
[warehouse] as an example—worked their asses off to get these great contracts and
stuff. And then got these great jobs for their kids, and nephews, and little brothers,
and stuff like that. And we had all this: Work forty hours a week. Work five days a
week. If you worked Saturday and Sunday it was time and a half for Saturday and
double time for Sunday. And all that great stuff, you know?
“And we came in, us kids of theirs, and just pissed it away. We just took it all for
granted that this was ours.”
During the final months of 2016, the members of the IBU turned their attention to
another election, for president of the United States. The real estate magnate, reality
television star, and Republican candidate Donald Trump campaigned tirelessly
throughout the fall. He settled on a consistent theme: the election was rigged. It was
controlled by dishonest forces that were allied against working families. And Hillary
Clinton, “Crooked Hillary,” was the face of athieving elite.
This story line resonated with many IBU members, like David Franzen. For all his
adult life, Franzen had been hitting the “Democrat” button when he voted, but his
life did not seem to be improving in material ways. His union told him to vote for
Hillary, and for the first time, he wasn’t going to listen.
Trump’s candidacy was also disrupting Charles Koch’s plans. In April of 2015,
Charles Koch had given a rare interview to USA Today to outline his political strategy
for 2016. Koch planned to be more engaged than usual in Republican politics. His
donor network would, for the first time, give money to influence the field of
Republican primary candidates. The network planned to spend $900 million, an
amount that rivaled the Republican National Committee’s spending. Roughly onethird would be donated directly to candidates, with the rest going toward
“educational” efforts and other activities. Koch told USA Today that his network had
selected five contenders who might win the money: Wisconsin’s governor, Scott
Walker; Florida’s former governor Jeb Bush; and three US senators: the libertarianleaning Rand Paul and conservatives Ted Cruz and Marco Rubio.
Koch had carefully set up the game table. Then Trump came along and flipped it
over. Over several months, Trump forced every candidate backed by Charles Koch
out of the race. To everyone’s surprise, Donald Trump became the frontrunner.
Rather than back a losing candidate, or risk failure if he confronted Trump directly,
Koch retreated to the margins of political attention. On November 8, 2016, Donald
Trump won the presidential election. His victory rested on Hillary Clinton’s collapse
in a group of heavily unionized states that Democrats referred to as the “Blue Wall”:
Michigan, Wisconsin, and Pennsylvania.
In many ways, Donald Trump posed a greater political threat to Charles Koch’s
political agenda than Barack Obama. Trump was not seeking to fight American
conservatism as much as he sought to transform it from the inside. Charles Koch
tried to bend the Republican party toward a libertarian view; now Donald Trump
was bending it toward a nationalist, populist philosophy that Charles Koch found
abhorrent. Trump’s policies aimed to benefit specific populations of Americans,
rather than to solely limit government interventions in the marketplace.
Shortly after Trump’s election, congressional Republicans scurried to reorient
themselves around Trumpism. Many Congress members knew that Trump won
their home districts with more votes than they had. They were not about to oppose
him. If Donald Trump was president for eight years, it would almost certainly abolish
Charles Koch’s political project. The Republican Party would be the party of
Trump, not Hayek or von Mises. Koch Industries’ retreat from the 2016 election
cycle had been well publicized, and members of the Trump administration were
quick to point out that the Koch network’s political influence was diminishing,
almost certainly for good.
Charles Koch took a different point of view. He was conditioned to thrive in
volatile environments. He thought about the long term, and tended to avoid the wall
of noise and media controversy that emanated from the White House each day.
Charles Koch worked on a longer political horizon and that gave him an advantage.
He had spent more than forty years building a densely connected network of political
operatives and institutions in the nation’s capital. Donald Trump had not.
When Trump arrived in Washington, Charles Koch was ready.
I. Appending an R, for registered trademark, to MBM seems to be the preferred style for Koch Industries
executives. Charles Koch used the abbreviation in his own writing,and it also appeared in internal memos.
II. The “tail” of a paper roll is the last section of paper that flaps loose, like the outside tab of paper on a toilet
paper roll.
CHAPTER 24
Burning
(2017–2018)
Springtime came early to the nation’s capital in 2017. In early February, the air was
unseasonably warm and the trees were starting to get their buds. Brightly colored
flowers bloomed in Lafayette Square park, just north of the White House, with early
tulips pushing up from their beds and cherry trees frosting themselves with pink and
white blossoms. In the suburbs, the forsythia exploded in vibrant yellow flowers and
the redbud trees were covered in purple. The riotous colors of spring, usually
celebrated in the capital city, were out of place and disquieting, like flashing signals
on a dashboard. Across the country, springtime arrived weeks early, with the zone of
blooming advancing farther north than usual. The election year of 2016 was the
hottest year on Earth since reliable record keeping began around 1880. NASA
compared Earth’s average surface temperatures against a period in the mid-1990s, and
found the average temperature rose steadily each year. Sixteen of the seventeen
warmest years on record occurred after 2001, peaking in 2016. Eight of twelve
months in 2016 broke records as the hottest months ever recorded. Scientists at
NASA did not dispute what caused the warming. It was “a change driven largely by
increased carbon dioxide and other human-made emissions into the atmosphere,” the
agency said. In the winter of 2017, carbon concentrations in the atmosphere reached
407 parts per million, far past the limit where most scientists considered radical
climate change unavoidable.
The political seasons in Washington, DC, were being disrupted as well. On
January 20 Donald J. Trump stood on the grand dais in the shadow of the Capitol
dome, put his hand on the Bible, and took the president’s oath. No candidate in US
history had risen to the White House like the real estate mogul had done. He was
backed by no party, supported by no discernable outside interests, and had no
previous experience in government or military service. The usually stable networks of
political influence were torn apart in 2017. No one knew who was in or out of
Trump’s political circle. No one knew what he really wanted—what was hyperbole
and what was an actual campaign platform. The lobbyists at Koch Companies Public
Sector and other companies had adapted to political shocks before, but this time was
different. The Trump administration saw itself as a revolutionary force, independent
of both political parties. One person close to the administration, and who also had
been close to the Koch’s political operations, said that the Trump administration
viewed Washington, DC, as a chessboard on which three opponents were doing
battle. One opponent (and the weakest) was the Democratic establishment: “Team
D.” Another was the Republican establishment: “Team R.” Finally, there was the
Trump administration, “Team T,” which planned to beat everyone else.
When Trump delivered his inaugural address, he made it clear that he was
upending the political order. His voice was booming and severe.
“Today we are not merely transferring power from one administration to another,
or from one party to another—but we are transferring power from Washington, DC,
and giving it back to you, the American people,” Trump said. His vision was nearapocalyptic, and he talked about “American carnage” that only his administration
could stop. He managed to offend and alienate virtually every politician and former
president sitting in the gallery behind him.
“For too long, a small group in our nation’s capital has reaped the rewards of
government while the people have borne the cost,” he said. “Washington flourished
—but the people did not share in its wealth. Politicians prospered—but the jobs left,
and the factories closed. The establishment protected itself, but not the citizens of
our country.”
Charles Koch was considered part of this establishment. And everything Trump
stood for was a threat to Charles Koch’s entire political project. Donald Trump’s
presidency had the potential to destroy everything Charles Koch had built. Charles
Koch’s political blueprints called for the federal government to retreat from virtually
any intervention in the marketplace. But if Donald Trump had an underlying
political philosophy, it was that the tools of government should be used aggressively
to steer economic activity toward the benefit of the people who voted for him.
Trump promised to tear up trade deals and impose tariffs to protect the white,
working-class, and affluent voters who put him in office. Trump spoke in favor of
punitive taxation on companies that thwarted this vision, and spoke favorably of
entitlement programs that were funded by taxes on the rich. Alarmingly, Trump also
lashed out in personal ways, at business leaders who antagonized him, using Twitter
as his weapon of choice. Trump singled out as targets Jeff Bezos, CEO of Amazon,
and the Carrier air-conditioning company, claiming that their economic decisions
harmed America. It was clear that this same vindictive power could be used against
Charles Koch. Based on Trump’s campaign rhetoric, it seemed entirely plausible that
Trump would be willing to squeeze Koch Industries with all the available levers of
government power, from the IRS to the EPA to the simple use of the White House
Twitter account.
Charles Koch responded to this threat with a strategy that bore his hallmarks:
patience, persistence, and a reliance on his competitive advantages. To counter
Trumpism, the Koch political machine employed a strategy that could be called
“block-and-tackle.” Charles Koch would “block” Trump when Trump deviated from
Koch’s wishes—when he imposed tariffs, raised taxes, or supported entitlement
programs, for example. But Koch Industries would help Trump “tackle” the things
that Charles Koch wanted to see demolished, helping the Trump administration
when they did such things as dismantle regulatory agencies, cut taxes, or nominate
economically conservative judges to the federal bench and the Supreme Court.
For this strategy to work, however, Charles Koch needed to prove that his political
machine was still relevant and still powerful within Donald Trump’s Washington. As
luck would have it, Koch got the opportunity to do this very early in Trump’s tenure,
just two months into the life of the Trump administration.
In March of 2017, Donald Trump had no choice but to venture into territory
where Koch Industries had the upper hand. It was time for Trump to turn his
campaign promises into reality and to show that he really was the deal maker who
could solve Washington’s dysfunction. This appeared entirely feasible—Republicans
controlled the House, the Senate, and the White House. There was nothing standing
in the way of Trump’s agenda. But to pass the agenda, Trump had no choice but to
work through Congress. He had to engage in the complicated, maddening process of
writing and passing laws. This is the terrain where Koch Industries was waiting for
him.
The first fight was to repeal Obamacare. Republicans had been trying to do this for
more than six years and now they had their chance. This seemed like the ideal project
for Charles Koch to support. Obamacare, just as Charles Koch had feared, had
become a massive government program that redistributed wealth from the very rich
to the working class and the poor. The government estimated that Obamacare raised
the tax bill of the top 1 percent of American earners by about $21,000, steering about
$16 billion from the richest Americans to the poorest, largely in the form of health
insurance subsidies.
Throughout his campaign, Trump promised to both repeal the hypercomplex law
and replace it with something else. And this is where the problem lay. In Charles
Koch’s eyes, Donald Trump did not seem sufficiently dedicated to the job of tearing
this system out, root and branch, and replacing it with nothing. Trump seemed open
to compromise.
Trump made statements along these lines that were particularly worrisome to
libertarians, showing that his allegiance to free markets was questionable. After taking
office, Trump made promises that were too large to fill without significant
government intervention, promises more grandiose than even Barack Obama would
have dared to make.
“We’re going to have insurance for everybody,” Trump told the Washington Post
during an interview in January. “There was a philosophy in some circles that if you
can’t pay for it, you don’t get it. That’s not going to happen with us.”
While potentially offensive to Charles Koch, Trump’s statements were firmly
grounded in political reality. Millions of people depended on Obamacare. The
Congressional Budget Committee estimated that even a limited repeal of the law
would take health insurance away from fourteen million people the first year, and
twenty-four million more people the following decade. Trump and other
Republicans sought to avoid such a political calamity. They planned to seek a middle
ground that would retain some benefits and subsidies for the working class and the
poor.
There was another reason for Trump to compromise. It would help the
Obamacare repeal effort move quickly. Trump wanted to achieve a legislative storm
of greatness during his first hundred days in office that would rival FDR’s. He would
repeal Obamacare, then pass tax reform, then pass an infrastructure bill, then pass an
immigration law that included construction of a wall along the border with Mexico.
With these accomplishments behind him, Trump would emerge as the most effective
president of modern times.
Charles Koch helped ensure that this agenda was derailed. The Koch political
network would attack the effort to repeal Obamacare, and in doing so it would win a
second victory by proving its power and ensuring a place at the bargaining table for
Charles Koch.
On March 6, the House of Representatives unveiled a plan to repeal and replace
Obamacare with a bill called the American Health Care Act. The next day,
Americans for Prosperity mobilized against the plan, just as it had mobilized against
Obama. Large tour buses, chartered and paid for by Americans for Prosperity, arrived
in Washington, DC, on March 7, unloading hundreds of passengers at an
intersection near Union Station, within view of the Capitol dome. The crowd looked
like tourists at Disney World. Most of them were older, congenial, and clearly
enjoying the free trip to the nation’s capital. They were directed down the sidewalk
by helpful employees in AFP windbreakers, who led them into the quiet, marble-tiled
lobby of an upscale office building. The volunteers were ushered into elevators and
sent to the building’s rooftop, where they walked into a lavish event space, covered by
a party tent, with a beautiful view of the city. As they entered, the volunteers were
given glossy placards with a sleek logo for the day’s event, reading “You Promised.”
The message of the day was that these voters had been let down by Congress
members who were balking on their years-long promise to repeal the health care law.
The attendees sat in rows of chairs, in front of a stage that was bordered by largescreen televisions. The crowd was shown video testimonials, made by AFP, from
everyday people who were purported victims of the ravages of Obamacare. The
victim-impact statements were somewhat incoherent, from a policy standpoint. Most
of their complaints were that health care was too expensive, or only available
intermittently, problems that other industrialized nations had solved by nationalizing
the health care industry. But the overall tenor was consistent—Obamacare was a
terrible burden, and Congress wasn’t doing enough to repeal it.
After the presentation, the crowd was led out onto a terrace in the delightful
spring weather and given free boxed lunches. They milled around and talked, and
were later led to Capitol Hill where they met with congressional staffers and
representatives to share their demands. The popular revolt against the American
Health Care Act had begun.
Inside the US House of Representatives, resistance to Trump’s plan was led by the
House Freedom Caucus, the group of lawmakers most aligned with Charles Koch’s
worldview. Koch Industries was the second-largest contributor to Freedom Caucus
members, according to Politico, ranking only behind the Club for Growth (which
was partially funded by Koch’s political network). The caucus declared that the
American Health Care Act was an unacceptable compromise of conservative
principles.
Mark Meadows, the North Carolina congressman who chaired the Freedom
Caucus, led an effort. On the day the bill was introduced, Meadows published an
editorial on the Fox News website, declaring his principled opposition to it. “We call
on congressional leaders to keep their word to the American people, to push a real
repeal of Obamacare, and to do it now,” Meadows wrote. The sin of the AHCA, as it
was called, was the inclusion of tax breaks that would help millions of people pay for
health insurance—“families will be given up to $14,000 of other people’s money,”
Meadows complained. He pointed out that the bill also forced insurance companies
to fine their customers if they dropped their health insurance, a sneaky way to
perpetuate Obamacare’s mandate to purchase insurance. The bill also included
subsidies to insurance companies approaching $100 billion, Meadows said. It was one
thing for the Freedom Caucus to obstruct the Obama agenda. Now the caucus was
obstructing its own party, its own president, and the bigger Republican agenda.
Weeks dragged on, and Donald Trump began to look just as ineffective as Barack
Obama had been. He couldn’t move the Freedom Caucus. The obstructionists in
Congress knew that time was on their side; the longer the bill was delayed, the weaker
Trump’s hand became. A left-wing resistance movement emerged, modeled on the
Tea Party, that confronted Congress members at town hall meetings in school
gymnasiums and auditoriums. New studies emerged showing the deep damage the
bill might do by kicking millions off their insurance. With each day, the bill became
harder to pass.
The halting effort to pass it was carried forward by Paul Ryan, the Wisconsin
Congressman who was the Speaker of the House. Ryan conducted his duties with the
enthusiasm of a funeral director, impeccably dressed, unmovably calm, but with a
deeply morose look in his eyes. He gave reasoned speeches and laid out the necessity
of passing the AHCA quickly out of the House. He couldn’t move the Freedom
Caucus.
The crisis came to a head during the week of March 20. Ryan wanted to put the
bill to a vote in the House. It wasn’t clear that the bill had enough votes to pass, but it
seemed imperative to move it to the Senate before time dragged on much longer.
Donald Trump made bold gestures to support the bill. He traveled to Capitol Hill
and cajoled lawmakers. He said that they needed a win at all costs and needed to
prove they could govern. Trump singled out Meadows in person and threatened to
bring down the weight of the White House upon him if he wouldn’t bend. “I’m
going to come after you,” Trump warned Meadows with a smile, according to media
reports of the closed-door meeting.
Nevertheless, Meadows persisted. That week, Trump gave the group an
ultimatum—either they passed the health care bill, or he would abandon the effort
altogether and lay the blame at their feet.
This is when Charles and David Koch stepped in, to fortify the caucus. They did
so in a way that was unprecedented. For forty years, Charles Koch prized his
discretion in politics, funding candidates and lobbying groups through obscure
cutout organizations with names like 60 Plus Association, Corner Table LLC, and
PRDIST LLC. But on March 22, Charles and David Koch went public with their
desire to change a legislative outcome. Americans for Prosperity and Freedom
Partners (a clearinghouse organization for many of Koch’s donations) announced
that they would support any member of Congress who voted against the health care
bill. If the Freedom Caucus stood up against Trump, the Koch network would be
there to protect them afterward. The two organizations announced they were
compiling a “seven-figure reserve fund” that obstructionist Congress members could
draw on if they voted no. “Republicans have been promising to fully repeal
Obamacare since it became law. This bill doesn’t do that,” James Davis, the executive
vice president of Freedom Partners, told Politico when the fund was announced.
This tactic carried risks. When the US Supreme Court handed down its decision
in Citizens United, the court emphasized that it was still illegal to engage in quid pro
quo corruption, meaning the explicit trade of money for a vote. If the announcement
from Freedom Partners and Americans for Prosperity was not a promise of money
for a specific vote, then it is unclear what it was. Regardless of the risks, the Koch’s
support stiffened the spines of the Freedom Caucus members. In a private meeting
with Donald Trump at the White House, the members said they still were not ready
to support the bill. On Friday, March 24, Paul Ryan admitted defeat. He pulled the
bill and cemented Donald Trump’s failure.
The bill showed passing signs of life over the summer as it was revived and
changed in a minor way that ultimately won the support of Meadows and his
caucus.
I When the bill passed the House, Donald Trump hosted a televised
celebration of the victory, alongside a smiling Paul Ryan and other House leaders.
But the bill would meet a similar destiny as the cap-and-trade bill in 2010. It was sent
to the Senate, where it languished. Eventually the bill was forced to a vote, even
though support was weak and the leadership could only hope to pass it by the
narrowest of margins. The bill was defeated by the Arizona Senator John McCain,
who voted no.
Donald Trump had been hobbled in the Congress. And once he was hobbled, the
Koch network pressed its advantage. The fight over health care had been a proxy war,
a way for the Koch network to prove its strength. The real fight was still looming.
After he abandoned the Obamacare repeal, Donald Trump moved on to
reforming the nation’s tax code. Trump had specific ideas about the ways to do this,
and many of them ran counter to Charles Koch’s interests. The Koch network was
ready for the fight. Once again, Americans for Prosperity chartered buses and paid for
volunteers to travel to Washington, this time to protest against Donald Trump’s tax
plan.
The Republican party had a once-in-a-generation chance to rewrite the American tax
code. It controlled all three branches of government, giving it the freedom to write a
tax bill that was true to Republican orthodoxy and untainted by the Democratic
impulse to raise taxes and support the social safety net programs.
Orchestrating the task fell to Paul Ryan. He made the mistake of helping write a
bill that reflected Republican orthodoxy, but ran counter to the interests of Charles
Koch.
Paul Ryan’s mistake was caused by seemingly good intentions. He partnered with
the Texas Republican Kevin Brady, head of the powerful House Ways and Means
Committee. They wrote a bill that would dramatically cut income taxes for US
corporations and middle-class families, while also remaining “revenue neutral,”
meaning that it would not increase the national debt. This might have seemed
eminently practical because lowering the debt had been the campaign platform of
Republicans for at least seven years. But the approach was fundamentally flawed in
Charles Koch’s eyes.
This flaw arose because Paul Ryan was trying to do three things at once: avoid
adding to the US deficit, cut corporate tax rates, and meet the desires of Republican
voters who elected Donald Trump. Ryan thought he could meet all of these needs by
using an obscure tax provision called the Border Adjustment Tax (technically it was a
border adjustment to the federal income tax, but it became widely known as the
Border Adjustment Tax, or BAT), which became a vital pillar of Ryan’s tax plan. The
BAT is what drew the Koch network’s opposition.
It is easy to see why Paul Ryan would have been seduced by the logic of the BAT.
A similar adjustment was already in place in more than 140 countries and wasn’t
exotic or particularly controversial.
II There was strong evidence that the BAT would
accomplish one of Donald Trump’s most important campaign platforms—boosting
economic growth inside US borders and discouraging companies from shifting their
factories overseas. Creating a BAT would also help raise money to offset the massive
cuts in corporate income tax that Ryan proposed, taking the rate from 35 percent
down to 20 percent. If the corporate tax rate was cut with no other changes, it would
dramatically increase the deficit. The BAT provided an elegant solution. It would
allow the government to raise money—roughly $1 trillion over a decade—that could
shore up the budget.
The BAT would do this by making a seemingly subtle shift to the US corporate
income tax system that had tremendously large effects. Under the current tax code in
2017, US companies were taxed based on the profits they earned from things that
they produced in the United States. Under the BAT, companies would be taxed on
profits from the things they sold in the United States. This difference, although it
seemed obscure, would upend the economic logic that enticed companies to send
their factories to Mexico and China. In essence, the BAT was a big tax break for
exporters.
III Under the BAT, exporters who made things in the United States and
sold them overseas would not be taxed on income from the sale. Conversely, if a
company produced goods in China and sold them in the United States, the company
would pay a 20 percent tax on the profit.
The end result of this tax shift was decidedly Trumpian. Most experts predicted
that the BAT would encourage companies to locate their factories in the United
States and make things to sell overseas. The change wouldn’t be dramatic, but it
would move the country closer to Donald Trump’s vision of “America First.” The
existing US tax code of 2017 did the opposite—it encouraged companies to move
their production to low-cost countries like China (because the United States didn’t
tax profits from overseas production) and sell them in the United States. For this
reason, Ryan began to call the existing tax code the “Made in America Tax.” He
bolstered his case for the BAT with poll numbers—the new surge of Trump voters
supported the idea of a BAT overwhelmingly. They wanted to do anything they
could to bring factories back to Wisconsin and Michigan.
Charles Koch opposed the BAT for two reasons. The first was ideological—the
BAT would impose a new tax, and Koch’s network opposed all new taxes. The
second reason was more central to Koch Industries’ business. The BAT posed a grave
threat to the company’s profits. In December of 2016, before Donald Trump was
inaugurated, Koch’s lobbying office funded a study by a consulting firm called the
Brattle Group. Unlike other groups that published Koch-funded studies, the Brattle
Group clearly acknowledged Koch’s support in the beginning of the report. Kevin
Neels, a coauthor of the study, said that Koch initially insisted that its support remain
secret. But hiding Koch’s financing would have violated the Brattle Group’s policies,
so Koch eventually agreed to let Brattle disclose it.
The study showed why Koch might have deep concerns with the BAT. The tax
could carry a high cost for energy companies that imported crude oil or other fuels
from overseas. The Brattle Group report claimed that the BAT, by imposing a 20
percent tax on imported oil sold inside the United States, would raise gasoline prices
by about 13 percent, or roughly 30 cents per gallon. This could be a nightmare for oil
refineries that imported crude and sold it domestically. The damage could potentially
be twofold and severe. First, it might cut into the refineries’ profit margins. Second,
and most dangerous, the tax might dampen demand for gasoline by raising prices. If
that happened, it would stoke demand for alternative energy sources, compounding
the long-term problem of peak demand for gas.
Koch Industries would later insist that it opposed the BAT only for purely
ideological reasons. The company argued that it would have actually benefited if the
border adjustment was imposed because the tax would raise consumer prices for
gasoline and other products Koch sold. But the effect of a BAT on Koch’s business
would be complicated. There was strong evidence that the tax could pose a threat to
Koch Industries’ oil refinery in Pine Bend, which was still considered to be the
company’s “crown jewel.” After decades, Pine Bend still benefited from occupying a
stunningly profitable bottleneck in the US energy system. Cheap oil from Canada’s
tar sands piled up at the US border without many buyers except Koch, and Koch
could still sell its refined gasoline into midwestern markets where prices were
relatively high thanks to a lack of refining capacity. Pine Bend was largely depending
on imports, and the BAT would make those imports more expensive.
In the month of February of 2017 alone, Koch Industries bought 9.55 million
barrels of Canadian crude oil at Pine Bend. The average price at that time was $39.41
a barrel. If the BAT was imposed, the government would be entitled to $75.3 million
in new taxes on products Koch made from that oil, for just one month of production.
More importantly, the new tax might wipe out some of the price advantage that
Koch had long realized by purchasing Canadian crude. Once the BAT was imposed
at 20 percent, the cost of Canadian crude would be $47.29. That was still an
advantage over the cost of a barrel under the WTI
IV contract in Texas (which was
$53.47), but far less of an advantage than before. And this change would be
permanent. The crown jewel might be tarnished, and long-term sales would be hurt
by the higher cost of gasoline.
Koch’s public relations team claimed that the Pine Bend refinery could actually
benefit from the BAT, because the tax would raise gasoline prices. It was difficult to
disprove this hypothetical argument, but three former Koch commodities traders said
that it was almost inconceivable that a BAT would benefit Pine Bend. One oil trader,
intimately familiar with the economics of Pine Bend, said there was “no scenario”
under which the refinery would benefit from a border tax. Another pointed out that
any 20 percent increase in the cost of inputs could hurt a refining operation, even if
gasoline prices rose. Regardless of the hypothetical scenarios from which the Pine
Bend refinery might benefit, there was no doubt that a BAT could be disruptive to
Koch’s refinery business.
The Koch political network moved against this threat hard and early. The network
launched its attack on the BAT in December and January, before Trump’s
inauguration and before the public, or even most Congress members, started
thinking about the measure. The goal seemed clear: to kill the BAT in the crib, before
a public debate could even begin.
The attack was well fashioned by Koch’s political team. After the Brattle Group
report was released in December, Koch Industries did not talk in detail about the
harm that the BAT posed to its oil business. Instead, the company’s political proxy
groups framed the issue with different arguments. Americans for Prosperity started
talking about the US tax code in terms of “crony capitalism” and a “rigged economy.”
The group presented BAT as an odious corporate giveaway. Corporations were
getting a tax cut, the group said, because the corporate tax rate would fall from 35
percent to 20 percent. But consumers would pick up the bill because prices for
imported goods—like toys, gasoline, and electronics—would rise. This was a
mischaracterization of what the BAT would do. More than a hundred countries had
imposed the BAT (or a similar tax) and data showed that the tax caused consumer
prices to rise, but only temporarily. The reasons for this were complicated, but they
derived from the fact that a BAT strengthened the value of the home country’s
currency. The incentive for domestic manufacturing would add to this effect,
creating jobs and raising wages. The real entities that were harmed by a BAT were
companies that sought to shift jobs overseas, and also the richest Americans who
owned stocks in such companies. A Tax Foundation report estimated that the
financial burden of the BAT would fall primarily on the richest 1 percent of
Americans.
In the winter months of January and February, while most public attention was
focused on the fight over Obamacare, Americans for Prosperity fully mobilized to
defeat the BAT. In May, the group launched a high-profile campaign called “Un-Rig
the Economy,” which made defeating the BAT a centerpiece of its efforts. AFP
released a statement saying that “72 percent of Americans feel that our ‘economy is
rigged to advantage the rich and powerful.’ And the biggest contributor to our
country’s rigged economy is the US tax code.”
In fighting the BAT, Koch Industries seemed out of step with Republican voters.
Koch had successfully grafted the fight against a cap-and-trade bill to the Tea Party
movement, but it was more difficult to graft opposition to the BAT to a conservative
movement that had just voted for an America First president. The Freedom Caucus,
which was Koch’s strongestally in Congress, was slow to pick up Koch’s cause. When
the caucus met privately in January to discuss the BAT, the group was split. Some
members supported the notion of cutting tax rates and shifting jobs back onshore.
After the closed-door meeting, Mark Meadows sounded open to the idea of
supporting the BAT, even if he had some reservations. “The border adjustment thing
is at twenty percent, so that would make sense,” Meadows told CQ Roll Call.
The weekend after Meadows made his comments, Americans for Prosperity sent a
letter to Kevin Brady, chair of the Ways and Means Committee, making AFP’s
opposition to the BAT clear, claiming that the BAT would hurt low-income
Americans by making imports more expensive. That weekend, AFP’s president, Tim
Phillips, gave a stirring speech at a donor conference in California, saying that the
group would pour its resources into defeating the BAT because it was unprincipled.
Within weeks, Meadows changed his view of the BAT. He began to say that he
wouldn’t support it. But his opposition was still tepid. “Let’s go ahead and pass [a tax
bill] without border adjustment, assuming that we can lower corporate [taxes] to
twenty percent, flatten the rate out for individuals,” Meadows told the media outlet
Axios.
Paul Ryan was unbending. He stubbornly insisted that the BAT was a necessary
part of tax reform, even though his support meant that he was now fighting one of
the Republican Party’s largest donor groups. “I obviously think border adjustment is
the smart way to go,” Ryan said during a news conference in May. “I think it makes
the tax code the most internationally competitive of any other version we’re looking
at. And I think it removes all tax incentives for a firm to move . . . their production
overseas.”
Americans for Prosperity brought its volunteers and employees to Washington,
DC, to lobby against the BAT. They met with lawmakers from Ohio, North
Carolina, Florida, and Virginia. The group ran ads attacking the BAT. “It’s safe to say
it’s been a seven-figure effort in total, so far,” Tim Phillips told Congressional
Quarterly.
If Ryan was fighting for the BAT, it was in part because of the issue of deficits. He
had campaigned, for years, on the promise of reducing deficits. Now the Koch
network was pushing Ryan to advocate a tax plan that would make the debt balloon.
This was not hypocritical on the part of Koch’s network. It revealed, in fact, the
network’s long-term goals and values. It revealed Charles Koch’s real thinking about
government financing and the role that tax cuts should play.
This thinking was reflected in the political strategy articulated in 1977 by Murray
Rothbard, Charles Koch’s partner in funding the libertarian Cato Institute.
In a confidential memo entitled “Toward a Strategy for Libertarian Social
Change,” Rothbard said that the goal of cutting taxes was not to just stimulate
economic growth. The goal was to fight oppression in the form of state-sanctioned
robbery. Libertarians, Rothbard wrote, should not be concerned about creating
budget deficits by cutting taxes. The deficits weakened “the enemy,” as Rothbard
referred to the state, and strengthened the libertarian’s power to demand that the
state reduce its spending and shrink its role in society. Deficits and debt were useful,
in other words, because they weakened the state.
Both Republicans and Democrats squabbled about the level of taxation,
Rothbard wrote. He continued:
The libertarian, in contrast, should always and everywhere support a tax cut as
a reduction in State robbery. Then, when the budget is discussed, the
libertarian should also support a reduction in government expenditures to
eliminate a deficit. The point is that the State must be opposed and whittled
down in every respect and at every point: e.g., in cutting taxes, or in cutting
government expenditures. To advocate for raising taxes or to oppose cutting
them in order to balance the budget is to oppose and undercut the libertarian
goal.
If Paul Ryan felt that Koch’s political network turned a deaf ear to his pleas for fiscal
responsibility in the form of a Border Adjustment Tax, he was correct. The effect of
the Koch network’s efforts was not to balance the budget but to attack the state itself.
As Americans for Prosperity was pressing its case publicly, the group was holding
private meetings with the Trump administration to help shape the tax bill. One of the
most important points of contact between the Koch network and the White House
was a forty-seven-year-old official named Marc Short. He had a long history with
Koch and a close working relationship with AFP president Tim Phillips. Short joined
the Koch network in 2011, where he helped fund Freedom Partners, a nonprofit
institution that acted like a clearinghouse for Koch’s donor network. Freedom
Partners collected donations and disbursed them to Koch-funded groups. Few people
knew the inner workings of the Koch political network better than Short.
Short was the White House director of legislative affairs, the key liaison between
Trump and Capitol Hill. He saw firsthand how Americans for Prosperity hindered
the Obamacare repeal. He said the administration had learned its lesson by the time
the tax bill came around—Short would bring aboard third-party groups like AFP
early. He met several times with Tim Phillips in the Executive Office Building, next
door to the White House.
Short had worked closely with Phillips over the years. They had a warm rapport.
During their meetings, Phillips said that AFP had a handful of key goals with the tax
plan. One was to remove the BAT. The other was to remove the slew of personal
deductions that had been written into the tax code over decades, allowing people to
get tax breaks for their children, home offices, and other expenses. These deductions
were the closest thing that middle-class families had to a shell company in the
Cayman Islands. They were a key way to reduce the tax burden, and many families
depended on them to claim tax returns. The tax code needed to be simplified, Phillips
said.
Short took Phillips’s concern back to the White House. Trump was willing to
abandon the BAT, even though it was in line with his “America First” doctrine, Short
recalled. Trump felt the BAT was too complicated to explain. He didn’t feel like he
could rally political support for the measure. He was also willing to sign a bill that
removed deductions.
Tim Phillips was invited with a handful of other conservative movement leaders to
a meeting with Trump in the White House. The tone was friendly. When Trump
saw Phillips, he quipped, “You’re the Koch guy, right?” Short recalled. Phillips said
that AFP was happy with the tax bill. Trump could count on the AFP foot soldiers to
get outand support it. It was understood that the BAT was gone.
On July 27, Paul Ryan and Kevin Brady released a statement saying that the BAT
proposal was dead and would not be included in the Republican tax reform bill.
Koch had won the fight over the BAT before the public fight began.
Now, with the BAT off the table, the Koch network deployed the second half of
its block-and-tackle strategy. After it had blocked the Trumpian Border Adjustment
Tax, the political network would help Congress, and President Trump, tackle any
opposition to passing a tax cut bill that conformed more closely to Charles Koch’s
vision.
On July 31, AFP released a statement crowing about its achievement: “AFP’s
Defeat of the Border Adjustment Tax Clears the Way for Principled Tax Reform.”
Other interest groups had fought the bill, led by retailers such as Walmart and Best
Buy that relied on imports for their sales. But none of the groups, and none of the
companies, had a political network that could rival Charles Koch’s. None had armies
of volunteers, or a network of wealthy donors who could fund attack ads.
On August 8, Americans for Prosperity rented out a large event space in the
Newseum, on Pennsylvania Avenue in downtown Washington, DC. The group
brought its charter buses from small towns throughout Virginia. Volunteers arrived
from North Carolina and Ohio. They filed into a conference room and were handed
glossy placards demanding that lawmakers “unrig the economy” by passing tax cuts.
Mark Meadows was the keynote speaker. If he was tepid in his opposition to the
BAT before, he was ferventabout it now.
“There are some who have said: ‘Well, you know, those special interest groups,
they want that border adjustment tax,’” Meadows said. “Well, I can tell you that
Americans for Prosperity were leading the charge, many times, to say: ‘What this is
going to be is a new tax on the American people.’ When we talk about revenue
neutral, what that means is that we’re going to cut your taxes in one place and we’re
going to add them someplace else. There is no benefit from that.”
Meadows encouraged the crowd to get out and fight for the new tax cut plan that
was working its way through Congress. He warned them that speed was now of the
essence—the bill had to be passed before opposition could build. Meadows, who had
led the charge to obstruct Trump’s agenda, said the time for obstruction was over.
“We’ve got a president in the White House who is not going to take any excuse.
He’s saying that we’ve got to get this done. We’ve got to deliver. And quite frankly,
it’s members in the Senate and the House that have kept him from accomplishing his
agendaalready!” he said.
Meadows framed the debate over tax reform in populist terms. He rallied the
volunteers by assuring them that if they helped pass the tax cut bill, they’d be helping
reduce corruption in Washington.
“For far too long, it’s been the well connected or the people that are well paid that
actually get the biggest benefit in terms of our tax code,” he said. “That is going to
change this year, when we actually start giving you back the money that you earned.”
The tax bill passed Congress in December, and was signed into law before Christmas.
The most significant portion of the bill was an income tax cut for corporations,
permanently reducing their tax rate from 35 percent to 21 percent, a cut that
amounted to roughly $1 trillion over a decade. The bill also cut the income tax rate
for the richest Americans from 39.6 percent to 37 percent.
Without a border adjustment, the tax cut for corporations increased the federal
deficit, making it difficult to pass the bill through the Senate. The reasons for this
were complicated. The Republicans planned to use a process called “budget
reconciliation,” which required only a bare majority vote. This allowed them to avoid
a filibuster. But a bill passed through reconciliation could only add so much money
to the deficit, and, without the BAT, the current tax cut plan added far too much. To
accommodate for this fact, the Republicans came up with a simple maneuver. They
made the tax cuts for middle-class families temporary. Those cuts would begin to
expire in 2022 and be fully repealed by 2027, leaving many families with a tax
increase. The middle class had been given a smaller tax cut, for a few years, in order to
make the math work.
In the end, the bill looked very much like the typical tax bill that Mark Meadows
described at the Americans for Prosperity event in August. It primarily benefited the
highest earners and the best connected. The richest 20 percent of Americans got 65.3
percent of the value of the tax cuts. Middle-income Americans got zero benefit from
the tax cuts after their temporary cuts expired.
Starting in 2027, the biggest tax breaks under the plan would go to the richest 5
percent of Americans, while taxes would slightly increase for the poorest Americans,
according to an analysis of the cuts by the Tax Policy Center. Using a number of
assumptions about the profit margins at Koch Industries, a liberal policy group called
Americans for Tax Fairness estimated that the tax cuts would save David and Charles
Koch more than $1 billion annually in taxes.
By the summer of 2017, Koch’s block-and-tackle strategy was paying dividends.
Koch had proved its power in the Obamacare fight, and had reshaped the tax reform
legislation from a Trumpian bill to a Koch bill. With these victories in hand, the
Koch network could turn to a more helpful role. As it turned out, the Trump
administration and the Koch network shared one important goal. Both groups
wanted to ensure that greenhouse gases were not regulated in any way, and that the
fossil fuel industry would retain its predominant role in America’s energy system.
Koch Industries had a knack for positioning itself to exploit good luck, and Donald
Trump’s election proved extraordinarily lucky in this regard. Trump waged a war on
climate change regulation across the federal government, from the US Department of
Agriculture to NASA and the Pentagon. Koch Industries was on hand to assist the
effort.
Ground zero for the fight happened to be the headquarters of an agency that had
antagonized Koch Industries for decades—the EPA.
When the Trump administration’s transition team arrived at EPA headquarters, the
transition officials described their effort in military terms. After the election, Trump
sent a self-described “landing team” of transition officials to the EPA. They were
followed by a “beachhead team” of twelve officials who would assume control of the
agency. The officials in the beachhead team were designated as “Wave 1,” suggesting
that backup forces might be arriving behind them.
Before the invasion, however, there had been silence. The career employees of the
EPA expected a team of Trump officials to arrive the day after the election, which
was standard procedure. But no one arrived. On the second day, no one arrived. At
the end of the first week, no one had shown up. And it wasn’t at all clear who would
be arriving or when. The EPA career staffers, like soldiers on an empty beach, waited
in silence for the landing team.
Then, on November 22, the Tuesday before Thanksgiving, the first member of
the Trump transition team arrived at EPA headquarters in downtown Washington,
DC. He was an older man with graying hair, congenial and talkative. His name was
Myron Ebell, and much of his adult life seemed aimed squarely at destroying the
EPA.
Ebell was a senior scholar with a DC think tank called the Competitive Enterprise
Institute, funded by Koch Industries, ExxonMobil, and other corporations. The CEI,
as it was called, was libertarian and studied the growing burden of the federal
government. The think tank put out a popular annual report, called “Ten Thousand
Commandments,” one of the few reliable sources that tracked the steady creation of
new federal rules and their costs for the private sector. Ebell earned a name for
himself as a leading intellectual opponent not just of the EPA, but of any regulations
that might constrain carbon emissions and the use of fossil fuels. He was a key voice
in Washington to cast doubt on the reality of human-created climate change and
what he called “global warming alarmism” a new religion. He said in 2012 that the
consensus around climate change was a political consensus, notascientific consensus.
By 2016, Ebell had acknowledged that human activity was causing climate change,
but he told the Climatewire news service that holding this belief didn’t mean that
climate change was “a serious problem or that the policies to address it will actually
do anything or that you are willing to pay the costs of those policies.”
Needless to say, this put Ebell directly at odds with the career staff at the EPA.
After Congress failed to pass the cap-and-trade bill in 2010, the effort to regulate
greenhouse gas emissions quietly moved into the EPA headquarters. The same team
of people who had toiled with Jonathan Phillips in the basement of the Longworth
Building—namely, Joel Beauvais, Michael Goo, and Shannon Kenny—moved
straight to the EPA to continue the effort there. The team quickly realized that the
EPA’s authority to do anything was limited. Only Congress could pass the type of
sweeping legislation that could significantly curtail carbon emissions. But this
limitation was counterbalanced by good news. The fracking boom had replaced coalfired power plants with natural gas–fired power plants, reducing America’s carbon
emissions. The economics of cheap natural gas essentially doomed coal as a major
energy source. But the EPA team, including Beauvais and Goo, took a “rear-guard
action” to ensure that coal wouldn’t make a comeback and boost carbon emissions
again. This rear-guard action took the form of an EPA rule called the Clean Power
Plan, which required states to meet targets for cutting back carbon emissions for
power plants. The rule aimed to cut emissions by about one-third by the year 2030,
compared with 2005 levels. The Clean Power Plan was only part of the EPA’s effort
to limit carbon emissions. On an upper floor of the agency’s headquarters was the
home office of the Climate Change Division, a sprawling office of cubicles where the
agency collected data on greenhouse gas emissions that were a vital tool in controlling
them.
When Myron Ebell finally arrived at the EPA, he was greeted by two senior EPA
officials who sat down with him to discuss how the Trump team might lead the EPA.
The officials were Matt Fritz and Shannon Kenny, who were tasked with helping the
transition. Ebell was an unremarkable-looking man, with the manner of a soft-spoken
college professor. He wore round-framed, deeply unstylish eyeglasses with
conservative suits and neckties. He was almost overly polite, even courtly, like an
English gentleman who would never say anything to offend. This didn’t mean that
his charm won over the EPA officials. The career officials developed a nickname for
him—“Creepy Grandpa”—that reflected both their disdain and mistrust.
It appeared, at least in the eyes of EPA officials, that the disdain ran both ways. As
the weeks wore on and Ebell interacted with more EPA employees, he remained
strenuously cordial, but they perceived that he was almost gleeful about what was to
come. “He was always very polite, but he has this sort of sadistic grin,” one employee
recalled. “He wants to be sure that you know he knows he’s fucking you over.”
When Donald Trump arrived in Washington, he had no connections and no political
network from which to draw the hundreds of people he needed to staff positions
across different government agencies. Charles Koch, by contrast, had spent forty
years building political networks in Washington. He had cultivated experts and
operatives through years of employing them at think tanks, lobbying offices, and
funded university chairs. When Donald Trump went out to hire people, he almost
necessarily hired people who were sympathetic to Charles Koch’s point of view, if not
directly beholden to Charles Koch’s largesse.
This influence was apparent in the beachhead team that arrived at the EPA. The
team wasn’t selected by Koch, but it was stacked with people who understood Koch
and sympathized with it. Myron Ebell was the most obvious connection, but not the
only one. There was also Charles Munoz, the beachhead team’s White House liaison,
who helped organize the Nevada chapter of Americans for Prosperity. There was
David Kreutzer, a senior research fellow at the Heritage Foundation, which was
funded in part by Koch Industries. There was Justin Schwab, an attorney who would
help craft EPA legal doctrine; he was previously an attorney at the firm
BakerHostetler, where one of his clients was Big River Steel, of which Koch
Industries was the majority stakeholder.
One of the most significant members of the beachhead team was David Schnare.
He was a former EPA employee of more than thirty years who had left the agency to
teach law and work for the Energy & Environment Legal Institute, which was funded
in part by the Donors Trust, a group that was funded in part by the Koch network.
Schnare was an imposing presence, both physically and personally. He had a silver
goatee and a deep voice and his sentences were honed with lawyerly precision. He also
had a deep knowledge of the EPA and the workings of power in Washington. His job
was to write a detailed plan for the Trump administration to carry out its campaign
promises at the EPA. It became clear, very quickly, that the plan was not to run the
agency in the tradition of previous administrations. Someone “in authority, said to
me: ‘You have to come up with a plan to get rid of it,’” Schnare recalled. In this case,
“it” was the entire EPA. “And I said: ‘You can’t do that. There are laws and all, you
know. [EPA] can’t just go away,’” Schnare said. His boss was not moved. “They
went: ‘Read my lips. You have to come up with a plan to get rid of it.’”
So Schnare came up with a plan to get rid of it. He estimated that the entire agency
could be cut up into component parts and its functions handed over to other
agencies or abandoned altogether. This could be completed by the sixth year of the
Trump administration. It couldn’t happen fast, but it could happen.
The beachhead team moved into the north building of the EPA headquarters, a
stately, stone office building built during the New Deal era, just south of the White
House off Pennsylvania Avenue. The building was shaped in a semicircle, embracing
astone courtyard full of picnic tables where office workers with lanyards around their
necks ate lunch while packs of sightseers walked past, many of them, in the early
winter of 2017, wearing red “Make America Great Again” baseball hats. Inside the
front door, the EPA lobby was majestic and full of echoes, like a giant bank lobby,
with marble floors and stone walls and hallways with vaulted ceilings. A large spiral
staircase, with bannisters of wrought iron emblazoned with ornate designs, led from
the lobby up to the third floor, which housed the agency’s executive offices.
David Schnare’s office was on this floor, near the administrator’s office. This was
where he worked on the detailed transition plan. Schnare’s plan was revealing in what
it emphasized. The EPA imposed burdens on American businesses both large and
small. Its many rules affected farmers, small business owners, and midsized
manufacturers, and all of them complained about regulations over dust pollution,
cleanup efforts at Superfund sites, and other matters. But the Trump team’s priority
was not attacking or changing these rules. The priority was focused, almost entirely,
on rules that were a burden for the fossil fuel industry.
A copy of Schnare’s forty-seven-page transition plan, entitled “Agency Action
Plan,” began with an overview of the agency. The next heading was “Priority Change
Initiatives.” The first priority for change read: “STOP. Obama climate agenda,
including Clear Act greenhouse gas regulations for new (NSPS) and existing (ESPS,
or the “Clean Power” Plan) coal and natural gas power plants, CAFE Standards,
Methane rules and others.” These priorities could accurately be called Koch
Industries’ top priorities. The CAFE standards, for example, referred to the federal
fuel efficiency mandates that reduced demand for gasoline. The Clean Power Plan
was the closest thing to carbon regulation that the Obama administration had been
able to achieve.
The plan then listed a timeline for change. The first item on the timeline read:
“Day One—Issue directives to comply with Executive Orders to rescind climate
change directives, including greenhouse gas emissions rules for new and existing
power plants, suspend for review (withdraw from OMB) all major final rules that
have not been published. . . .” The focus on eliminating climate change rules came
from a simple source—Donald Trump’s campaign speeches. “Myron Ebell always
said, ‘Go look at the president’s speeches and the president’s website . . . that’s the
basis for what we put together in the transition plan,” Schnare recalled.
It is difficult to pinpoint the source of Donald Trump’s driving fixation with
fighting climate change regulation. The fixation was apparent in his campaign
speeches, and then in his administration’s actions across virtually every federal
department. From the USDA to the Departments of Energy and Interior and the
EPA, a mandate was handed down to roll back climate change efforts.
One plausible explanation of Trump’s fixation was that he responded to the
political realities of the modern Republican voting base. If Trump had a genius, it
was the genius of reading a crowd and telling people what they wanted to hear, even
before they knew they wanted to hear it. He had a sensitive radar for applause lines,
and he built on the lines that worked the best. In this way, Trump’s focus on denying
the reality of climate change could be seen as an echo of Koch Industries’ years of
work to politicize the issue by casting doubt on the science and portraying carbon
emission rules as a government conspiracy against liberty. The politics that Koch
stoked in 2010 became the policies that Trump enacted in 2017.
The new EPA administrator would carry out these policies. To fill that role,
Trump selected Scott Pruitt, the attorney general of Oklahoma, where oil interests
dominated the political landscape. A number of Koch funded groups signed an open
letter to US Senators, urging that they confirm Pruitt. Pruitt won confirmation with
a vote of 52 to 46. Only one Republican senator, Susan Collins of Maine, voted
against him.V
Pruitt arrived for work in the spring of 2017. One of the first people Pruitt met
when he arrived at EPA headquarters was David Schnare. “I met him at the door,”
Schnare said. “I handed him a book, which contained all the statutes that EPA has to
implement. It’s about three, three and a half, inches thick. And I said: ‘Welcome
aboard, sir, here’s the operating manual.’”
The gift was more than a good-hearted joke. It was also a warning. Schnare knew
Pruitt’s job was to dismantle the EPA. But dismantling the agency wouldn’t be as
easy as Trump might have suggested on the campaign trail.
Almost immediately after he arrived in his new office at EPA headquarters, Scott
Pruitt apparently became convinced that a lot of people inside and outside the
building wanted to kill him.
He requested that a security guard be posted outside his office door, behind a
bulletproof desk. The desk would presumably act as a barricade if someone came in
the office shooting. Pruitt also requested a bulletproof SUV for his personal
transport, complete with bulletproof seats. He dramatically expanded the size of his
security detail, building a team that could protect him around the clock. He swept
the administrator’s office for listening devices and ordered the EPA security
department to build a soundproof booth inside his office, where he could make
phone calls outside the hearing of career EPA staffers, at a cost to taxpayers of
$43,000.
It was common for new EPA administrators to hold town hall meetings with the
career EPA staff to meet the team and lay out priorities. But Pruitt rarely interacted
with any staff members, including senior staffers. He became something of a curious
figure inside the EPA. He rarely saw the staffers, rarely talked to them, and when he
did pass employees in the hallway, the effect was sometimes off-putting. He said
hello, cheerfully, and quoted Bible scripture without solicitation or apparent
relevance to the situation. In one instance, Pruitt recited a long quote about toiling in
the fields, which left staffers wondering what he meant. Two staffers suspected the
quote was from the Old Testament, but they weren’t brushed up on their Scripture
and couldn’t confirm it. One day, word raced through the office that Pruitt was
making a rare public appearance and standing by a bank of elevators, handing longstemmed roses to women as they arrived for work, for reasons that were unclear.
While Pruitt’s personality was a puzzle, his policy stances were well known. When
he became attorney general of Oklahoma, Pruitt was extraordinarily close to the
state’s fossil fuel companies. In 2011, lawyers with Devon Energy drafted a letter
complaining to the EPA about air pollution regulations. Pruitt pasted the letter onto
an official state document with the official seal of the state’s attorney general and sent
it to the EPA. After Pruitt sent the letter, a Devon lobbyist named William F.
Whitsitt sent Pruitt an e-mail that said: “Outstanding!” Devon Energy’s involvement
in sending the letter was not made public until 2014, when it was uncovered by New
York Times reporter Eric Lipton. This was one example among many.
Pruitt’s political career had been carefully nurtured in Oklahoma’s political
culture. But when he arrived in Washington, it seemed that he wasn’t prepared for
what awaited him. He was particularly unsuited to deal with criticism. In the spring
of 2017, Pruitt attended a conference at the Mayflower Hotel in Washington, DC,
hosted by the Environmental Council of the States, or ECOS, a nonprofit group
representing state-level environmental regulators. Two protestors attended the event.
They were women, carrying baskets of oranges with stickers on them, highlighting
the use of a pesticide called chlorpyrifos. Pruitt’s administration had recently allowed
the pesticide’s continued use, even though it was shown to harm human health. The
women shouted, and were led out of the conference hall. This was standard fare in
Washington, where Senate hearings were often staffed by protestors in wait.
When he returned to EPA headquarters, however, Pruitt seemed deeply shaken by
the women with the oranges. During a meeting in his office on an unrelated topic,
Pruitt kept returning to the protestors and the threat they posed to him. He seemed
to suggest that the conference organizers were complicit in letting the protestors in
the building.
“He treated it as if he’d been shot at. He wouldn’t let it go . . . he was furious at the
conference organizers for not protecting him,” recalled one person in the room.
Pruitt often fixated on what he saw as threats to his safety, this person said. “He
becomes obsessed. I think he truly believes that he is sort of on God’s mission, and
people are out to get him.”
Pruitt’s new leadership team consisted largely of loyalists from Oklahoma. They
barricaded themselves off from the rest of the agency and held hours-long meetings
each morning without any EPA staff present. David Schnare attended those
meetings, and he became frustrated with Pruitt’s refusal to meet with EPA staff. It
was hindering Pruitt’s ability to understand the agency and to mobilize the people
who worked there.
“Let’s put it this way. He didn’t want anyone to tell him that he couldn’t do
something. He only wanted to be able to tell people to go do things and sometimes
someone has to stand up and say you can’t do that. And those people didn’t last,”
Schnare said.
There were other problems with Pruitt. Schnare began to doubt that Pruitt, for all
his close ties to energy companies, might be a reliable conduit for the effort to
thoroughly dismantle the legal basis for climate change regulation. Schnare discussed
the transition plan with Pruitt, and explained the importance of attacking climate
rules. But Pruitt seemed uninterested. Instead, Pruitt asked his staff to come up with
quick initiatives that could garner headlines and give him a chance to visit states for
public events.
“If he had an agenda, the agenda was: promote Scott Pruitt for the next job,”
Schnare said. “He looked for opportunities that gave him the chance to go out into
the states—especially Iowaand New Hampshire.”
Schnare quit the EPA that spring. Pruitt’s inner circle became tighter. The
morning meetings went long—three hours sometimes—and Pruitt’s team began
issuing policy proposals that were fully formed, without any input from the EPA’s
staff. In the course of a year, Pruitt’s team issued orders to repeal or roll back forty-six
rules and regulations. Many of these were major rules. Pruitt’s team issued a proposal
to repeal the Clean Power Plan and to strip away the CAFE standards for fuel
efficiency.
In June, Pruitt attended a ceremony at the White House Rose Garden, where he
introduced President Trump. The event was to announce America’s withdrawal
from the Paris Climate Accord agreement to reduce global greenhouse gas emissions.
It was the third global treaty to combat climate change abandoned by the United
States. Pruitt was a vocal proponent of the withdrawal, and his argument won out
over officials who believed that international obligations should be honored from
administration to administration.
The withdrawal was characteristic of the Trump administration’s approach to
governing and conformed with Charles Koch’s views. Trump and his advisors
considered the Washington bureaucracy to be a parasitic population, feeding off the
American economy. To combat these parasites, the administration left jobs unfilled,
transferred career employees considered disloyal into dead-end jobs, and failed to
appoint staff members to the one review board that considered employee complaints.
This slow corrosion of the civil service melded smoothly with Charles Koch’s goals.
There would be no harm in letting the administrative state recede.
Still, it wasn’t clear how effective Pruitt was in his effort to dismantle, or
permanently hobble, the EPA. His efforts to repeal the Clean Power Plan and other
measures would face legal challenges. Pruitt also seemed to be stalling on the tedious
and time-consuming work of chopping up the EPA’s functions and delegating them
to other agencies, as Schnare had suggested. Finally, Pruitt became fatally distracted—
by mid-2018, he was the focus of eleven federal investigations for his spending on
security and relationships with lobbyists. He asked one of his staffers, for example, to
reach out to Chick-fil-A to win Pruitt’s wife afranchise location.
In July of 2018, Pruitt resigned. He was temporarily replaced by his deputy,
Andrew Wheeler, a former coal industry lobbyist. In certain circles, there was hope
that Wheeler would be more focused and more disciplined in carrying forward some
of the goals outlined in Schnare’s transition plan.
Even within the chaos of Pruitt’s tenure, he achieved important victories for Koch
Industries. The effort to regulate greenhouse gas emissions had been purged from the
EPA, at least temporarily, pushing back the date when carbon emission limits might
harm Koch’s oil refining and trading operations.
The Trump administration also did something that seemed impossible—it
politicized the issue of climate change even further than it had been in 2010. It
seemed inconceivable, in the Trump era, that any Republican or conservative
Democrat could even broach the topic of combating climate change. The real-world
effects were measurable. When George W. Bush was elected president, atmospheric
concentrations of carbon were 375 parts per million, far exceeding the record level of
human history. When Barack Obama pushed for the cap-and-trade bill in 2010,
carbon dioxide levels were 393 parts per million. In 2018, the concentrations reached
410 parts per million, a new record.
In late 2017, Charles Koch’s political network released a memo to its donors. The
memo touted two big achievements that year. The first was the “comprehensive tax
reform bill,” which the memo said was the network’s top priority. The second was
the regulatory rollback administered by cabinet members like Scott Pruitt, including
the proposed repeal of the Clean Power Plan and the withdrawal from the Paris
Climate Accord.
The Koch network couldn’t claim credit for these accomplishments. The group
had shaped the Trump agenda but had not written it. The balance of power between
the Trump administration and the Koch network was still uncertain. Koch claimed
some victories, but it was clear that Donald Trump was determined to go his own
way. Trump abandoned a major trade deal in Asia and imposed tariffs on goods from
Europe and China, policies that Charles Koch vehemently opposed.
Inside the Trump administration, there was disdain for Charles Koch because he
was considered too ideological, inflexible, and out of touch with American voters.
Trump’s influential policy advisor, Steve Bannon, made this disdain public during an
interview with the New York Times Magazine, published in March of 2017. Bannon,
indirectly praising Donald Trump’s brilliance, disparaged the Democratic Party.
Then he took a shot directly at Charles Koch: “And then the Republicans, it’s all this
theoretical Cato Institute, Austrian economics, limited government—which just
doesn’t have any depth to it. They’re not living in the real world.”
It seemed that the Trump administration and the Koch network were like
opposing chess players who couldn’t clear the board. There was no clear winner. But
Charles Koch pressed his advantage. His donor network announced that they would
spend between $300 million and $400 million during the 2018 midterm elections,
helping shape the most important political contest of Trump’s presidency.
The Koch network maximized its influence with this money by forging a
connection with the one senior member of the Trump administration with whom
Charles Koch had a long relationship—Vice President Mike Pence. As an Indiana
congressman, Pence was a close ally of Americans for Prosperity, a relationship that
lasted after Pence entered the White House. In June of 2017, while Charles Koch
attended a meeting with his donor network in Colorado Springs, Koch took a detour
to hold a private meeting with Pence and a handful of Pence’s staff members at the
Broadmoor Hotel. The meeting lasted roughly an hour, and was not on Pence’s
official schedule for that day. Koch and Pence discussed Trump’s legislative agenda,
including the tax cuts and health care reform. Pence was later given responsibilities
for helping manage Trump’s strategy for the 2018 midterms. Trump said that if the
Democrats won control of the House or Senate, their first order of business would be
impeachment proceedings, which would disrupt the presidency. The contest was
vital, and Charles Koch ensured he would be a major player in it.
With this money hanging in the balance, Charles Koch traveled to Palm Springs in
January of 2018 to host the meeting of his donors. As the event got underway,
Charles Koch took the stage, standing behind the podium as an evening breeze blew
through the luxury resort. He wore a suit jacket and blue shirt, with no tie. He looked
profoundly confident, and told his colleagues that they were making great progress in
the Trump era.
“I’m more excited about what we’re doing and about the opportunities than I’ve
ever been,” he said. “We’ve made more progress in the last five years than I had in the
previous fifty.”
In typical fashion, Koch then made a joke at his own expense, pointing out that
some people might have wondered what he was doing all those fifty years, if he hadn’t
achieved great results. The comment drew light laughter. But it was clear enough
what he had been doing. He had been building a political network with a reach and
influence that was arguably stronger than any other in corporate America. Only the
CEO of Koch Industries could call upon a massive lobbying operation, an army of
grassroots activists, a donor network with contributions in the billions of dollars, and
a universe of political front groups and donor vehicles nearly impossible for outsiders
to map. If the CEO of General Electric or any other publicly traded company tried to
build a similar machine to influence public policy, and dedicated as much time and
money to it as Charles Koch, then that CEO would almost certainly be curtailed by a
board of directors. Thanks to his efforts to retain such tight control over Koch
Industries, Charles Koch did not face this dilemma. His political network was
enduring, and massive. And it would almost certainly outlive the Trump
administration.
Charles Koch possessed an attribute that seemed to elude Donald Trump—he
possessed almost limitless patience, and atime horizon that was measured in decades.
After the laughter passed during his speech, Charles Koch explained that his fifty
years of work in politics had a clear directive, even if the results were slow in coming.
“You’ve got to build the foundation before you build the house,” he said. “That’s
what I claim I was working on.”
I. The change that appeared to win over Meadows and the Freedom Caucus was curiously minute. An
amendment introduced by Republican congressman Tom MacArthur allowed states to request a waiver from
certain obligations imposed by Obamacare, essentially punting hard decisions about cutting health care coverage
to state governors. A Brookings Institution analyst speculated that the MacArthur Amendment made the bill
palatable in part because it allowed the House to pass the bill on to the Senate, making it the upper chamber’s
problem.
II. This similar tax was called a Value Added Tax on sales inside a country. While not exactly the same as the
border adjustment proposed by Paul Ryan, the widely used VATs frequently included border adjustments,
allowing economists to study their impact.
III. The BAT wasn’t expected to be all good for exporters. Most experts expected that a BAT would eventually
strengthen the dollar, making US products more expensive overseas. But the tax structure would still most likely
benefit exporters over firms that shipped production overseas.
IV. West Texas Intermediate
V. In 2018, Americans for Prosperity attacked Collins with a campaign of Internet ads, direct mail, and radio
spots as she sought reelection.
CHAPTER 25
Control
(2018)
It was about six in the morning, in the middle of winter, when dawn started to break
over Charles Koch’s family compound in Wichita. Behind the compound’s tall walls,
treetops became visible in the faint light, their branches bare and sharp. The sky
turned faintly purple, then pink. Outside the compound, a man sat alone in a large
black Chevy Tahoe with tinted windows, apparently watching the walls. The man sat
patiently. He looked down at his phone and waited, the light of its screen making his
face glow. His headlights were extinguished and he was all but invisible to the
morning traffic that passed by. Then, a little bit before six thirty, the man in the
Tahoe flipped on his headlights and drove forward. At the same time, another black
SUV emerged from Charles Koch’s compound, pulling out from an entrance that
was partly obscured by shrubbery. The man in the Tahoe pulled out into traffic, his
timing impeccable, and fell into line behind the other black SUV. Both cars headed
north, toward Koch Industries headquarters.
Part of the myth about Charles Koch was that he drove himself to work every day,
parking in front of Koch Industries headquarters and walking up the stairs to his
office. His reality was different now. It was an open secret in Wichita that Charles
Koch rode to work in a convoy of armored vehicles, chaperoned by armed security
guards. This was seen as pragmatic. Since he had become politically active, Charles
Koch was a magnet for death threats. He was a private man, little understood and
widely hated. He was now also one of the richest men on earth, so security was
necessary. Charles Koch’s great skill was analyzing and mitigating risk.
Traffic was light this early in the morning. The black SUVs drove past strip malls
as they headed north. The sky continued to lighten, but only slightly. At this time of
day, the commute to Koch headquarters lasted only a matter of minutes. The Koch
Industries campus was visible from miles away. The Tower sat at the center of the
campus, still the tallest building within several miles. The first rays of the morning
sun glinted off the dark brown granite walls and the opaque windows. The parking
lots around the Tower were still illuminated, this early in the morning, by bright
lights that hung from the top of tall black poles. The lights made the campus look like
a self-contained universe, a splendidly isolated pool of shining stars, surrounded by a
wall. It was a beautiful sight in the morning. Kochland.
When he arrived at work, Charles Koch’s car pulled into a special parking garage
with high security. The lot was near the bombproof chamber where mail was sorted
before entering the building. Here was a universe that he, primarily, had authored.
The people he encountered spoke a language he invented, worked in business units
he oversaw, and granted him the kind of deference enjoyed by national leaders. When
he entered the hallways of his office building, Charles Koch could take the elevator
up to the third floor, or walk there through the spacious and well-lit stairwell.
The hallways were hushed in the morning. The décor of the third floor, which
housed Koch’s executive suites, had barely changed in twenty years. The doorway to
the executive suite was near the elevator bank. Walking inside that door, Charles
Koch passed into a spacious lobby. There was a couch, a table, and a small bookcase
across from the desk where his assistant sat. Beyond the desk was the doorway to his
office. And to the left, on the other side of the lobby, was the entrance to the
corporate boardroom, the site of countless strategy sessions and battles over the
decades.
As he walked to his office, Charles Koch passed a sculpture. It was a bust of his
father’s head, mounted on a tall pedestal, surrounded by decorative plants. It looked
like a monument to a nation’s founder. It had been fifty years since Fred Koch died
and Charles took over the family company. Fred Koch, that difficult and driving
man, was now safely enshrined in the form of a memorial, a silent bust. The man who
had encouraged his sons to wear boxing gloves and fight one another, the man who
forced Charles Koch to dig weeds in the family yard with a spoon, the man who sent
Charles to military school, who used guilt to drag Charles back home to Wichita to
run the business, that man was gone. There was only the memory of him—a memory
that was shaped and cultivated by his son Charles. Every year in September, Charles
Koch hosted the “Founder’s Day” memorial event, where he talked about his father’s
legacy. He wrote about his father and produced videos about his father. He
controlled the narrative. And one part of the narrative that Charles Koch didn’t
emphasize, maybe because he didn’t have to, was that Charles’s achievements had
surpassed his father’s. Fred Koch left behind a company that was a motley assortment
of assets—a cattle ranch, a share in an oil refinery, a gas-gathering business. Charles
Koch fused them together. Charles was the one who invented Koch Industries. Fred
Koch published a political tract and sold it through mail order. Fred Koch cofounded
the John Birch Society, a paranoid, marginal political group that dissolved into
obscurity. Charles Koch wrote his own political tracts and two books on MarketBased Management, one of which was a national bestseller. Charles Koch built a
political network that was arguably more influential than any other in corporate
America. Reporters and authors traveled from around the country, seeking an
audience with Charles Koch. His political pronouncements made the evening news.
Everything Fred Koch accomplished, Charles Koch surpassed.
And while he might not admit to this fact, Charles Koch must have been aware of
it, on some level, as he passed that bust of his father. He walked past the receptionist’s
desk and into his familiar office. He walked past the small leather couch and coffee
table, past the walls with their built-in bookshelves that held his personal library. His
desk was still in the same spot, over by the window. It was not uncommon for
Charles Koch to arrive at his desk justafter dawn.
When he sat down, Charles Koch could turn his head to take in a sweeping view
of the Kansas horizon. This view had changed over the last decade or so. It wasn’t all
empty space now. There was a public-school building just north of Koch
headquarters and some suburban neighborhoods to the northeast. But the landscape
changed only because Charles Koch had allowed it to change. He owned virtually all
the land he could see, out to the horizon. He had purchased the acreage over time, at
reasonable prices. He donated the land on which the public school sat to clear the
way for its construction. When Charles Koch gazed out his window, he saw a
landscape that he controlled.
If this control was like a gravitational field—shaping everything within it—then
the epicenter of the field was the Koch Industries campus. The campus extended
north, surrounded by the large wall that bowed out in a horseshoe shape with trees
planted along its length. Within the wall was the vast parking lot, which started to fill
with cars very early in the morning. Charles Koch could sit at his desk and watch the
employees get out, filing into the entrance of the underground pedestrian tunnel that
brought them into the Tower. As they walked through the tunnel, the employees
passed the mounted collages with black-and-white photos of the Koch family history.
When they reached the elevator bank below the Tower, they stood near the large
portrait of Charles Koch, smiling. The portrait was composed of tiny photos of Koch
Industries employees, as if Charles Koch himself incorporated all of them.
Every quarter, the business leaders from Koch’s various divisions came to the Tower
to report to Charles Koch. When it was time for such meetings, Charles could rise
from his desk and walk across the small lobby into the boardroom, where the senior
leadership team was seated around the large circular table. The boardroom was still
spartan in its decoration. The puffy leather office chairs were unremarkable. The only
extravagance was the leather coasters placed at each seat at the table, emblazoned with
the company logo. Extra chairs lined the outside wall of the windowless room,
providing seats for any support staffers.
Charles Koch sat and listened as his business leaders explained their most recent
quarter. He interrogated them and looked for soft spots in their presentations. It was
always understood that chaotic market forces were slamming against their front door,
and everyone would be accountable for their reactions. If a division lost money, the
division’s president needed to provide a detailed vision for regaining profits over the
long term.
In 2018, as he listened to the division heads make their presentations, Charles
Koch oversaw a corporation that seemed to vindicate his every belief. Entire, massive,
profitable units of the company did not even exist in 2000, when Charles Koch
launched a turnaround effort after the disasters of the 1990s. Georgia-Pacific, for
example, was generating over $1 billion in annual profits, on average. The Koch
Fertilizer division, the result of one risky bet in 2003, was delivering billions in
revenue each year. Then there was Molex, the microchip company, and Guardian
Industries. Charles Koch could make the case that his company wasn’t just
perpetually growing, but perpetually transforming as well, entering new industries,
abandoning the old, always searching for the next opportunity. And bolstering these
experimental efforts were the reliable cash cows. The Pine Bend refinery, still refining
cheap crude and selling expensive gasoline, throwing off cash around the clock. And
now Corpus Christi, repeating the same trick thanks to the fracking revolution. And
the trading division, still selling derivatives, still trading in markets where it had an
unparalleled view into real-time shipments and inventories.
Charles Koch’s beliefs would have been validated in another way during these
meetings. Senior leaders at Koch Industries phrased everything they said in the
vocabulary of Market-Based Management. One of Charles Koch’s indisputable
accomplishments over the preceding thirty years was creating an organization where
every employee—to a person—publicly subscribed to the same intricately encoded
philosophy. Division heads who came to Wichita spoke in terms of mental models
and discovery processes and the five dimensions. They talked about integrity.
Decision rights. Challenge processes. Experimental discovery. Virtues and talents.
These weren’t dog whistles or catchphrases. They were the internal vocabulary of
Kochland. Learning them was the first condition to winning a seat at the table.
Downstairs, on the first floor of the Tower, the hallways were lined with classrooms
where new recruits sat around circular tables during daylong learning sessions,
memorizing this vocabulary and learning the rules of MBM. As Charles Koch himself
put it, the new recruit either subscribed to this philosophy entirely, or they left Koch
Industries. There was no halfway.
The real-world verdict about MBM’s efficacy was less clear than Charles Koch’s faith
in it. In 2018, as Charles Koch listened to a parade of business leaders describe their
operations, there were signs of trouble within Koch Industries. If MBM really was the
code of achieving prosperity, then prosperity was necessarily an uneven and volatile
thing.
Invista, for example, was deeply troubled. Depending on one’s point of view, the
Invista acquisition in 2004 was either a disappointment or a disaster. In the spring of
2018, the Invista wing of the Koch Industries headquarters was like a ghost town of
empty cubicles. In 2017 alone, Invista cut fifty-two jobs in Athens, Georgia, sold a
plant in Tennessee, and sold another one in Derry, Ireland. It seemed that MBM
couldn’t fix whatever ailed Invista and the global market in synthetic fabrics.
Similarly, MBM seemed inadequate to reduce workplace injuries inside GeorgiaPacific. The injury rate fell slightly during the first few months of 2018, but was still
at the elevated levels that began in 2012. Jim Hannan and his team were still trying to
solve the problem, but it stubbornly persisted.
There were also signs that Koch Industries, in spite of strict adherence to MBM,
was repeating some of the mistakes of the 1990s. The company’s acquisition spree
had once again saddled it with wildly diversified units that seemed like an unnatural
fit with one another—glass, steel, computer sensors, greeting cards, and advanced
fertilizers, all under one roof. Molex, the microchip and sensor company, was already
delivering mixed results. In 2017, a Molex plant in Minnesotalaid off 136 employees.
The economy itself was shaky in the spring of 2018. The stock market swung
wildly, rising and falling with volatility that hadn’t been seen in years. There was
speculation that the economy had overheated, thanks in part to the kind of
government intervention Charles Koch despised. The Federal Reserve Bank had kept
interest rates at zero for several years after the crash of 2008, pumping global markets
with easy money. This was compounded by a program called Quantitative Easing,
which essentially pumped more than $3.5 trillion of new US dollars into the
economy. If this radical monetary policy caused asset bubbles to appear in different
pockets of the US economy, those bubbles might soon pop. When that happened,
Koch’s corporate structure would be tested in ways it hadn’t been tested in a decade.
The weaker divisions might suffer massive losses.
If the economic future was uncertain, Charles Koch seemed supremely calm
during the winter and spring months of 2018. This might have been due to that fact
that even in the worst-case economic scenarios, there was seemingly no plausible
scenario in which Koch Industries actually failed. There might be layoffs. The
company might have to sell some divisions at fire-sale prices. But the Koch Industries
entity itself, the core business that executives referred to as KII, seemed impervious to
failure. There was simply too much cash in the company, and too little debt, to
envision it going under. Koch’s bread-and-butter assets—the oil refineries, the
fertilizer plants, the paper mills, the commodities trading desks—were part of the
machinery that provided life’s necessities. People would buy gasoline and fertilizer
during any recession, and it was unlikely that big companies could swoop in and
build multibillion-dollar facilities to steal Koch’s share of the business. Koch’s
business was also protected by the masterfully constructed corporate veil, the massive,
multichambered legal nautilus shell that walled off various parts of the company
from one another. Divisions could fail and be sued, but the damage would never
penetrate to the heart of KII.
Charles Koch had other reasons to be supremely calm during 2018. If Koch
Industries was impervious to bankruptcy, then Charles Koch was outright immune
to it. If ever there was evidence for his faith in his own abilities, and the power of
MBM, then it was in the size of his private fortune.
In 1991, Fortune magazine estimated that Charles and David Koch were worth a
combined $4.7 billion, putting them among the wealthiest people in the world. This
fortune was the estimated value of Charles and David’s roughly 80 percent ownership
stake in Koch Industries, which the brothers split evenly.
The policies of the Clinton presidency did not diminish this fortune. During the
1990s, the Kochs’ family fortune almost doubled. In 2002, Forbes magazine estimated
that Charles and David Koch were worth a combined $8 billion.
The fortune exploded during the Bush years, against a backdrop of growing
government, uneven economic growth, and overseas military campaigns. In 2007,
Charles Koch alone was worth an estimated $17 billion. He and his brother were
worth a combined $34 billion, the third-largest fortune in the United States behind
Warren Buffett’s.
During the Obama years—the years when Americans for Prosperity warned
repeatedly about the threat of creeping socialism—Charles and David Koch’s fortune
more than doubled once again. At the end of the Obama administration, Charles
Koch was worth $42 billion. Together, Charles and David were worth $84 billion, a
fortune larger than Bill Gates’s $81 billion. By 2018, Charles Koch’s fortune
amounted to $53.5 billion.
Charles Koch was so rich in part because he fought so hard, for so many years, to
keep his company private. The vast majority of Koch Industries’ ownership wasn’t
spread among thousands of shareholders, but only two. The employees at Koch
Industries—including its senior executives—could not earn a real equity stake in the
firm, no matter how hard they worked. They earned, instead, the right to shadow
stock, essentially a derivatives contract based on the company’s performance. They
also earned onetime merit bonuses.
This ownership structure, while rare in corporate America, reflected the US
economy in 2018. Charles Koch’s household was part of an exclusive club—about
160,000 households in America were in the wealthiest 0.1 percent of the population.
This group prospered just like Charles Koch. In 1963, the top 0.1 percent of
households possessed 10 percent of all American wealth. By 2012, they possessed 22
percent. This gain came as the vast majority of Americans’ lost ground. The bottom
90 percent of Americans possessed about 35 percent of the nation’s wealth in the
mid-1980s. By about 2015, their share had fallen to 23 percent.
The American labor market resembled the labor market inside Kochland. For
more and more Americans, employment and income were now contingent,
temporary, and reflected the volatile swing of market conditions. Labor unions,
which had shielded workers from financial volatility for decades, were a negligible
sideshow of the American economic scene. Militant unions like the OCAW at the
Pine Bend refinery were a novelty found in history books. Even the modern, relatively
powerless unions like the IBU in Oregon were vanishingly rare. Full-time jobs were
increasingly replaced by contract jobs and part-time work. Pensions were replaced by
401(k) plans, whose value rose and fell with the markets. Pay was not steady and was
increasingly tied to bonuses rather than annual raises. Across America, the ownership
of wealth reflected the ownership structure of Koch Industries. The vast majority of
Americans owned shadow stock in the American enterprise.
This disparity in American wealth reflected the disparity in political power. The
rich and well connected shaped policy in America. It helped, in 2018, to have several
hundred million dollars at your disposal and a large lobbying office, coupled with
think tanks and a grassroots army, to have your policy preferences recognized. In
2014, a group of political scientists at Princeton studied the policy outcomes on
1,779 issues between 1980 and 2002. They found that no group in America had a
surefire hold over policy making. But the rich—a group they called the “economic
elite”—had, by far, the best chance of turning their policy choices into a reality. The
second most-powerful entities in Washington were special interest groups like
lobbying organizations, which had a lower success rate than the ec

        """

prompt = f"Use the first person, imagine you are interviewing for the cato institute , explain how the book above contributed to your own political philosophy. In a bulleted form"
# prompt = f"""Use the first person, imagine you are interviewing for the cato institute, here is my current response on how I believe the book contributed to my own political philosophy. I'm trying to fill in specific examples for my response. Currently just saying examples are two vague so please help me figure out what specific examples from the book i can reference here is the response i have so far:
# - Gained deeper appreciation for the practicality of free-market principles:
  
#   * The stark contrast between wealthy and impoverished nations reinforced my belief in individual economic freedom as a driver of prosperity.
#   * Observing how minimal government intervention in places like Hong Kong spurred growth, I became convinced of the benefits of laissez-faire economics.

# - Strengthened conviction in the importance of property rights and rule of law:

#   * Seeing the critical role of property rights in wealth creation, I realized that securing these rights is foundational to economic success.
#   * The book's examples highlighted that without the rule of law, markets can neither function properly nor protect individual freedoms.

# - Acknowledged the moral dimension of free markets:

#   * The concept of the "invisible hand" leading to societal benefits helped shape my view that self-interest can positively impact the community.
#   * I came to understand that wealth created through market exchanges is a moral outcome as it arises from voluntary and beneficial interactions.

# - Recognized the complexity of culture in economic development:

#   * The book showed me that while culture plays a role in a nation's economic narrative, it can both aid and hinder development.
#   * This nuanced understanding helped refine my political philosophy to advocate for economic systems that can transcend cultural limitations.

# - Emphasized the necessity of personal responsibility and hard work:

#   * Through the lens of different global economies, I concluded that personal initiative is indispensable for economic advancement.
#   * The success stories in the book reaffirmed my belief that individual effort, backed by a free-market system, yields the greatest rewards.

# - The importance of pragmatism in policy-making became clear:

#   * The real-world examples illustrated that rigid ideologies often fail to address economic challenges effectively.
#   * My political philosophy now incorporates a more pragmatic approach, advocating for policies that are evidence-based and results-driven.

# - Reinforced skepticism of large government’s role in the economy:

#   * Witnessing the negative consequences of excessive government control and intervention solidified my support for limited government.
#   * I now argue for a political philosophy that prioritizes minimal state interference in economic affairs to maximize growth and innovation.

# - Deepened understanding of the unintended consequences of wealth redistribution:

#   * The book's insights into failed attempts at economic fairness shaped my belief that forced redistribution can do more harm than good.
#   * I advocate for a system where wealth generation is encouraged rather than redistributed, as it naturally leads to broader societal upliftment.


#  """

response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]
)

generated_message = response.choices[0].message.content.strip("'")

print(generated_message)