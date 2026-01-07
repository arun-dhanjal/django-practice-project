from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question


def quiz_app(request):
    quiz = get_object_or_404(Quiz, pk=1)
    question = quiz.questions.first()

    return render(
        request,
        "quiz_app/quiz_app.html",
        {
            "question_text": question.question_text,
            "choices": question.choices,
            "answer": question.answer,
        },
    )
