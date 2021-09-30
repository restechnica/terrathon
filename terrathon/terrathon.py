import logging

from terrathon import terraform


def apply_or_exit(options):
    logging.info('applying terraform...')

    terraform.run_or_exit(
        subcommand='apply',
        options=options,
        on_success=lambda: logging.info('applied terraform successfully'),
        on_error=lambda: logging.error(f'failed to apply terraform')
    )


def destroy_or_exit(options):
    logging.info('destroying terraform...')

    terraform.run_or_exit(
        subcommand='destroy',
        options=options,
        on_success=lambda: logging.info('destroyed terraform successfully'),
        on_error=lambda: logging.error(f'failed to destroy terraform')
    )


def plan_or_exit(options):
    logging.info('planning terraform...')

    terraform.run_or_exit(
        subcommand='plan',
        options=options,
        on_success=lambda: logging.info('planned terraform successfully'),
        on_error=lambda: logging.error(f'failed to plan terraform')
    )


def select_workspace_or_exit(workspace):
    logging.info(f"selecting terraform '{workspace}' workspace...")

    terraform.run_or_exit(
        subcommand='workspace',
        options=['select', workspace],
        on_success=lambda: logging.info(f"selected terraform workspace '{workspace}' successfully"),
        on_error=lambda: logging.error(f"failed to select terraform '{workspace}' workspace")
    )
