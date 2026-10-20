Approach CERID

C - Clarify requirements
E - Entities
R - Responsibilities
I - Interactions
D - Durability

Bonus - Thread safety


1. Clarify Requirements 

- system should send notification to user 
- support multiple channels (email, sms, push)
- user can have preference which channel they want
- retry mechanism


2. Entities

UserPreference
Notification
NotificationChannel
NotificationChannelFactory
NotificationService
NotificationDispatcher


3. Responsibilities

UserPreference - will remember user choice 
Notification - will keep notification message and metadata
NotificationChannel (interface) - business logic to send message through particcular channels
    - Email
    - SMS
    - Push
NotificationChannelFactory - create different notification channel objects
NotificationService - entry point and provide method to send notification
NotificationDispatcher - dispatches user notification through multiple channels based on user preference


4. Interactions

