import requests


# =========================================================
# OPENROUTER API KEY
# =========================================================

API_KEY = "OPENROUTER_API_KEY"


# =========================================================
# TEACHING AGENT
# =========================================================

class TeachingGPT:

    def __init__(self):

        self.syllabus = ""
        self.topic = ""
        self.history = []

    # -----------------------------------------------------
    # INITIALIZE SESSION
    # -----------------------------------------------------

    def seed_agent(self, syllabus, topic):

        self.syllabus = syllabus
        self.topic = topic
        self.history = []

    # -----------------------------------------------------
    # USER MESSAGE
    # -----------------------------------------------------

    def human_step(self, human_input):

        self.history.append(
            f"Student: {human_input}"
        )

    # -----------------------------------------------------
    # AI RESPONSE
    # -----------------------------------------------------

    def instructor_step(self):

        recent_history = "\n".join(
            self.history[-6:]
        )

        prompt = f"""
        You are an intelligent AI Tutor.

        Teach clearly and step-by-step.

        Topic:
        {self.topic}

        Syllabus:
        {self.syllabus}

        Conversation:
        {recent_history}

        Instructions:
        - Give educational answers
        - Stay relevant to topic
        - Use examples
        - Keep answers concise
        - Be beginner friendly
        """

        try:

            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "openrouter/free",
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.7,
                    "max_tokens": 1000
                },
                timeout=60
            )

            result = response.json()

            print(result)

            if "choices" not in result:

                return f"API Error: {result}"

            answer = result["choices"][0]["message"]["content"]

            self.history.append(
                f"Tutor: {answer}"
            )

            return answer

        except Exception as e:

            return f"Error: {str(e)}"


# =========================================================
# GLOBAL AGENT
# =========================================================

teaching_agent = TeachingGPT()