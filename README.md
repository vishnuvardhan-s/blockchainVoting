# blockchainVoting
Regenerative Voting System using Azure Blockchain and Raspberry

  There is an increasing number of EVM Hacks and a lot of effort made to securely trasport the EVM Machines to the Counting Booth.  With our project, we ensure that there will be no third party who interacts with the voting sytem.  We use RFID cards to uniquely identify a voter along with his AADHAR card.  The details of the voter are stored in a separate database along with his mail id and the AADHAR number.  The Zone Representative can also check if the voter has already voted or not using the RFID card.

  Even if the RFID card is lost, the uniqueID of the Voter can be found using the AADHAR number he has.  There is also a functionality to find the mail id of the Voter with the help of his unique id.
  
  Microsoft SQL management studio is used for the Database.  After verification, the User enters into the Blockchain Application that is created using his mail id and the password that only he knows.
   
  There are three roles in our Blockchain Application. 
    1.ElectionHead
    2.ZoneRepresentative
    3.Voter
 
  The Election Head is the one who adds the candidates and the Voters in the Blockchain Application. He is also responsible for the declaration of results.
  
  The Zone Representative will take care of Initiating the Election on the Election Day.
  
  The voter signs into the Blockchain Application and votes for the candidate.
