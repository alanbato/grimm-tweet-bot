def to_tweets(filename):
    with open(filename, 'r') as raw_file:
        with open(filename.split('.')[0]+'_tweets.txt', 'w') as output:
            is_title = False
            char_count = 0  # Max = 140
            current_tweet = []
            for line in raw_file.readlines():
                line = line.strip()
                # Handle Titles
                if is_title:
                    is_title = False
                    output.write(line + '\n')
                    continue
                # Handle the rest
                if line == '':
                    continue
                elif line == '---TITLE---':
                    output.write(' '.join(current_tweet) + '\n')
                    is_title = True
                    continue
                else:
                    curr_line_len = len(line)
                    if char_count + curr_line_len + len(current_tweet) < 140:
                        current_tweet.append(line)
                        char_count += curr_line_len
                    else:
                        # Separate on period to finish the tweet
                        dot_split = line.split('. ', maxsplit=1)
                        if (len(dot_split) > 1 and
                                len(dot_split[0]) + char_count
                                + len(current_tweet) < 140):
                            current_tweet.append(dot_split[0] + '.')
                            # Write the current tweet
                            output.write(' '.join(current_tweet) + '\n')
                            # Continue where we left off
                            current_tweet = [dot_split[1]]
                            char_count = len(current_tweet[0])
                        else:
                            # Period too far, use comma to finish
                            comma_split = line.split(', ', maxsplit=1)
                            if (len(comma_split) > 1 and
                                    len(comma_split[0]) + char_count +
                                    len(current_tweet) < 140):
                                current_tweet.append(comma_split[0] + ',')
                                # Write the current tweet
                                output.write(' '.join(current_tweet) + '\n')
                                # Continue where we left off
                                current_tweet = [comma_split[1]]
                                char_count = len(current_tweet[0])
                            else:
                                # Split on words
                                word_split = line.split()
                                rest = []
                                rest_count = 0
                                for word in word_split:
                                    if (char_count + len(word) +
                                        len(current_tweet) < 140):
                                        current_tweet.append(word)
                                        char_count += len(word)
                                    else:
                                        rest.append(word)
                                        rest_count += len(word)
                                output.write(' '.join(current_tweet) + '\n')
                                current_tweet = rest
                                char_count = rest_count
