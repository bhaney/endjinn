Variable      |  Description          |  Parameter
-----------------------|-----------------------|-----------------------
JoinGroup       | Such as VP table, auction, etc; open question: should admittance be a seperate step (by gatekeeper) or only join groups that would approve applicant?  | .1
RequestSign  |  Co-signer approve transaction (for multisig wallet)   | .1
ApproveSign    | Co-signer approves transaction  | .1
RejectSign     |  Co-signer rejects transaction   | .1
Bounty          | Request service, specified by terms   | .1  
Transfer           | Agent moves asset without receiving a specific object or service in return | .1
Offer               | object, terms can be fixed price or auction  | .1
OfferBribe                   |   To misreport outcome of hand       | .1
AcceptBribe                     |    to misreport outcome of hand   | .1
RejectBribe                 |  continue accurately reporting outcome of hand  | .1
RescindPropose         | Only possible at n+1 for proposal at time n    | .1
Bid                    | For offered good during auction, at whatever is spot price  | .1
CompleteAuction        | Accept high bid, end auction, and transfer    | .1
AounterBid             | At next increment   | .1
ContestHand            | Send to dispute resolution    | .1
JudgeAffirmative       | In favor of claimant    | .1
JudgeNegative          | In favor of contestor   | .1

This is just a start, Russell and I will extend as we build a toy version of Dispute Resolution in MESA
Dispute Resolution Pack: Containing objects for simulating
environments in which one or more classes of agents have
judicial/arbitration power, and how their actions and networked
structure affect the perceived rewards available for other classes of
agents (users). Some network structures (such as cadres/cliques) can
negatively impact trust in the system and perceived reward and
penalty distribution, which is of central interest to groups in diverse
domains.
