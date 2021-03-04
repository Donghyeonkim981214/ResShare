from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from . import models as rev_models

class CreatorOnlyView(UserPassesTestMixin):
    def test_func(self):
        user_review = self.get_object()
        if self.request.user == user_review.created_by:
            return True
        else:
            return False

    def handle_no_permission(self):
        user_review = self.get_object()
        return redirect("shareRes:resDetailPage", res_id = user_review.restaurant.id)

class OnlyOneReview(UserPassesTestMixin):
    def test_func(self):
        try:
            user_review = rev_models.Review.objects.get(created_by = self.request.user)
        except rev_models.Review.DoesNotExist:
            user_review = None
        if user_review is not None:
            return False
        return True

    def handle_no_permission(self):
        return redirect(reverse("shareRes:resDetailPage", kwargs={"res_id": self.kwargs['pk']}))