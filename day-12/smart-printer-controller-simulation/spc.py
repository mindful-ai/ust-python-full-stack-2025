import threading
import time
from queue import Queue

# ------------------------------
# Data Class: PrintJob
# ------------------------------
class PrintJob:
    def __init__(self, job_id, user, document_name, priority="normal"):
        self.job_id = job_id
        self.user = user
        self.document_name = document_name
        self.priority = priority

    def __str__(self):
        return f"[{self.job_id}] {self.document_name} by {self.user} ({self.priority})"


# ------------------------------
# Smart Print Queue Class
# ------------------------------
class SmartPrintQueue:
    def __init__(self):
        self.normal_queue = Queue()
        self.urgent_queue = Queue()
        self.undo_stack = []
        self.redo_stack = []
        self.completed_jobs = []
        self.lock = threading.Lock()
        self.active = True

    # ------------------------------------
    # Add Job
    # ------------------------------------
    def add_job(self, job):
        with self.lock:
            if job.priority == "urgent":
                self.urgent_queue.put(job)
            else:
                self.normal_queue.put(job)
            self.undo_stack.append(("add", job))
            self.redo_stack.clear()
            print(f"✅ Added job: {job}")

    # ------------------------------------
    # Cancel Job
    # ------------------------------------
    def cancel_job(self, job_id):
        with self.lock:
            temp_urgent = []
            temp_normal = []
            cancelled_job = None

            while not self.urgent_queue.empty():
                job = self.urgent_queue.get()
                if job.job_id == job_id:
                    cancelled_job = job
                    print(f"❌ Cancelled urgent job: {job}")
                else:
                    temp_urgent.append(job)

            while not self.normal_queue.empty():
                job = self.normal_queue.get()
                if job.job_id == job_id:
                    cancelled_job = job
                    print(f"❌ Cancelled normal job: {job}")
                else:
                    temp_normal.append(job)

            for job in temp_urgent:
                self.urgent_queue.put(job)
            for job in temp_normal:
                self.normal_queue.put(job)

            if cancelled_job:
                self.undo_stack.append(("cancel", cancelled_job))
                self.redo_stack.clear()
            else:
                print("⚠️ Job ID not found!")

    # ------------------------------------
    # Undo and Redo Actions
    # ------------------------------------
    def undo_action(self):
        with self.lock:
            if not self.undo_stack:
                print("⚠️ Nothing to undo.")
                return

            action, job = self.undo_stack.pop()
            if action == "add":
                self._remove_job(job.job_id)
                print(f"↩️ Undid Add: {job}")
            elif action == "cancel":
                if job.priority == "urgent":
                    self.urgent_queue.put(job)
                else:
                    self.normal_queue.put(job)
                print(f"↩️ Undid Cancel: {job}")

            self.redo_stack.append((action, job))

    def redo_action(self):
        with self.lock:
            if not self.redo_stack:
                print("⚠️ Nothing to redo.")
                return

            action, job = self.redo_stack.pop()
            if action == "add":
                if job.priority == "urgent":
                    self.urgent_queue.put(job)
                else:
                    self.normal_queue.put(job)
                print(f"🔁 Redid Add: {job}")
            elif action == "cancel":
                self._remove_job(job.job_id)
                print(f"🔁 Redid Cancel: {job}")

            self.undo_stack.append((action, job))

    def _remove_job(self, job_id):
        """Helper to remove a job by ID."""
        temp_urgent, temp_normal = [], []

        while not self.urgent_queue.empty():
            job = self.urgent_queue.get()
            if job.job_id != job_id:
                temp_urgent.append(job)

        while not self.normal_queue.empty():
            job = self.normal_queue.get()
            if job.job_id != job_id:
                temp_normal.append(job)

        for job in temp_urgent:
            self.urgent_queue.put(job)
        for job in temp_normal:
            self.normal_queue.put(job)

    # ------------------------------------
    # Show Pending Jobs
    # ------------------------------------
    def show_pending_jobs(self):
        with self.lock:
            print("\n🗂️ Pending Jobs:")
            urgent_jobs = list(self.urgent_queue.queue)
            normal_jobs = list(self.normal_queue.queue)
            if not urgent_jobs and not normal_jobs:
                print("📭 No pending jobs.")
            else:
                for job in urgent_jobs:
                    print(f"  🔴 URGENT: {job}")
                for job in normal_jobs:
                    print(f"  🟢 NORMAL: {job}")

    # ------------------------------------
    # Show Completed Jobs
    # ------------------------------------
    def show_completed_jobs(self):
        print("\n✅ Completed Jobs:")
        if not self.completed_jobs:
            print("📭 No jobs printed yet.")
        else:
            for job in self.completed_jobs:
                print(f"  ✔️ {job}")

    # ------------------------------------
    # Print Processing Thread
    # ------------------------------------
    def printer_worker(self):
        while self.active:
            with self.lock:
                job = None
                if not self.urgent_queue.empty():
                    job = self.urgent_queue.get()
                elif not self.normal_queue.empty():
                    job = self.normal_queue.get()

            if job:
                print(f"🖨️ Printing: {job}")
                time.sleep(3)  # simulate printing time
                with self.lock:
                    self.completed_jobs.append(job)
                print(f"✅ Completed: {job}")
            else:
                time.sleep(1)

    def stop(self):
        self.active = False


# ------------------------------
# Menu-Driven Interface
# ------------------------------
def menu():
    spq = SmartPrintQueue()
    printer_thread = threading.Thread(target=spq.printer_worker, daemon=True)
    printer_thread.start()

    while True:
        print("\n===== 🖨️ SMART PRINT QUEUE MENU =====")
        print("1. Add Job")
        print("2. Cancel Job")
        print("3. Undo")
        print("4. Redo")
        print("5. Show Pending Jobs")
        print("6. Show Completed Jobs")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            job_id = input("Enter Job ID: ")
            user = input("Enter User Name: ")
            doc = input("Enter Document Name: ")
            priority = input("Enter Priority (normal/urgent): ").lower() or "normal"
            job = PrintJob(job_id, user, doc, priority)
            spq.add_job(job)

        elif choice == '2':
            job_id = input("Enter Job ID to cancel: ")
            spq.cancel_job(job_id)

        elif choice == '3':
            spq.undo_action()

        elif choice == '4':
            spq.redo_action()

        elif choice == '5':
            spq.show_pending_jobs()

        elif choice == '6':
            spq.show_completed_jobs()

        elif choice == '7':
            spq.stop()
            print("🛑 Stopping Smart Print Queue System...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()
