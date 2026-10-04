# Service: ISNetworld

Contractor web account, not the Empower phone app. Job values (client, site, USA#, course titles) live in `/workspace/jobs/<USA#>/`, never here.

## Sign-in

- URL: `https://www.isnetworld.com/Login`
- Step 1: field label **Username**, button **Continue**. Step 2: field **Password**, button **Login**. No password field until Continue.
- Use the app secure form (one step at a time). Never put the password in chat or a file.
- 1Password connect is Mac-only. Jesse has a Windows desktop and an iPhone, no Mac, so autofill is unavailable. Use the forms.
- After Login, a spinner can sit a long time. Wait. A tab discarded under memory pressure means the login did not stick — reopen `/Login` and sign in again.
- Finishing a course can dump the session back to `/Login`. Re-auth and continue the remaining list. Do not treat that as a failed course.

## Assigned courses

- List: `https://www.isnetworld.com/contractortraining/workers` (nav: Employee Information & Training → Complete Online Training).
- Rows: requirement owner = `<hiring client>`, requirement = `<site>`. Status labels seen: Complete, In Progress, Not Taken. Action: **Launch**.
- Library search by client name does not find assigned courses (**No Records Found**). Do not use Training Library for that.
- Project list: `https://www.isnetworld.com/employeetraining/ceprojectresourcesassignment.aspx`. Filter Hiring Client = `<hiring client>`.

When Jesse says finish the course: skip video with **Continue** (no audio), scroll down to unlock the next control, answer quizzes from on-screen text, check responsibility/acknowledgment boxes. Do not launch a sibling course unless he named it. Not every course shows a quiz score.

## Print Certificate

On the same workers list, a Complete row has **Print Certificate** (one course said **Print**). It downloads a PDF. Do not relaunch the course.

Save under `/workspace/jobs/<USA#>/certs/` and attach each PDF in the reply. `/workspace` can drop files.

## Google Drive

- Connector that worked: `user-Google-drive`. Create the folder with `create_file`, `contentMimeType` `application/vnd.google-apps.folder`, title `<Client> <Site> Training Certificates`. Upload each PDF with `upload_file`, `connection` `user-Google-drive`, `destination.folderId` from that create, `destination.name` the filename.
- `user-Google Drive-xai` `create_folder` failed (gateway error). Do not use it for this.

## Not this service

Empower is iPhone/Android only. `https://app.joinempower.com/` returned Firebase **Invalid Dynamic Link**. `https://www.joinempower.com/` is a marketing page. No desktop app.

## Web-request candidates (not proven)

Login is a two-step form; tokens were not captured, so do not replace sign-in with curl. Once a session exists, the workers list URL and each Print Certificate download are the likely GET candidates — capture the certificate response URL on the next run before clicking through print dialogs again.

## Example (USA26046 Cenovus Lima) — do not reuse values

Requirement owner Cenovus Energy Inc, requirement Lima. Project filter Hiring Client = Cenovus Energy Inc showed project Cenovus Lima Training Qualifications, requirement - TQ. Drive folder Cenovus Lima Training Certificates, id `1m_QZ5py4o8scRC7bye3wyOfGk2S4xmfz`. PDFs that day: Downstream Site Onboarding, Lima Refinery Vehicle Safety Spotter Escort Training, Refinery & Maritime Security Awareness (score 90%, pass 80%), Life Saving Rules (LSR). Expirations seen 2027-09-19. Those files were first saved under `/workspace/cenovus-certs/`; new saves go under `/workspace/jobs/<USA#>/certs/`.
