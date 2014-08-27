# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from telemetry.core.backends import form_based_credentials_backend


class GoogleCredentialsBackend(
    form_based_credentials_backend.FormBasedCredentialsBackend):
  def IsAlreadyLoggedIn(self, tab):
    return tab.EvaluateJavaScript(
        'document.getElementById("gb")!== null')

  @property
  def credentials_type(self):
    return 'google'

  @property
  def url(self):
    # pylint: disable=C0301
    # WPR doesn't support having 2 responses for the same URL (with/without
    # session cookie), so after login behaviour differs with/without wpr.
    # Sign-in URL is specified directly to overcome this.
    return 'https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount'

  @property
  def login_form_id(self):
    return 'gaia_loginform'

  @property
  def login_input_id(self):
    return 'Email'

  @property
  def password_input_id(self):
    return 'Passwd'
