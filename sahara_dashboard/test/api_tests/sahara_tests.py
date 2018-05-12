# Copyright 2015, Telles Nobrega
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sahara_dashboard import api
from sahara_dashboard.test import helpers as test


class SaharaApiTest(test.SaharaAPITestCase):
    #
    # Cluster
    #
    def test_cluster_create_count(self):
        saharaclient = self.stub_saharaclient()
        saharaclient.clusters.create.return_value = \
            {"Clusters": ['cluster1', 'cluster2']}
        ret_val = api.sahara.cluster_create(self.request,
                                            'name',
                                            'fake_plugin',
                                            '1.0.0',
                                            count=2,
                                            is_public=False,
                                            is_protected=False)

        self.assertEqual(2, len(ret_val['Clusters']))
