# Copyright 2021 University College London (UCL) Research Software Development
# Group.  See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: Apache-2.0

import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.backends import getlauncher


@rfm.simple_test
class NVidiaHPCGGraceOnlyBenchmark(rfm.RunOnlyRegressionTest):
    valid_systems = [r'-gpu +grace']
    valid_prog_environs = ['default']
    # num_cpus_per_task = 1
    # num_tasks = required
    # num_tasks_per_node = required

    # The program for running the benchmarks.
    executable = 'run_xhpcg_grace_cpuonly.sh'
    # Arguments to pass to the program above to run the benchmarks.
    executable_opts = []
    # Time limit of the job, automatically set in the job script.
    time_limit = '60m'
    # hpcg.dat sets size of grid
    # prerun_cmds.append('cp "$(dirname $(which xhpcg))/hpcg.dat" .')

    # reference = {
    #     "*": {
    #         "flops": (1, None, None, "Gflops/seconds"),
    #     },
    # }

    @run_before('run')
    def replace_launcher(self):
        self.job.launcher = getlauncher('local')()

    @sanity_function
    def validate(self):
        # Check that it's a valid run
        return sn.assert_found(r'VALID with a GFLOP/s rating of=', self.stdout)

    @performance_function('flops')
    def flops(self):
        # This performance pattern parses the output of the program to extract the desired figure of merit.
        return sn.extractsingle(
            r'VALID with a GFLOP/s rating of=(\S+)', self.stdout, 1, float
        )

    # @run_after('setup')
    # def setup_num_tasks(self):
    #     self.set_var_default(
    #         'num_tasks',
    #         self.current_partition.processor.num_cpus
    #         // min(1, self.current_partition.processor.num_cpus_per_core)
    #         // self.num_cpus_per_task,
    #     )
    #     self.set_var_default(
    #         'num_tasks_per_node',
    #         self.current_partition.processor.num_cpus // self.num_cpus_per_task,
    #     )
