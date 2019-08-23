# blockchainVoting
## Regenerative Voting System using Azure Blockchain and Raspberry
## Objective
  There is an increasing number of EVM Hacks and a lot of effort made to securely trasport the EVM Machines to the Counting Booth.  With our project, we ensure that there will be no third party who interacts with the voting sytem.  We use RFID cards to uniquely identify a voter along with his AADHAR card.  The details of the voter are stored in a separate database along with his mail id and the AADHAR number.  The Zone Representative can also check if the voter has already voted or not using the RFID card.

## Functionalities
  Even if the RFID card is lost, the uniqueID of the Voter can be found using the AADHAR number he has.  There is also a functionality to find the mail id of the Voter with the help of his unique id.
  
  Microsoft SQL management studio is used for the Database.  After verification, the User enters into the Blockchain Application that is created using his mail id and the password that only he knows.

## Roles
  There are three roles in our Blockchain Application. <br />
    1.ElectionHead<br />
    2.ZoneRepresentative<br />
    3.Voter<br />
  <br />
  <br />
  The Election Head is the one who adds the candidates and the Voters in the Blockchain Application. He is also responsible for the declaration of results.
  <br />
  <br />
  <br />
  <a href="url"><img src="https://github.com/coderrag/blockchainVoting/blob/master/election%20head.jpg" align="left" height="400" width="1000" ></a>
  <br />
  <br />
  <br />
  The Zone Representative will take care of Initiating the Election on the Election Day.
  <br />
  <br />
  <br />
  <a href="url"><img src="https://github.com/coderrag/blockchainVoting/blob/master/zone%20representative.jpg" align="left" height="400" width="1000" ></a>
  <br />
  <br />
  <br />
  The voter signs into the Blockchain Application and votes for the candidate.
  <br />
  <br />
  <br />
  <a href="url"><img src="https://github.com/coderrag/blockchainVoting/blob/master/voter.jpg" align="left" height="400" width="1000" ></a>
  <br />
  <br />
  <br />
  ## Blockchain Application
  The blockchainVoting.json and blockchainVoting.sol files are deployed in the Azure Blockchain Workbench.  The candidates and voters are added in the election zone by the ElectionHead.  The ZoneRepresentative initiates the Election. After verifying the AADHAR number using the RFID Card, the voter is permitted to vote in the Azure Blockchain.  The Election Head finally declares the election and the contract is complete.
  ## Advantages
  **The main disadvantage of using only the Azure Blockchain for voting is that, if I have the username and password of my friend, relative or anyone, I can vote for them without their knowledge.  Our system provides an extra security of verifying the voter before he votes using the RFID Card.**  
  
