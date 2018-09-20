Field                 |             Description    |       Parameter
----------------------|----------------------------|------------------------
Stake                 | Place in escrow with intent of receiving back after some period/series of events  | .1
Unstake               | Remove from escrow                        |   .1
Buy                   | Something on offer (specify agent offering) | .1
Sell                  | Something on offer (by this agent)         | .1
Hold                  | Pass turn            | .1
FollowAgent           | Replace normal action evaluation procedure with simple imitation of another agent's action (without other agent's knowledge)         | .1
StopFollow            | Return to normal action evaluation procedure   | .1 
ProposeCollusion      | Agents agree to harmonize movements           | .1
Bid                   | For offered good during auction, at whatever is spot price  | .1
Ask                   | For offered good during auction, at whatever is spot price  | .1
Offer                 | Make tokens available on secondary market at spot price   | .1
CompleteAuction       | Accept high bid, end auction, and transfer      | .1
CounterBid            | At next increment           | .1
Transfer              | Agent moves asset without receiving a specific object or service in return    | .1
ClaimBonus            | Such as for posting articles, influencer social sharing    | .1

Informational activities to be included in agent state characteristics, but not explicit actions
Agent knowledge of surrounding users (some decay as you get further out on their social graph)
Risk profile (preferably learned)
Bounded rationality (probably a random obscuring of relevant information, or a deviation from identified ideal action function)
Agent knowledge of global state
Agent funds, maybe in more than just the token of interest
Perhaps all accept/reject choices should be made at agent state update, rather than occupy a full time step as an action?
