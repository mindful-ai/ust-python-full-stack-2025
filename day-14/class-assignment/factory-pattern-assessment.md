# 🧩 Assessment Problem: Factory Design Pattern - Notification System

## **Problem Context**
You are working as a software developer for a company that builds a **web-based project management tool** (similar to Trello or Asana).  
Whenever certain events happen in the system—like a **new task is created**, **a task is assigned**, or **a deadline is approaching**—the system needs to send **notifications** to users.

However, users may have different **preferred notification channels**, such as:
- **Email**
- **SMS**
- **Push Notifications (Mobile/Web)**

Currently, your company’s codebase is filled with `if-else` or `switch` statements to handle different notification types. This makes the code difficult to maintain and extend whenever a new notification method is added.

Your task is to **refactor** the system using the **Factory Design Pattern**.

---

## **Objective**
Design and implement a **Notification Factory** that dynamically provides the correct notification object based on user preference.

---

## **Requirements**

1. Create an abstract class or interface named `Notification` with a method:
   ```python
   def notify_user(self, message: str): 
       pass
   ```

2. Create concrete classes for each type of notification:
   - `EmailNotification`
   - `SMSNotification`
   - `PushNotification`

   Each should implement `notify_user()` differently (just print a message like “Sending EMAIL: …”).

3. Create a **NotificationFactory** class with a method:
   ```python
   def get_notification(channel_type: str) -> Notification
   ```
   This method should return an instance of the correct notification type.

4. Write a **main function** that:
   - Accepts a user’s preferred channel (from input or a variable)
   - Uses the factory to get the appropriate notification object
   - Sends a notification

---

## **Example Input/Output**

### Input:
```
Preferred Channel: SMS
Message: "Your task is due tomorrow!"
```

### Output:
```
Sending SMS: Your task is due tomorrow!
```

---

## **Bonus Extensions**
- Add a new channel type like **SlackNotification** or **WhatsAppNotification** without modifying existing code (just extend).
- Store user preferences in a JSON file and dynamically select the notification type at runtime.
- Integrate logging to show which class was instantiated by the factory.

---

## **Evaluation Criteria**
| Criterion | Description |
|------------|-------------|
| **Correctness** | Implements Factory pattern correctly with minimal conditional logic |
| **Extensibility** | Supports easy addition of new notification types |
| **Code Quality** | Follows clean code practices and proper class design |
| **Practicality** | Simulates a real-world use case (notifications system) |

---

### **Submission**
- Submit a `.py` file with your implementation.
- Include a short README (optional) describing your approach.
