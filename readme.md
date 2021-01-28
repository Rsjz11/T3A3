Discuss how the app handles privacy user data and how security features of the framework utilising will assist to mitigate security concerns.

The application aims to be as secure as possible. Provided that SQL injection attacks are one of the most frequent attacks that jeopardise the privacy of data, this application tries to reduce the chances of SQL injections to be effective. Input validation is the first security measure to be discussed. Input validation simply determines what is and what is not acceptable input by the user. Constraints are conditions that can be placed upon the input and only when the inputs meet the specifications of the constraints will the input be deemed valid. 

Parameterized query: precompiling a SQL statement to which only parameters need to be added. This has not been utilised in the application, but believe it important to address. 

Stored procedures: SPs are grouped SQL statements put together to carry out a purpose. SP are useful when commonly repeated SQL statements are being used. By using SP you can use SP without worrying about the database security (Assuming the SP was designed to be secure). 

Escaping: The application uses character-escaping functions for user-supplied input. This ensures that the database does not confuse input from the user with the input of the developer. By adding Escaping as a security measure, it avoids the challenge of unintended changes to the database. (NOT SURE YET)

Avoiding administrative privileges: It is bad practice to connect an application to the database using an account with root access. Therefore, the application does not do this. The security ramifications of conncting an application to the database using an account with root access is that it could undermine the whole system should a malicious attacker gain the credentials to the root account. In addition it is good practice to limit the privileges given to users. I have taken the approach to give privileges based on requirements opposed to taking away privileges. 

Web application firewall: This is a feature that I would like to add however I am unsure as to whether I am capable of adding a Web application firewall. According to Positive Technologies the WAF (Web application firewall) is "one of the best practices to identify SQL injection attacks...". The firewall acts as a barrier and filters through the data acting only on files that are deemed a threat. It is easy to use and simple to modify. Postive Technologies continues to state that 'WAF should always be considered a part of web security defense in-depth strategy'. SQL injection attacks can occur with large variations and therefore prevention techniques mentioned above excluding WAF are often unable to protect the database. Because of this, WAF is recommended to be used in tandem with the other prevention techniques. WAF provides protection for custom web applications that are usually unprotected. 

Source:
https://www.ptsecurity.com/ww-en/analytics/knowledge-base/how-to-prevent-sql-injection-attacks/#2

Discuss how I will address; Professional obligations (timely manner, explicit about maintenance of the system, industry ethical obligations, legal obligations OR privacy impications)

