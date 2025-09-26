import argparse
import os

from benchmarks.xpk_configs import XpkClusterConfig

# Constants for defining supported actions
DELETE = "delete"


def _handle_delete(
    cluster_config: XpkClusterConfig, user: str, **kwargs
) -> int:
  """Handles the deletion of workloads.

  Args:
      cluster_config: XpkClusterConfig object
      user: User string
      **kwargs: Optional keyword arguments, such as xpk_path
  """
  xpk_path = kwargs.get("xpk_path", "xpk")  # Default to "xpk" if not provided
  first_three_chars = user[:3]
  delete_command = (
      f"python3 {xpk_path}/xpk.py workload delete "
      f"--project={cluster_config.project} --cluster={cluster_config.cluster_name}"
      f" --filter-by-job={first_three_chars} --zone={cluster_config.zone}"
  )
  print(
      f"Deleting workloads starting with: {first_three_chars} using command:"
      f" {delete_command}"
  )
  os.system(delete_command)


def handle_delete_specific_workload(
    cluster_config: XpkClusterConfig, workload_name: str, **kwargs
) -> int:
  """Handles the deletion of workloads with a specific name.

  Args:
      cluster_config: XpkClusterConfig object
      workload_name: workload name
      **kwargs: Optional keyword arguments, such as xpk_path
  """
  xpk_path = kwargs.get("xpk_path", "xpk")  # Default to "xpk" if not provided
  delete_command = (
      f"python3 {xpk_path}/xpk.py workload delete "
      f"--project={cluster_config.project} --cluster={cluster_config.cluster_name}"
      f" --filter-by-job={workload_name} --zone={cluster_config.zone}"
  )
  print(
      f"Deleting workload: {workload_name} using command:"
      f" {delete_command}"
  )
  os.system(f"yes | {delete_command}")


def handle_cmd_args(
    cluster_config: XpkClusterConfig, is_delete: bool, user: str, **kwargs
) -> bool:
  """Parses command-line arguments and executes the specified actions.

  Args:
      cluster_config: Contains Cluster configuration information that's helpful
        for running the actions.
      is_delete: A boolean indicating whether the delete action should be
                 performed.
      **kwargs: Optional keyword arguments to be passed to action handlers.
  """

  # Get user
#   user = os.environ["USER"]

  # Handle actions
  should_continue = True
  if is_delete:
    _handle_delete(cluster_config, user, **kwargs)
    should_continue = False

  return should_continue