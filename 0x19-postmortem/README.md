# Postmoterm Report On 500 Server Error Expirienced by clients of PayMe App
![what just happened](https://github.com/devmarrie/alx-system_engineering-devops/blob/master/0x19-postmortem/images/prob.gif?raw=true)

## Issue Summary

From 8:19 AM to 9:30 AM EAT, requests to most PayMe APIs resulted in 500 error response messages. PayMe apis serving customer sign in, payments and dashboard were mostly affected. At its peak, the issue affected 100% of user login service and accessing their payments to various services aquired via the app. Users could continue to access certain APIs that run on separate infrastructures. The root cause of this outage was an invalid configuration change that exposed a bug in a widely used internal library.

Timeline (East African Time)

    * 8:19 AM: Configuration push begins
    * 8:24 AM: Outage begins
    * 8:26 AM: Pagers alerted teams
    * 9:15 AM: Successful resolving
    * 9:19 AM: Server restarts begin
    * 9:30 AM: 100% of traffic back online

## Root Cause

At 8:19 AM EAT, a configuration change on the user endpoint was inadvertently released to our production environment without first being released to the testing enviroment. This changes affected the ability of users to use their passwords to validate payments. Thus  at 8:26 AM EAT, the service outage began.

## Resolution and recovery

At 8:26 AM EAT, the PagerDuty alerted our engneers on duty about the incident. At 8:54 AM, we attempted to rollback the problematic configuration change. We managed to successfully rollback at 9:15 AM after isolating and resolving the problem.
To help with the recovery, we turned off some of our monitoring systems which were triggering the bug. By 9:19 AM, 25% of traffic was restored and 100% of traffic was routed to the API infrastructure at 9:30 AM.

## Corrective and Preventative Measures

We resolved  that before any commit to production the following should be done:

   -  Restrict the number of people who can push changes to production for more accountability(Completed.)
   - Programmatically enforce staged rollouts of all configuration changes.
    - Improve process for auditing all high-risk configuration options.
    

We sinceerly appologise for the inconviniences caused and thank you for bearing with us during the downtime.

Sincerely,

PayMe Development Team


