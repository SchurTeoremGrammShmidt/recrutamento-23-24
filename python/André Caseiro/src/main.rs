use std::io::{self, Write};

use clap::{command, Command};

fn main() {
    let mut cmd = cmd();

    loop {
        let input = prompt();

        let matches = match cmd.try_get_matches_from_mut(input.split_whitespace()) {
            Ok(matches) => matches,
            Err(_) => {
                println!("{}", cmd.render_help());
                continue;
            }
        };

        match matches.subcommand() {
            Some(("exit", _)) => break,
            Some(("help", _)) => println!("{}", cmd.render_help()),

            _ => unreachable!(
                "Exhausted list of subcommands and subcommand_required prevents `None`"
            ),
        }
    }
}

/// Prompt the user for input and return the entered line.
fn prompt() -> String {
    print!("> ");
    io::stdout().flush().expect("Failed to flush stdout");
    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    input
}

// Build the CLI
fn cmd() -> Command {
    command!()
        .no_binary_name(true)
        .disable_help_flag(true)
        .disable_version_flag(true)
        .disable_help_subcommand(true)
        .subcommand(Command::new("exit").about("Exit the app."))
        .subcommand(Command::new("help").about("Exit the app."))
}
