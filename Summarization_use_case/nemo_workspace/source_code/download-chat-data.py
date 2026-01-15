# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import gdown
import os

dialogSum = 'https://drive.google.com/uc?id=1Uy1PUKdMkVRSY-cUF54L1h5RRVjOg7Gj&confirm=t'
samSum = 'https://drive.google.com/uc?id=12TfEcnqlUcvFtURlbLJBuJ0d0P4qS4d3&confirm=t'
tweetsumm = 'https://drive.google.com/uc?id=1RZpIpMEEfq5ZHvYLGWd23tdI64ZnzsXn&confirm=t'

output_dailog = '../data/DialogSum.zip'
output_sam = '../data/SAMSum.zip'
output_tweet= '../challenge/data/TweetSumm.zip'

gdown.download(dialogSum, output_dailog, quiet=False, proxy=None)
gdown.download(samSum, output_sam, quiet=False, proxy=None)
gdown.download(tweetsumm, output_tweet, quiet=False, proxy=None)
