

Field                      |             Description    |       Parameter
---------------------------|----------------------------|------------------------
stake           |     place in escrow with intent of receiving back after some period/series of events  | .1
Unstake         |     remove from escrow                        |   .1
Buy                        |       something on offer (specify agent offering) | .1
Sell                       |       something on offer (by this agent)         | .1
Hold         |     pass turn            | .1
Follow agent          | replace normal action evaluation procedure with simple imitation of another agent's action (without other agent's knowledge)          | .1
StopFollow          | return to normal action evaluation procedure   | .1 
Propose collusion     | agents agree to harmonize movements           | .1
bid                   |     for offered good during auction, at whatever is spot price  | .1
complete auction            |     accept high bid, end auction, and transfer      | .1
counter bid           |     at next increment           | .1
offer                 | make tokens available on secondary market at spot price   | .1
transfer                       | agent moves asset without receiving a specific object or service in return    | .1
claim bonus             | such as for posting articles, influencer social sharing    | .1

Informational activities to be included in agent state characteristics, but not explicit actions
Agent knowledge of surrounding users (some decay as you get further out on their social graph)
risk profile (preferably learned)
bounded rationality (probably a random obscuring of relevant information, or a deviation from identified ideal action function)
agent knowledge of global state
agent funds, maybe in more than just the token of interest
perhaps all accept/reject choices should be made at agent state update, rather than occupy a full time step as an action?

