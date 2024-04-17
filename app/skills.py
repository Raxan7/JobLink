


def isskill(line):
	skills = [
    "python", "java", "c++", "javascript", "php", "ruby", "swift", "kotlin",
    "html", "css", "react", "angular", "vue.js", "node.js", "express.js",
    "django", "flask", "spring", "ruby on rails", "asp.net", "jquery",
    "sql", "mysql", "postgresql", "mongodb", "firebase", "oracle",
    "machine learning", "deep learning", "data science", "data analysis",
    "artificial intelligence", "natural language processing",
    "computer vision", "big data", "blockchain", "cloud computing",
    "devops", "ci/cd", "docker", "kubernetes", "aws", "azure", "google cloud",
    "linux", "unix", "windows", "shell scripting", "bash", "powershell",
    "git", "github", "bitbucket", "jira", "trello", "slack", "confluence",
    "agile methodologies", "scrum", "kanban", "waterfall",
    "software development", "web development", "mobile app development",
    "game development", "ui/ux design", "graphic design", "illustration",
    "animation", "video editing", "motion graphics", "photography",
    "content writing", "copywriting", "technical writing", "blogging",
    "seo", "sem", "social media marketing", "email marketing",
    "sales", "marketing", "business development", "customer service",
    "project management", "product management", "quality assurance",
    "test automation", "manual testing", "continuous integration",
    "leadership", "problem solving", "critical thinking",
    "communication", "teamwork", "time management", "adaptability"
]

	#print(skills)
	for s in skills:
		if line.find(s)!=-1:
			#print(s)
			return True
	return False