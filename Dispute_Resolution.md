Variable      |  Description          |  Parameter
-----------------------|-----------------------|-----------------------
join group       | such as VP table, auction, etc; open question: should admittance be a seperate step (by gatekeeper) or only join groups that would approve applicant?  | .1
Requestsign  |  co-signer approve transaction (for multisig wallet)   | .1
approvesign    | Co-signer approves transaction  | .1
rejectsign     |  Co-signer rejects transaction   | .1
bounty          | request service, specified by terms   | .1  
transfer           | agent moves asset without receiving a specific object or service in return | .1
offer               | object, terms can be fixed price or auction  | .1
offerbribe                   |   to misreport outcome of hand       | .1
acceptbribe                     |    to misreport outcome of hand   | .1
rejectbribe                 |  continue accurately reporting outcome of hand  | .1
Rescind propose         |    only possible at n+1 for proposal at time n    | .1
bid                   |     for offered good during auction, at whatever is spot price  | .1
complete auction            |     accept high bid, end auction, and transfer    | .1
counter bid           |     at next increment   | .1
Contest hand               |      send to dispute resolution    | .1
judge affirmative         | in favor of claimant    | .1
judge negative            | in favor of contestor   | .1

This is just a start, Russell and I will extend as we build a toy version of Dispute Resolution in MESA
Dispute Resolution Pack: Containing objects for simulating
environments in which one or more classes of agents have
judicial/arbitration power, and how their actions and networked
structure affect the perceived rewards available for other classes of
agents (users). Some network structures (such as cadres/cliques) can
negatively impact trust in the system and perceived reward and
penalty distribution, which is of central interest to groups in diverse
domains.
