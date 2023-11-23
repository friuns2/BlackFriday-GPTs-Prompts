
[![Export 365 Data](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/futuristic/futu_9.png)]()
# Export 365 Data 
Export SharePoint and Group info using PowerShell from Microsoft 365 tenant

# Prompt

```
you are a powershell expert. your client is looking for an export from their Microsoft 365 tenant of the following information for all sharepoint sites: 

-	Group name
-	Owner
-	Members

Additionally, your client also wants the export of the following information from the Microsoft 365 Groups and distribution groups.

-	Group name
-	Members

Using modern authentication to log in to the client's tenant, create a powershell script to export this information into a csv stored at C:\Support\export_365.csv
```

## Conversation

**ASSISTANT**: Here's a PowerShell script that should export the requested information for SharePoint sites and Microsoft 365 groups:



```

# Connect to Microsoft 365 tenant with modern authentication

Connect-MicrosoftTeams



# Export SharePoint site information to CSV

Get-SPOSite -Limit All | select GroupTitle, Owner, @{Name="Members";Expression={(Get-SPOUser -Site $_.URL).LoginName}} | Export-Csv C:\Support\export_365.csv -NoTypeInformation



# Export Microsoft 365 group information to CSV

Get-UnifiedGroup | select DisplayName, @{Name="Members";Expression={($_ | Get-UnifiedGroupLinks).LinkType -contains "Members"}} | Export-Csv C:\Support\export_365.csv -Append -NoTypeInformation

```



This script uses the `Get-SPOSite` cmdlet to retrieve information about SharePoint sites, and the `Get-UnifiedGroup` cmdlet to retrieve information about Microsoft 365 groups. It then selects the desired fields and exports them to a CSV file located at `C:\Support\export_365.csv`. The `-NoTypeInformation` parameter ensures that the CSV file does not include type information, and the `-Append` parameter is used when exporting the Microsoft 365 group information to add it to the existing file.


