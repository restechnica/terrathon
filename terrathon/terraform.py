from cliwrap import cliwrap, utils


def run(subcommand, options, on_success=utils.do_nothing, on_error=utils.do_nothing):
    command = ['terraform', subcommand]
    return cliwrap.run(command=command, options=options, on_success=on_success, on_error=on_error)


def run_or_exit(subcommand, options, on_success=utils.do_nothing, on_error=utils.do_nothing):
    has_succeeded = run(subcommand=subcommand, options=options, on_success=on_success, on_error=on_error)
    utils.exit_if_false(has_succeeded)
