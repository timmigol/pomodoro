class Timer:
    def __init__(self, root, update_callback):
        self.root = root
        self.update_callback = update_callback
        self.default_time = 1500  # 25 minutes
        self.remaining_time = self.default_time
        self.running = False
        self.after_id = None

    def countdown(self):
        if not self.running:
            return

        self.remaining_time -= 1
        minutes, seconds = divmod(self.remaining_time, 60)
        formatted_time = f"{minutes:02}:{seconds:02}"
        self.update_callback(formatted_time)

        if self.remaining_time > 0:
            self.after_id = self.root.after(1000, self.countdown)
        else:
            self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.countdown()

    def pause(self):
        if self.running and self.after_id:
            self.root.after_cancel(self.after_id)
            self.running = False

    def reset(self):
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.running = False
        self.remaining_time = self.default_time
        minutes, seconds = divmod(self.remaining_time, 60)
        formatted_time = f"{minutes:02}:{seconds:02}"
        self.update_callback(formatted_time)
