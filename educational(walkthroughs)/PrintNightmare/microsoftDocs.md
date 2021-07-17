https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527

# Windows Print Spooler Remote Code Execution Vulnerability

CVE-2021-34527  son of CVE-2021-1675 ? 

Print Spooler service improperly performs privileged file operations.

UPDATE July 7, 2021 Version 1607



In addition to installing the updates, in order to secure your system, you must confirm that the following registry settings are set to 0 (zero) or are not defined (**Note**: These registry keys do not exist by default, and therefore are already at the secure setting.), also that your Group Policy setting are correct (see FAQ):

-   HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Printers\PointAndPrint
-   NoWarningNoElevationOnInstall = 0 (DWORD) or not defined (default setting)
-   UpdatePromptSettings = 0 (DWORD) or not defined (default setting)

**Having NoWarningNoElevationOnInstall set to 1 makes your system vulnerable by design.**


https://support.microsoft.com/en-us/topic/kb5005010-restricting-installation-of-new-printer-drivers-after-applying-the-july-6-2021-updates-31b91c02-05bc-4ada-a7ea-183b129578a7
## **Resolution**

1.  Install the July Out-of-band and later updates.
    
2.  Check if the following conditions are true:
    

[-]   Registry Settings: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Printers\PointAndPrint
    
    -   NoWarningNoElevationOnInstall = 0 (DWORD) or not defined (default setting)
        
    -   UpdatePromptSettings = 0 (DWORD) or not defined (default setting)
        
[-]   Group Policy: You have not configured the Point and Print Restrictions Group Policy.
    

If both conditions are true, then you are not vulnerable to CVE-2021-34527 and no further action is needed. 

If either condition is not true, you are vulnerable. 
Follow the steps below to change the Point and Print Restrictions Group Policy to a secure configuration.

1.  Open the group policy editor tool and go to **Computer Configuration** > **Administrative Templates** > **Printers**. 
    
2.  Configure the Point and Print Restrictions Group Policy setting as follows:
    
    1.  Set the the Point and Print Restrictions Group Policy setting to "Enabled".
        
    2.  "When installing drivers for a new connection": "Show warning and elevation prompt".
        
    3.  "When updating drivers for an existing connection": "Show warning and elevation prompt".

![[printNightmare.png]]






## Workarounds

**Determine if the Print Spooler service is running**

Run the following in Windows PowerShell:

`Get-Service -Name Spooler`

If the Print Spooler is running or if the service is not set to disabled, select one of the following options to either disable the Print Spooler service, or to Disable inbound remote printing through Group Policy:

**Option 1 - Disable the Print Spooler service**

If disabling the Print Spooler service is appropriate for your enterprise, use the following PowerShell commands:

`Stop-Service -Name Spooler -Force`

`Set-Service -Name Spooler -StartupType Disabled`

if you need to print this might be useful:

`Set-Service -Name Spooler -StartupType Automatic`

`Start-Service -Name Spooler`

remember to turn it back off!

**Impact of workaround** Disabling the Print Spooler service disables the ability to print both locally and remotely.

**Option 2 - Disable inbound remote printing through Group Policy**

You can also configure the settings via Group Policy as follows:

Computer Configuration / Administrative Templates / Printers

Disable the “Allow Print Spooler to accept client connections:” policy to block remote attacks.

You must restart the Print Spooler service for the group policy to take effect.

**Impact of workaround** This policy will block the remote attack vector by preventing inbound remote printing operations. The system will no longer function as a print server, but local printing to a directly attached device will still be possible.